from typing import Dict, List

from phoneme_list import (
    BN_DEPENDENT_CONSONANT,
    BN_DEPENDENT_DIPHTHONGS,
    BN_DEPENDENT_VOWEL,
    BN_INDEPENDENT_VOWEL,
    BN_SIGN_VIRAMA,
    BN_TO_PHONEME,
    PHONEME_J,
    PHONEME_R,
    calculate_sonority,
)

MARKER_NULL = "x"
MARKER_BOUNDARY = "B"
MARKER_CONTINUOUS = "C"

SYLLABLE_DELIMITER = "/"
UNCLEAR_DELIMITER = "?"


def syllabify(word: str) -> str:
    TYPE_NULL = "x"
    TYPE_VIRAMA = "v"
    TYPE_INDEPENDENT_VOWEL = "iv"
    TYPE_DEPENDENT_VOWEL = "dv"
    TYPE_INDEPENDENT_CONSONANT = "ic"
    TYPE_DEPENDENT_CONSONANT = "dc"

    marker_null: str = MARKER_NULL
    marker_boundary: str = MARKER_BOUNDARY
    marker_continuous: str = MARKER_CONTINUOUS

    to_phoneme: Dict[str, str] = BN_TO_PHONEME

    # 0. Init
    # 0.1. Character types
    char_types = [TYPE_NULL for _ in range(len(word))]
    # 0.2. Phonemes
    phonemes = [to_phoneme.get(char, "") for char in word]
    # 0.3. Character markers
    char_markers = [marker_null for _ in range(len(word) + 1)]
    char_markers[0], char_markers[-1] = marker_boundary, marker_boundary

    # 1. Assign character types
    for idx, char in enumerate(word):
        if char == BN_SIGN_VIRAMA:
            char_types[idx] = TYPE_VIRAMA
        elif char in BN_DEPENDENT_VOWEL:
            char_types[idx] = TYPE_DEPENDENT_VOWEL
        elif char in BN_DEPENDENT_CONSONANT:
            char_types[idx] = TYPE_DEPENDENT_CONSONANT
        elif char in BN_INDEPENDENT_VOWEL:
            char_types[idx] = TYPE_INDEPENDENT_VOWEL
        else:
            char_types[idx] = TYPE_INDEPENDENT_CONSONANT

    # 2. Assign character markers
    for idx, (char, char_type, phoneme) in enumerate(zip(word, char_types, phonemes)):
        # 2.1. Character based
        if char == BN_SIGN_VIRAMA:
            char_markers[idx] = marker_continuous
            if idx == 1:
                char_markers[idx + 1] = marker_continuous

            if idx + 1 < len(word) and word[idx - 1] == word[idx + 1]:
                char_markers[idx + 1] = marker_boundary
        elif (
            idx + 1 < len(word) and str(word[idx : idx + 2]) in BN_DEPENDENT_DIPHTHONGS
        ):
            char_markers[idx + 1] = marker_continuous

        # 2.2. Phoneme based
        if char == BN_SIGN_VIRAMA and idx + 1 < len(phonemes):
            if phonemes[idx + 1] == PHONEME_R or phonemes[idx + 1] == PHONEME_J:
                char_markers[idx + 1] = marker_continuous
            elif (
                calculate_sonority(phoneme) == 1
                and calculate_sonority(phonemes[idx + 1]) == 1
            ):
                char_markers[idx + 1] = marker_boundary

        # 2.3. Type based
        if char_type == TYPE_DEPENDENT_VOWEL:
            char_markers[idx] = marker_continuous
            if idx + 2 < len(word) and (
                char_types[idx + 2] == TYPE_DEPENDENT_VOWEL
                or char_types[idx + 2] == TYPE_DEPENDENT_CONSONANT
            ):
                char_markers[idx + 1] = marker_boundary
            if idx > 1 and char_types[idx - 2] != TYPE_VIRAMA:
                char_markers[idx - 1] = marker_boundary
        elif char_type == TYPE_DEPENDENT_CONSONANT:
            char_markers[idx] = marker_continuous
            char_markers[idx + 1] = marker_boundary
        elif idx + 1 < len(word) and char_types[idx + 1] == TYPE_INDEPENDENT_VOWEL:
            char_markers[idx + 1] = marker_boundary

    return as_str(word, char_markers)


# Utility functions
def as_str(word: str, markers: List[str]) -> str:
    output = ""
    for idx, marker in enumerate(markers[1:]):
        char = word[idx]
        if marker == MARKER_BOUNDARY:
            output += f"{char}{SYLLABLE_DELIMITER}"
        elif marker == MARKER_NULL:
            output += f"{char}{UNCLEAR_DELIMITER}"
        else:
            output += char
    return output


# Test
def test(words: List[str]) -> None:
    for word in words:
        output = syllabify(word)
        print(f"{word} -> {output}")


if __name__ == "__main__":
    words = [
        "অংগ্রেসশিংনা",
        "অকায়বশিং",
        "অকোইবা",
        "অগরটলাগীদমক",
    ]
    test(words)
