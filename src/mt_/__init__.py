from enum import Enum
from typing import Dict, List

from tqdm import tqdm

from .b2m import B2P, P2M, Tag, Delimiter
from ..lon_ import Bengali, MMPhoneme

__all__ = ["MMTransliteration", "B2P", "P2M", "Tag", "Delimiter", "make_tokens"]


class Marker(Enum):
    NULL = "x"
    CONTINUOUS = "C"
    BOUNDARY = "B"
    ERROR = "e"


class MMTransliteration:

    def __init__(self, delimiter: str = "/") -> None:
        self.delimiter = delimiter

    def transliterate_words(self, text: str) -> str:
        bn = Bengali()
        b2p = B2P()
        words = []
        for word in tqdm(text.split(), desc="Transliterating..."):
            words.append(self.transliterate(text=word, bn=bn, e2b=b2p))
        return "\n".join(words)

    def transliterate(self, text: str, bn: Bengali | None, b2P: B2P | None) -> str:
        if bn == None or b2p == None:
            bn = Bengali()
            b2p = B2P()

        self.virama = bn.sign_virama

        # Step 0: Adjusting s550 characters
        char_markers = self.__gen_markers(text)

        # Returns final content
        return text

    def __gen_markers(self, text) -> str:
        """Generate Universal Markers. Based on each consecutive charactres

        Args:
            word (str): input word
        """
        char_markers = [Marker.NULL] * (len(text) + 1)
        char_markers[-1] = Marker.BOUNDARY
        for idx in range(len(text) - 1, 0, -1):
            char_markers[idx] = self.mark_two_chars(text[idx - 1], text[idx])
        char_markers[0] = Marker.BOUNDARY
        return char_markers

    # Private methods
    def __adjust_glyph(self, text: str, charmap: Dict[str, str]) -> str:
        for key, value in charmap.items():
            text = text.replace(key, value)
        return text

    def __map_unicode(self, text: str, charmap: Dict[str, str]) -> str:
        # 1. Mapping to correct unicode values (in or of decreasing size of key length)
        sorted_keys = sorted(charmap.keys(), key=len, reverse=True)
        for key in sorted_keys:
            text = text.replace(key, charmap[key])
        # 2. Fix redundant virama
        num_mistypes: int = 2
        for num in range(num_mistypes + 1, 1, -1):
            text = text.replace(self.virama * num, self.virama)
        return text


#! OLD Which should work


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
    total_num_unidentified = 0
    total_num_markers = 0

    for idx, word in enumerate(words):
        # Pass 1: Generate marker based on two consecutive chars
        char_markers = generate_universal_tag(word)

        # Pass 2: Generate marker based on context
        char_markers = generate_contextual_tag(word, char_markers)

        num_unidentified = char_markers.count(Tag.NULL)
        total_num_unidentified += num_unidentified
        total_num_markers += len(char_markers)
        tokens[word] = (
            f"{use_markers(word, char_markers)}\t{mix_markers(word, char_markers)}\t{check_markers(char_markers)}\t{num_unidentified}/{len(char_markers)}"
        )
        if check_markers(char_markers):
            num_completed += 1

    print(f"{num_completed}/{len(words)} | {num_completed/len(words):.2f}% (Completed)")
    print(
        f"{total_num_unidentified}/{total_num_markers} | {total_num_unidentified/total_num_markers:.2f}% (Marker Error)"
    )
    return tokens


# Pass 1: Generate tag based on two consecutive chars
def generate_universal_tag(word: str) -> str:
    bn = Bengali()

    char_markers = [Tag.NULL] * (len(word) + 1)
    char_markers[-1] = Tag.BOUNDARY

    for idx in range(len(word) - 1, 0, -1):
        char_markers[idx] = mark_two_chars(word[idx - 1], word[idx], bn=bn)

    char_markers[0] = Tag.BOUNDARY
    return char_markers


