from pathlib import Path
from typing import List

from src.utils.file import fget_list, fwrite_text
from src.resource.bn_alphabet import (
    BN_DEPENDENT_CONSONANT,
    BN_DEPENDENT_VOWEL,
    BN_INDEPENDENT_VOWEL,
    VIRAMA,
)

TYPE_NULL = "x"
TYPE_VIRAMA = "v"
TYPE_INDEPENDENT_VOWEL = "iv"
TYPE_DEPENDENT_VOWEL = "dv"
TYPE_INDEPENDENT_CONSONANT = "ic"
TYPE_DEPENDENT_CONSONANT = "dc"

MARKER_NULL = "x"
MARKER_BOUNDARY = "B"
MARKER_CONTINUOUS = "C"


def make_tokens(words: List[str]):
    tokens = {}
    # Step 1: Prepare Universal Truth
    for word in words:
        # Initialize character types
        char_types = [TYPE_NULL for _ in range(len(word))]

        # Type Assignment
        for idx, char in enumerate(word):
            if char == VIRAMA:
                char_types[idx] = TYPE_VIRAMA
            elif char in BN_DEPENDENT_VOWEL:
                char_types[idx] = TYPE_DEPENDENT_VOWEL
            elif char in BN_DEPENDENT_CONSONANT:
                char_types[idx] = TYPE_DEPENDENT_CONSONANT
            elif char in BN_INDEPENDENT_VOWEL:
                char_types[idx] = TYPE_INDEPENDENT_VOWEL
            else:
                char_types[idx] = TYPE_INDEPENDENT_CONSONANT

        # Initialize character markers
        char_markers = [MARKER_NULL for _ in range(len(word) + 1)]
        char_markers[0] = MARKER_BOUNDARY
        char_markers[-1] = MARKER_BOUNDARY

        # Assign markers according to char or char_type
        for idx, (char, char_type) in enumerate(zip(word, char_types)):
            if char_type == TYPE_VIRAMA:
                char_markers[idx - 1] = MARKER_CONTINUOUS
            if char_type == TYPE_DEPENDENT_VOWEL:
                char_markers[idx] = MARKER_CONTINUOUS
                if idx + 2 < len(word) and char_types[idx + 2] == TYPE_DEPENDENT_VOWEL:
                    char_markers[idx + 1] = MARKER_BOUNDARY
                if idx > 1 and char_types[idx - 2] != TYPE_VIRAMA:
                    char_markers[idx - 1] = MARKER_BOUNDARY
            elif char_type == TYPE_DEPENDENT_CONSONANT:
                char_markers[idx] = MARKER_CONTINUOUS
                char_markers[idx + 1] = MARKER_BOUNDARY

        tokens[
            word
        ] = f"{use_marker(word, char_markers)}\t{'-'.join(char_types)}\t{'-'.join(char_markers)}\t{check_markers(char_markers)}"
    # Step 2: Use BPE

    # Step 3: Build TU
    print("Completed")

    return tokens


def use_marker(word: str, markers: List[str]) -> str:
    output = ""
    for idx, marker in enumerate(markers[1:]):
        char = word[idx]
        if marker == MARKER_BOUNDARY:
            output += f"{char} - "
        else:
            output += char
    return output


def check_markers(markers: List[str]) -> bool:
    return False if MARKER_NULL in markers else True


word1 = "অংগ্রেসশিংনা"
words = [word1]

words = fget_list(Path("data/words.txt"))

output_path = Path("data/tokens.txt")
token_list = make_tokens(words)
token_list = [f"{key}\t{value}" for key, value in token_list.items()]
fwrite_text("\n".join(token_list), output_path)
