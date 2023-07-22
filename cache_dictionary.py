import logging
import os
import re
import json
import unicodedata
from natsort import natsorted
from rich.progress import track
import redis

from config import *
from linguistics_symbols import *

logger = logging.getLogger(__name__)

# Connect to Redis server
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

def cache_json_dictionary():

    logger.info("Writing dictionary to cache...")
    term_banks = get_sorted_term_banks()

    for file_name in track(term_banks, description="Caching dictionary"):
        file_path = os.path.join(ORIGINAL_DICTIONARY_PATH, file_name)
        logger.info(f"Writing {file_name} to cache...")
        with open(file_path, 'r', encoding="utf8") as json_file:
            data = json.load(json_file)

            for term in data:

                # Deserialize the term from JSON dictionary
                term = deserialize_json_dictionary_term(term)

                term = process_cache_term(term)

                # Construct the cache key and remove the key parts from the term
                key = construct_cache_key([
                    term.pop("term_text"),
                    term.pop("pos")
                ])

                # If the term exists in the cache then merge the terms
                if redis_client.exists(key):
                    term = merge_cache_term(key, term)

                # Write the term to cache
                cache_term(key, term)


def process_cache_term(term):

    if term['pos'] not in PARTS_OF_SPEECH and term['pos'] != TERM_INFLECTION_KEY:
        raise ValueError(f"Invalid part of speech {term['pos']} for term {term['term_text']}")

    # normalize diacritics notations
    term = normalize_diacritic_term(term)

    # Process the term based on its lemmatization
    if term['pos'] == TERM_INFLECTION_KEY:
        term = process_inflected_term(term)
    else:
        term = process_lemma_term(term)

    return term


def process_inflected_term(term):
    term['is_lemma'] = str(False)
    # Clear the TERM_INFLECTION_KEY
    del term['tags']
    # Get the pos from the defintion
    term['pos'] = term['definition'][0].split()[0]
    # Get the lemma term text from the defintion
    term['lemma_term_text'] = extract_lemma_term_text(term['definition'][0])
    # Normalize lemma term text by replacing diacritic notation characters with their base form
    term['lemma_term_text'] = normalize_diacritic_text(term['lemma_term_text'])

    return term


def process_lemma_term(term):
    # Process the lemma term
    term['is_lemma'] = str(True)

    return term


def normalize_diacritic_term(term):
    # Check if diacritic notation is present in the term text
    if DIACRITIC_NOTATION_REGEX.findall(unicodedata.normalize('NFKC', term['term_text'])):
        # Set diacritic notation as the original term text
        term['diacritic_notation'] = term['term_text']
        # Normalize term text by replacing diacritic notation characters with their base form
        term['term_text'] = normalize_diacritic_text(term['term_text'])
        # Remove diacritic notation marker definition
        for definition in term["definition"]:
            if re.search(DIACRITIC_FORM_REGEX, definition):
                term["definition"].remove(definition)
    
    return term


def normalize_diacritic_text(text):
    # Normalize text by replacing diacritic notation characters with their base form    
    return DIACRITIC_NOTATION_REGEX.sub(
        lambda match: unicodedata.normalize('NFD', match.group())[0],
        text
    )

def merge_cache_term(cached_term_key, term):

    cached_term = redis_client.hgetall(cached_term_key)
    cached_term = deserialize_cache_term(cached_term_key, cached_term)

    # Update any new values to the cached term
    for term_key, term_value in term.items():

        if term_key == "definition":
            term_value = merge_cache_term_definitions(cached_term["definition"], term)
        else:
            if term_key not in cached_term or cached_term[term_key] != term_value:
                cached_term[term_key] = term_value

    return cached_term


def merge_cache_term_definitions(cache_definitions, term):
    
    term_definitions = term["definition"]
    diacritic_term = "diacritic_notation" in term and term["diacritic_notation"] is not None

    # Update any new values to the cached term
    new_definitions = []

    # Check each definition
    for definition in term_definitions:
        # Check if the definition is already present in the cached definitions
        if definition not in cache_definitions:
            # Save new definitions
            new_definitions.append(definition)

    # Add the new definitions to the set of existing definitions
    if new_definitions:
        if diacritic_term:
            # Append diacritic term definitions to non-diacritic definitions
            cache_definitions.extend(new_definitions)
        else:
            # Prepend non-diacritic definitions to diacritic term definitions
            cache_definitions = new_definitions + cache_definitions
    
    return cache_definitions



def cache_term(key, term):

    term = serialize_cache_term(term)

    # Store the term
    redis_client.hmset(key, mapping=term)


def construct_cache_key(key_parts):

        # Join the key parts with seperator
        return ':'.join(key_parts)


def serialize_json_dictionary_term(term):
    return [
        term['term_text'],
        term['reading'],
        term['tags'],
        "",
        0,
        json.dumps(term['definition'], ensure_ascii=False),
        0,
        ""
    ]


def deserialize_json_dictionary_term(term):
    return {
        'term_text': term[0],
        'reading': term[1] if term[1] != "" else None,
        'tags': term[2],
        'pos': term[2].split()[0],
        'definition': term[5]
    }


def serialize_cache_term(term):
    term["definition"] = json.dumps(term["definition"])

    # Remove the term data values that are None or empty strings
    keys_to_remove = [k for k, v in term.items() if v is None or v == ""]
    for key in keys_to_remove:
        del term[key]

    return term


def deserialize_cache_term(term_key, term):

    term_text, pos = term_key.split(":")

    return {
        'term_text': term_text,
        'pos': pos,
        'reading': term['reading'] if 'reading' in term else None,
        'tags': term['tags'] if 'tags' in term else None,
        'definition': json.loads(term['definition']),
        # Check if string value is 'True'
        'is_lemma': term['is_lemma'] == 'True',
        'lemma_term_text': term['lemma_term_text'] if 'lemma_term_text' in term else None,
        'diacritic_notation': term['diacritic_notation'] if 'diacritic_notation' in term else None
    }


def get_cache_term(key):

    # Retrieve the term from cache
    term_data = redis_client.hgetall(key)

    # Check if the term exists
    if term_data:
        return deserialize_cache_term(key, term_data)
    else:
        # If no matching term is found, return None
        return None


def get_cache_scan(cursor, batch_size):
    # Scan the Redis database for entries
    cursor, term_keys = redis_client.scan(cursor, count=batch_size)
    return cursor, term_keys


def get_sorted_term_banks():
    # Get the sorted list of term banks
    return natsorted([
        file_name for file_name in os.listdir(ORIGINAL_DICTIONARY_PATH)
        if re.match(r'term_bank_\d+\.json', file_name)
    ])


def extract_lemma_term_text(definition):
    match = LEMMA_TERM_TEXT_REGEX.search(definition)
    if match:
        return match.group(1)
    else:
        logger.warning(f"Invalid lemma pointer in definition \"{definition}\"")
        return None
