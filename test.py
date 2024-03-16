from pathlib import Path
from tqdm import tqdm
from typing import Dict, List
from phoneme_list import (
    BN_INDEPENDENT_CONSONANT,
    BN_TO_PHONEME,
    SIEVERS_FRICATIVE,
    SIEVERS_GLIDE,
    SIEVERS_PLOSIVE,
)

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

ROOT = "data_new"

MARKER_UNIDENTIFIED = "x"
MARKER_BOUNDARY = "B"
MARKER_CONTINUOUS = "C"
MARKER_ERROR = "e"


# Step 1: Syllabify the bengali text
def syllabify(word: str) -> str:
    pass


# Step 2: Convert into phoneme
def phonemize(word: str, syllable_delimiter: str = "/") -> str:
    pass


# Step 3: Build Meetei Mayek words
def spell(word: str, syllable_delimiter: str = "/") -> str:
    pass


# Process all words in a list
def make_tokens(words: List[str]):
    tokens = {}
    num_completed = 0
    error_in_spelling = []
    total_num_unidentified = 0
    total_num_markers = 0

    for idx, word in enumerate(words):
        # for idx, word in enumerate(tqdm(words, desc="Transliterating")):
        # Pass 1: Generate marker based on two consecutive chars
        char_markers = generate_universal_marker(word)

        # Pass 2: Generate marker based on context
        char_markers = generate_contextual_marker(word, char_markers)

        num_unidentified = char_markers.count(MARKER_UNIDENTIFIED)
        total_num_unidentified += num_unidentified
        total_num_markers += len(char_markers)
        tokens[word] = (
            f"{use_markers(word, char_markers)}\t{mix_markers(word, char_markers)}\t{check_markers(char_markers)}\t{num_unidentified}/{len(char_markers)}"
        )
        if check_markers(char_markers):
            num_completed += 1
        if MARKER_ERROR in char_markers:
            error_in_spelling.append(f"{idx+1}\t{word}\t{word}")

    print(f"{num_completed}/{len(words)} | {num_completed/len(words):.2f}% (Completed)")
    print(
        f"{total_num_unidentified}/{total_num_markers} | {total_num_unidentified/total_num_markers:.2f}% (Marker Error)"
    )
    # write_text("\n".join(error_in_spelling), dest=Path(f"{ROOT}/error_in_spelling"))

    return tokens


# Pass 1: Generate marker based on two consecutive chars
def generate_universal_marker(word: str) -> str:
    char_markers = [MARKER_UNIDENTIFIED] * (len(word) + 1)
    char_markers[-1] = MARKER_BOUNDARY

    for idx in range(len(word) - 1, 0, -1):
        char_markers[idx] = mark_two_chars(word[idx - 1], word[idx])

    char_markers[0] = MARKER_BOUNDARY
    return char_markers


# Pass 2: Generate marker based on context
def generate_contextual_marker(word: str, char_markers: List[str]) -> List[str]:
    word_len = len(word)
    # 2.1. (V, C, )
    ptr1 = word_len - 1
    while ptr1 != 0:
        if char_markers[ptr1] == MARKER_UNIDENTIFIED:
            char2 = word[ptr1]
            char1 = word[ptr1 - 1]
            # print(
            #     f"{char1=} | {char2=} | {word[ptr1]=} | {char_markers[ptr1]=} | {word[ptr1+1]=} | {char_markers[ptr1 + 1]=}"
            # )
            if (
                ptr1 > 0
                and char_markers[ptr1 + 1] == MARKER_CONTINUOUS
                and word[ptr1 + 1] != SIGN_VIRAMA
                and char2 in BN_INDEPENDENT_CONSONANT
                and char1 != SIGN_VIRAMA
            ):
                char_markers[ptr1] = MARKER_BOUNDARY
        # Go to previous
        ptr1 -= 1

    # print(f"2.1. {char_markers=}")

    # 2.2: After virama
    ptr1 = word_len - 1
    while ptr1 != 0:
        if char_markers[ptr1] == MARKER_UNIDENTIFIED and word[ptr1 - 1] == SIGN_VIRAMA:
            char2, phoneme2 = word[ptr1], BN_TO_PHONEME.get(word[ptr1], "")
            char1, phoneme1 = word[ptr1 - 2], BN_TO_PHONEME.get(word[ptr1 - 2], "")

            # print(f"{char1=} | {phoneme1=} | {char2=} | {phoneme2=}")
            # 2.2.1. Gemination
            if phoneme1 == phoneme2:
                char_markers[ptr1] = MARKER_BOUNDARY
            # 2.2.2. Plosive
            elif phoneme1 in SIEVERS_PLOSIVE and phoneme2 in SIEVERS_PLOSIVE:
                char_markers[ptr1] = MARKER_BOUNDARY
            # 2.2.3. Fricative
            elif phoneme1 in SIEVERS_FRICATIVE or phoneme2 in SIEVERS_FRICATIVE:
                char_markers[ptr1] = MARKER_CONTINUOUS
            # 2.2.4. Approximant (Glide in Sievers)
            elif phoneme2 in SIEVERS_GLIDE:
                char_markers[ptr1] = MARKER_CONTINUOUS

            # 2.2.3. Lateral Approximant
            # elif phoneme1 in SIEVERS_PLOSIVE and phoneme2 in SIEVERS_PLOSIVE:
            #     char_markers[ptr1] = MARKER_BOUNDARY
            # # 2.2.3. Rhotic
            # elif phoneme1 in SIEVERS_PLOSIVE and phoneme2 in SIEVERS_PLOSIVE:
            #     char_markers[ptr1] = MARKER_BOUNDARY
            # # 2.2.3. Nasal
            # elif phoneme1 in SIEVERS_PLOSIVE and phoneme2 in SIEVERS_PLOSIVE:
            #     char_markers[ptr1] = MARKER_BOUNDARY
            # else:
            #     char_markers[ptr1] = MARKER_BOUNDARY

        # Go to previous
        ptr1 -= 1

    # print(f"2.2. {char_markers=}")

    # 2.3 CC
    ptr1 = word_len - 1
    # while ptr1 != 0:
    #     if char_markers[ptr1] == MARKER_UNIDENTIFIED:
    #     ptr1 -= 1

    return char_markers


