import json
import logging
import re
import subprocess

from natsort import natsorted
from rich.logging import RichHandler
from rich.progress import Progress, MofNCompleteColumn
import cProfile
import snakeviz

from config import *
import cache_dictionary

logger = logging.getLogger()

profiler = cProfile.Profile()


def flatten_dictionary():
    modified_term_bank = []
    term_batch_counter = 0
    file_counter = 1
    cursor = 0
    batch_size = 10000

    # Get the total number of entries
    total_entries = cache_dictionary.redis_client.dbsize()

    with Progress(
        MofNCompleteColumn(),
        transient=True,
        *Progress.get_default_columns()
        ) as progress:

        task = progress.add_task("Flattening terms...", total=total_entries)

        while True:
            # Scan the Redis datahead for entries
            cursor, term_keys = cache_dictionary.get_cache_scan(cursor, batch_size)

            for key in term_keys:

                term = cache_dictionary.get_cache_term(key)

                # Process the term
                term = process_term(term)

                if term is not None:
                    
                    term = cache_dictionary.serialize_json_dictionary_term(term)

                    modified_term_bank.append(term)

                    term_batch_counter += 1

                    # Update progress bar with the number of term keys processed
                    progress.update(task, advance=1)

                if term_batch_counter % 10000 == 0:
                    # Write the modified term bank to a JSON file
                    write_term_bank_to_file(modified_term_bank, file_counter)              

                    # Clear the modified term bank and increment the file counter
                    modified_term_bank = []
                    file_counter += 1

            # Break the loop if the cursor is back to 0
            if cursor == 0:
                break

        # Write the remaining modified term bank to a JSON file if there are any terms left
        if modified_term_bank:
            write_term_bank_to_file(modified_term_bank, file_counter)


def process_term(current_term_node):
    term_linked_list = []

    seen_current_term_nodes = set()

    while current_term_node:

        term_linked_list.append(current_term_node)

        # Handle inflected term
        if current_term_node["is_lemma"] == False:

            term_text = current_term_node['term_text']
            lemma_term_text = current_term_node['lemma_term_text']
            pos = current_term_node["pos"]
            lemma_key = cache_dictionary.construct_cache_key([lemma_term_text, pos])

            self_reference = term_text == lemma_term_text
            missing_reference = not cache_dictionary.redis_client.exists(lemma_key)
            circular_reference = lemma_term_text in seen_current_term_nodes
            
            if self_reference or missing_reference or circular_reference:
                if self_reference:
                    logging.debug(f"Self-referenced lemma term detected and resolved: {term_text} -> {lemma_term_text}")
                elif missing_reference:
                    logging.debug(f"Missing lemma term reference detected and resolved: {term_text}")
                elif circular_reference:
                    logging.debug(f"Circular lemma term reference detected and resolved: {term_text} -> {term_text}")

                # Fix bad lemma term reference
                # Set term node lemma term text to None and mark as a lemma
                current_term_node['lemma_term_text'] = None
                current_term_node['is_lemma'] = True

                # Stop recursing inflected term nodes
                break

            # Recursively process inflected term node to handle multi-level inflections
            if cache_dictionary.redis_client.exists(lemma_key):
                current_term_node = cache_dictionary.get_cache_term(lemma_key)
            # Stop recursing inflected term nodes
            else:
                current_term_node = None

            seen_current_term_nodes.add(current_term_node['term_text'])

        # Handle lemma term 
        else:
            break

    return merge_term_linked_list(term_linked_list)
    

def merge_term_linked_list(term_linked_list):

    # Lemma term not referenced by inflected term
    if len(term_linked_list) == 1:

        return term_linked_list.pop()
    
    # Lemma term referenced by inflected term
    else:

        head_inflected_term = term_linked_list[0]
        lemma_term = term_linked_list[-1]

        merged_term = head_inflected_term.copy()

        # Update the merged term definition and tags and lemma state
        merged_term["definition"] = merge_term_linked_list_definitions(term_linked_list)
        merged_term["tags"] = lemma_term["tags"]
        merged_term["is_lemma"] = True

        # Return the merged term
        return merged_term


def merge_term_linked_list_definitions(term_linked_list):

    # head_inflected_term = term_linked_list[0]
    lemma_term = term_linked_list[-1]

    # Push the lemma definitions to the top of the head inflected term definitions stack
    merged_term_definitions = lemma_term["definition"].copy()

    # Push the inflected term definitions to the top of the head inflected term definitions stack
    for inflected_term in term_linked_list[:-1]:
        for inflected_definition in inflected_term["definition"]:
            merged_term_definitions.append(modify_inflected_definition(inflected_definition))
   
    return merged_term_definitions


def modify_inflected_definition(definition):

    # Create a copy of the string
    new_definition = definition

    # Remove the pos
    new_definition = re.sub(r'^\S+\s+', '', new_definition)

    # Remove the automation key
    new_definition = new_definition.replace(DEFINITION_INFLECTION_KEY, '')

    # Change {xxx -> xxx} to (xxx -> xxx)
    new_definition = re.sub(r'\{([^}]*)\}', r'(\1)', new_definition)

    # Remove (->xxx)
    new_definition = re.sub(r'\s\(->[^)]*\)', '', new_definition)

    return new_definition


def write_term_bank_to_file(term_bank, file_counter):

    file_name = f"term_bank_{file_counter}.json"
    file_path = os.path.join(FLATTENED_DICTIONARY_PATH, file_name)

    logger.info(f"Writing {file_name} to disk...")

    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(term_bank, file, ensure_ascii=False)


def initialize():
    
    profiler.enable()

    # Set up logging with RichHandler
    logger.addHandler(RichHandler(show_time=False, show_path=False))

    # logger.setLevel(logging.DEBUG)
    logger.setLevel(logging.INFO)

    # Enable RDB persistence to save every 3600 seconds if at least 1 key changed
    cache_dictionary.redis_client.config_set('save', '3600 1')  


def main():

    # Clear the Redis data
    # cache_dictionary.redis_client.flushdb()

    # logging.info(f"Redis data size: {cache_dictionary.redis_client.dbsize()}")

    # cache_dictionary.cache_json_dictionary()

    # term = [
    # "bíli ste protivili",
    # "",
    # "non-lemma",
    # "",
    # 0,
    # [
    #     "verb -automated- {bíli ste protivili -> protiviti} second-person plural past pluperfect (->protiviti)"
    # ],
    # 0,
    # ""
    # ]


    # # Deserialize the term from JSON dictionary
    # term = cache_dictionary.deserialize_json_dictionary_term(term)
    # cache_dictionary.process_cache_term(term)

    # # Construct the cache key and remove the key parts from the term
    # key = cache_dictionary.construct_cache_key([
    #     term.pop("term_text"),
    #     term.pop("pos")
    # ])

    # # If the term exists in the cache then merge the terms
    # if cache_dictionary.redis_client.exists(key):
    #     term = cache_dictionary.merge_cache_term(key, term)
    #     a = 1

    flatten_dictionary()


def cleanup():

    cache_dictionary.redis_client.close()

    profiler.disable()

    # # Save the profiling results to a file
    # output_file = "profiling_results.prof"
    # profiler.dump_stats(output_file)

    # # Launch SnakeViz using the subprocess module
    # subprocess.run(["snakeviz", output_file])


if __name__ == "__main__":

    initialize()

    main()

    cleanup()


