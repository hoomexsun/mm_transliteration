from typing import Dict, List

map_mm: Dict[str, str] = {}


def extract(words: List[str]):
    extracted = [extract_one(word) for word in words]

    def extract_one(word: str) -> str:
        return "".join([map_the_chars(syllable) for syllable in word.split("/")])

    def map_the_chars(syllable: str) -> str:
        units = []
        track = 0
        for char in syllable:
            pass
        return ""


def assign_phoneme(word: str) -> str:
    pass


# Algorithm
# Input: Syllabified bengali word
# Output: Transliterated meetei mayek word


# convert each character into the respective phonemes
# Improve the phoneme conversion by searching for diphthongs and treat it as single phoneme
# Split word into syllables using a boundary character
# For each syllable
# Find the nucleus
# Assign everything before nucleus as onset if it exists and after nucleus as coda
# If there is no onset, map nucleus using PHONEME_TO_MM_BEGIN and code using PHONEME_TO_MM_END
# Else, map onset using PHONEME_TO_MM_BEGIN, nucleus and coda using PHONEME_TO_MM_END
# Add apun, if there are multiple character in onset or coda between the characters
# Add apun, if nucleus ends with character other than MM_CHEITAPS and coda is not empty. [EXPERIMENTAL]
# Join onset, nucleus, coda and return