# Universal character type based relations
def mark_two_chars(char1: str, char2: str) -> str:
    if char2 == SIGN_VIRAMA:
        return MARKER_CONTINUOUS if char1 in BN_INDEPENDENT_CONSONANT else MARKER_ERROR
    elif char2 in BN_DEPENDENT_VOWEL:
        if (
            char1 in BN_INDEPENDENT_CONSONANT
            or f"{char1}{char2}" in BN_DEPENDENT_DIPHTHONGS
        ):
            return MARKER_CONTINUOUS
        else:
            return MARKER_ERROR
    elif char2 in BN_DEPENDENT_CONSONANT:
        if char1 in BN_INDEPENDENT_CONSONANT.union(
            BN_INDEPENDENT_VOWEL, BN_DEPENDENT_VOWEL
        ):
            return MARKER_CONTINUOUS
        else:
            return MARKER_ERROR
    elif char2 in BN_INDEPENDENT_VOWEL:
        if char1 in BN_DEPENDENT_CONSONANT.union(
            BN_INDEPENDENT_VOWEL, BN_INDEPENDENT_CONSONANT
        ):
            return MARKER_BOUNDARY
        elif f"{char1}{char2}" in BN_DEPENDENT_DIPHTHONGS:
            return MARKER_CONTINUOUS
        elif char1 in BN_DEPENDENT_VOWEL:
            return MARKER_BOUNDARY
        else:
            return MARKER_ERROR
    elif char2 in BN_INDEPENDENT_CONSONANT:
        return (
            MARKER_BOUNDARY if char1 in BN_DEPENDENT_CONSONANT else MARKER_UNIDENTIFIED
        )
    else:
        return MARKER_UNIDENTIFIED


# Utility functions
# 1. For representation
def use_markers(word: str, markers: List[str]) -> str:
    output = ""
    for idx, marker in enumerate(markers[1:]):
        char = word[idx]
        if marker == MARKER_BOUNDARY:
            output += f"{char}/"
        elif marker == MARKER_UNIDENTIFIED:
            output += f"{char}?"
        elif marker == MARKER_ERROR:
            output += f"{char}*"
        else:
            output += char
    return output


# 2. For detailed representation
def mix_markers(word, char_markers):
    output = ""
    for idx in range(len(word)):
        output += char_markers[idx]
        output += f"-{word[idx]}-"
    output += char_markers[len(word)]
    return output


# 3. For checking whether syllabification is complete
def check_markers(markers: List[str]) -> bool:
    return False if MARKER_UNIDENTIFIED in markers else True


# Test
if __name__ == "__main__":
    # word1 = "অংগ্রেসশিংনা"
    word1 = "অকাম্পাৎ"
    words = [word1]

    words = read_list(Path(f"{ROOT}/words.txt"))

    token_path = Path(f"{ROOT}/tokens.txt")
    output_path = Path(f"{ROOT}/output.txt")
    tokens: Dict[str, str] = make_tokens(words)

    token_list = [f"{word}\t{token}" for word, token in tokens.items()]
    write_text("\n".join(token_list), token_path)

    output_list = [f"{word}\t{token.split()[0]}" for word, token in tokens.items()]
    write_text("\n".join(output_list), output_path)
