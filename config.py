import os
import re
import unicodedata

from linguistics_symbols import *

# Directory containing the original dictionary
ORIGINAL_DICTIONARY_DIRECTORY = "original_dictionary"

# Directory to place the flattened dictionary
FLATTENED_DICTIONARY_DIRECTORY = "flattened_dictionary"

# Keys for identifying inflected terms
TERM_INFLECTION_KEY = "non-lemma"
DEFINITION_INFLECTION_KEY = "-automated- "

# Working directory
WORKING_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Get the path to the original dictionary directory
ORIGINAL_DICTIONARY_PATH = os.path.join(WORKING_DIRECTORY, ORIGINAL_DICTIONARY_DIRECTORY)

# Create a child directory to store the modified JSON files
FLATTENED_DICTIONARY_PATH = os.path.join(WORKING_DIRECTORY, FLATTENED_DICTIONARY_DIRECTORY)

# NFKC (Normalization Form KC) is a Unicode normalization form that combines characters with diacritical marks
# or similar variations into a more compatible representation for consistent handling of Unicode characters.
DIACRITIC_NOTATION_REGEX = re.compile('|'.join(unicodedata.normalize('NFKC', char) for char in DIACRITIC_NOTATION_CHARACTERS))

LEMMA_TERM_TEXT_REGEX = re.compile(r'->\s*([^}]+)\s*}')

DIACRITIC_FORM_REGEX = re.compile(r"diacritic form \(")