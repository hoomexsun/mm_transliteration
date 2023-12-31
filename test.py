from pathlib import Path
from tqdm import tqdm
from typing import Dict, List

from src.utils.file import read_list, write_text
from src.assets.bn_alphabet import (
    BN_DEPENDENT_CONSONANT,
    BN_DEPENDENT_VOWEL,
    BN_INDEPENDENT_VOWEL,
    LETTER_RA,
    LETTER_YA,
    SIGN_VIRAMA,
    BN_DEPENDENT_DIPHTHONGS,
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
    for word in tqdm(words, desc="Transliterating"):
        # Initialize character types
        char_types = [TYPE_NULL for _ in range(len(word))]

        # Type Assignment
        for idx, char in enumerate(word):
            if char == SIGN_VIRAMA:
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
        # Marker indices
        # idx -> previous + marker + current
        # idx + 1 -> current + marker + next
        # idx - 1 -> previous of previous + marker + previous
        # Pass 1
        for idx, (char, char_type) in enumerate(zip(word, char_types)):
            # Character based
            if char == SIGN_VIRAMA:
                char_markers[idx] = MARKER_CONTINUOUS
                if idx == 1:
                    char_markers[idx + 1] = MARKER_CONTINUOUS
                if idx + 1 < len(word) and (
                    word[idx + 1] == LETTER_RA or word[idx + 1] == LETTER_YA
                ):
                    char_markers[idx + 1] = MARKER_CONTINUOUS
                if idx + 1 < len(word) and word[idx - 1] == word[idx + 1]:
                    char_markers[idx + 1] = MARKER_BOUNDARY
            elif idx + 1 < len(word) and word[idx : idx + 2] in BN_DEPENDENT_DIPHTHONGS:
                char_markers[idx + 1] = MARKER_CONTINUOUS
            # Type based
            if char_type == TYPE_DEPENDENT_VOWEL:
                char_markers[idx] = MARKER_CONTINUOUS
                if idx + 2 < len(word) and (
                    char_types[idx + 2] == TYPE_DEPENDENT_VOWEL
                    or char_types[idx + 2] == TYPE_DEPENDENT_CONSONANT
                ):
                    char_markers[idx + 1] = MARKER_BOUNDARY
                if idx > 1 and char_types[idx - 2] != TYPE_VIRAMA:
                    char_markers[idx - 1] = MARKER_BOUNDARY
            elif char_type == TYPE_DEPENDENT_CONSONANT:
                char_markers[idx] = MARKER_CONTINUOUS
                char_markers[idx + 1] = MARKER_BOUNDARY
            elif idx + 1 < len(word) and char_types[idx + 1] == TYPE_INDEPENDENT_VOWEL:
                char_markers[idx + 1] = MARKER_BOUNDARY

        # Pass 2

        # for idx, (char, char_type) in enumerate(zip(word, char_types)):
        #     if char == SIGN_VIRAMA or idx == len(word) - 1:
        #         if (
        #             idx + 1 < len(word)
        #             and idx > 1
        #             and char_markers[idx + 1] == MARKER_BOUNDARY
        #             and (
        #                 char_types[idx - 1] == BN_DEPENDENT_CONSONANT
        #                 or char_types[idx - 1] == BN_DEPENDENT_VOWEL
        #             )
        #             and char_markers[idx] == MARKER_NULL
        #         ):
        #             char_markers[idx - 1] = MARKER_CONTINUOUS

        tokens[
            word
        ] = f"{use_marker(word, char_markers)}\t{check_markers(char_markers)}\t{'/'.join(char_markers)}\t{'/'.join(char_types)}"
    # Step 2: Use BPE

    # Step 3: Build TU

    return tokens


def use_marker(word: str, markers: List[str]) -> str:
    output = ""
    for idx, marker in enumerate(markers[1:]):
        char = word[idx]
        if marker == MARKER_BOUNDARY:
            output += f"{char}/"
        elif marker == MARKER_NULL:
            output += f"{char}?"
        else:
            output += char
    return output


def check_markers(markers: List[str]) -> bool:
    return False if MARKER_NULL in markers else True


word1 = "অংগ্রেসশিংনা"
words = [word1]

words = read_list(Path("data/words.txt"))

token_path = Path("data/tokens.txt")
output_path = Path("data/output.txt")
tokens: Dict[str, str] = make_tokens(words)


token_list = [f"{word}\t{token}" for word, token in tokens.items()]
write_text("\n".join(token_list), token_path)

output_list = [f"{word}\t{token.split()[0]}" for word, token in tokens.items()]
write_text("\n".join(output_list), output_path)