# Pass 2: Generate tag based on context
def generate_contextual_tag(word: str, char_markers: List[str]) -> List[str]:
    bn = Bengali()
    mmP = MMPhoneme()
    b2p = B2P()
    word_len = len(word)
    # 2.1. (V, C, )
    ptr1 = word_len - 1
    while ptr1 != 0:
        if char_markers[ptr1] == Tag.NULL:
            char2 = word[ptr1]
            char1 = word[ptr1 - 1]
            # print(
            #     f"{char1=} | {char2=} | {word[ptr1]=} | {char_markers[ptr1]=} | {word[ptr1+1]=} | {char_markers[ptr1 + 1]=}"
            # )
            if (
                ptr1 > 0
                and char_markers[ptr1 + 1] == Tag.CONTINUOUS
                and word[ptr1 + 1] != bn.sign_virama
                and char2 in bn.independent_consonant_set
                and char1 != bn.sign_virama
            ):
                char_markers[ptr1] = Tag.BOUNDARY
        # Go to previous
        ptr1 -= 1

    # print(f"2.1. {char_markers=}")

    # 2.2: After virama
    ptr1 = word_len - 1
    while ptr1 != 0:
        if char_markers[ptr1] == Tag.NULL and word[ptr1 - 1] == bn.sign_virama:
            char2, phoneme2 = word[ptr1], b2p.charmap.get(word[ptr1], "")
            char1, phoneme1 = word[ptr1 - 2], b2p.charmap.get(word[ptr1 - 2], "")

            # print(f"{char1=} | {phoneme1=} | {char2=} | {phoneme2=}")
            # 2.2.1. Gemination
            if phoneme1 == phoneme2:
                char_markers[ptr1] = Tag.BOUNDARY
            # 2.2.2. Plosive
            elif (
                mmP.get_seivers(phoneme1)[0] == 1 and mmP.get_seivers(phoneme2)[0] == 1
            ):
                char_markers[ptr1] = Tag.BOUNDARY
            # 2.2.3. Fricative
            elif mmP.get_seivers(phoneme1)[0] == 3 or mmP.get_seivers(phoneme2)[0] == 3:
                char_markers[ptr1] = Tag.CONTINUOUS
            # 2.2.4. Approximant (Glide in Sievers)
            elif mmP.get_seivers(phoneme2)[0] == 4:
                char_markers[ptr1] = Tag.CONTINUOUS

            # 2.2.3. Lateral Approximant
            # elif phoneme1 in SIEVERS_PLOSIVE and phoneme2 in SIEVERS_PLOSIVE:
            #     char_markers[ptr1] = Tag.BOUNDARY
            # # 2.2.3. Rhotic
            # elif phoneme1 in SIEVERS_PLOSIVE and phoneme2 in SIEVERS_PLOSIVE:
            #     char_markers[ptr1] = Tag.BOUNDARY
            # # 2.2.3. Nasal
            # elif phoneme1 in SIEVERS_PLOSIVE and phoneme2 in SIEVERS_PLOSIVE:
            #     char_markers[ptr1] = Tag.BOUNDARY
            # else:
            #     char_markers[ptr1] = Tag.BOUNDARY

        # Go to previous
        ptr1 -= 1

    # print(f"2.2. {char_markers=}")

    # 2.3 CC
    ptr1 = word_len - 1
    # while ptr1 != 0:
    #     if char_markers[ptr1] == Tag.NULL:
    #     ptr1 -= 1

    return char_markers


# Universal character type based relations
def mark_two_chars(char1: str, char2: str, bn: Bengali) -> str:
    if char2 == bn.sign_virama:
        return Tag.CONTINUOUS if char1 in bn.independent_consonant_set else Tag.ERROR
    elif char2 in bn.dependent_vowel_set:
        if (
            char1 in bn.independent_consonant_set
            or f"{char1}{char2}" in bn.dependent_diphthongs_set
        ):
            return Tag.CONTINUOUS
        else:
            return Tag.ERROR
    elif char2 in bn.dependent_consonant_set:
        if char1 in bn.independent_consonant_set.union(
            bn.independent_vowel_set, bn.dependent_vowel_set
        ):
            return Tag.CONTINUOUS
        else:
            return Tag.ERROR
    elif char2 in bn.independent_vowel_set:
        if char1 in bn.independent_consonant_set.union(
            bn.independent_vowel_set, bn.independent_consonant_set
        ):
            return Tag.BOUNDARY
        elif f"{char1}{char2}" in bn.dependent_diphthongs_set:
            return Tag.CONTINUOUS
        elif char1 in bn.dependent_vowel_set:
            return Tag.BOUNDARY
        else:
            return Tag.ERROR
    elif char2 in bn.independent_consonant_set:
        return Tag.BOUNDARY if char1 in bn.dependent_consonant_set else Tag.NULL
    else:
        return Tag.NULL


# Utility functions
# 1. For representation
def use_markers(word: str, markers: List[str]) -> str:
    output = ""
    for idx, marker in enumerate(markers[1:]):
        char = word[idx]
        if marker == Tag.BOUNDARY:
            output += f"{char}/"
        elif marker == Tag.NULL:
            output += f"{char}?"
        elif marker == Tag.ERROR:
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
    return False if Tag.NULL in markers else True
