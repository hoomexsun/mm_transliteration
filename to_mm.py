from typing import Dict, List, Set, Tuple

from phoneme_list import (
    BN_TO_PHONEME,
    MM_APUN_IYEK,
    MM_CHEITAP,
    MM_LETTER_NGOU_LONSUM,
    MM_VOWEL_NUNG,
    PHONEME_DIPHTHONGS_COMBINATION,
    PHONEME_TO_MM_BEGIN,
    PHONEME_TO_MM_END,
    PHONEME_VOWELS,
    PHONEME_X,
)


# f(syllable) = (onset, nucleus, coda)
def split_syllable_phonemes(syllable: str) -> Tuple[List[str], List[str], List[str]]:
    onset, nucleus, coda = [], [], []
    to_phoneme: Dict[str, str] = BN_TO_PHONEME
    vowels: Set[str] = PHONEME_VOWELS
    diph_combinations: Dict[str, str] = PHONEME_DIPHTHONGS_COMBINATION
    diph_found: bool = False
    start_idx: int = -1
    num_vowel: int = 0
    phonemes: List[str] = []
    schwa: str = PHONEME_X

    # 1. Transform every bengali character into respective phoneme
    init_phonemes = [to_phoneme.get(char, "") for char in syllable]

    # 2. Combine phoneme to form diphthong if exists (Pass 1)
    for idx, phoneme in enumerate(init_phonemes):
        # 2.1. Pair up every two character
        phoneme_pair = "".join(init_phonemes[idx : idx + 2])
        if diph_found:
            diph_found = False
        # 2.2. Check if phoneme pair is a candidate for diphthongs
        elif phoneme_pair in diph_combinations.keys():
            # 2.2.1. If so, then replace the phoneme pair with the diphthongs
            phonemes.append(diph_combinations.get(phoneme_pair, phoneme_pair))
            diph_found = True  # To skip next phoneme
        else:
            # 2.2.2. Else, leave the phoneme as it is
            phonemes.append(phoneme)

    # 3. Find nucleus in the syllable
    for idx, phoneme in enumerate(phonemes):
        # 3.1. Check if phoneme is a vowel
        if phoneme in vowels:
            # 3.1.1. Get index of first phoneme of nucleus
            start_idx = idx
            num_vowel = 1
            # 3.1.2. Check if the next phoneme is also a part of nucleus
            while (
                idx + num_vowel < len(phonemes) and phonemes[idx + num_vowel] in vowels
            ):
                # 3.1.2.1. Increment number of phonemes in nucleus
                num_vowel += 1
            # 3.1.3. Break
            break

    # 4. Split components using start_idx and num_vowels
    # 4.1. If nucleus is found
    if start_idx != -1:
        # 4.1.1. Split onset, nucleus and coda
        onset = phonemes[:start_idx]
        nucleus = phonemes[start_idx : start_idx + num_vowel]
        coda = phonemes[start_idx + num_vowel :]
    # 4.2. If there are two consonant phonemes
    elif len(phonemes) == 2:
        # 4.2.1. Split into onset and coda and add schwa in nucleus
        onset = phonemes[0]
        nucleus = [schwa]
        coda = phonemes[1]
    # 4.3. Else
    else:
        # 4.3.1 Add schwa in nucleus
        onset = phonemes
        nucleus = [schwa]

    # 5. Return (onset, nucleus, coda)
    return list(onset), list(nucleus), list(coda)


# f(onset, nucleus, coda) = mm_string
def write_mm(onset: List[str], nucleus: List[str], coda: List[str]) -> str:
    begin_dict: Dict[str, str] = PHONEME_TO_MM_BEGIN
    end_dict: Dict[str, str] = PHONEME_TO_MM_END
    ngou_lonsum: str = MM_LETTER_NGOU_LONSUM
    cheitap: Set[str] = MM_CHEITAP
    nung: str = MM_VOWEL_NUNG
    apun: str = MM_APUN_IYEK

    # 1. Get onset characters using begin_dict
    onset = [begin_dict.get(phoneme, "") for phoneme in onset]

    # 2. Get nucleus characters using begin_dict if there is no onset or else using end_dict
    nucleus = (
        [begin_dict.get(phoneme, "") for phoneme in nucleus]
        if not onset
        else [end_dict.get(phoneme, "") for phoneme in nucleus]
    )

    # 3. Get coda characters using end_dict
    coda = [end_dict.get(phoneme, "") for phoneme in coda]

    # 4. Use nung if ngou lonsum is used without cheitap on its left
    if coda and nucleus and coda[0] == ngou_lonsum and nucleus[-1] not in cheitap:
        coda[0] = nung

    # 5. Add apun to denote consonants cluster in both onset as well as coda
    onset = onset[0] if len(onset) == 1 else apun.join(list(filter(None, onset)))
    coda = coda[0] if len(coda) == 1 else apun.join(list(filter(None, coda)))
    nucleus = "".join(nucleus)

    # 6. Return output string formed using onset, nucleus and coda
    return f"{onset}{nucleus}{coda}"


def to_mm(syllabified_word: str, syllable_delimiter: str = "/") -> str:
    # 1. Split syllabified word into syllables
    syllables = syllabified_word.split(syllable_delimiter)
    output_str = []
    # 2. For every syllable
    for syllable in syllables:
        # 2.1. Get syllable components
        onset, nucleus, coda = split_syllable_phonemes(syllable)
        # 2.2. Transform to Meetei Mayek Characters
        output_str.append(write_mm(onset, nucleus, coda))
    return "".join(output_str)


# Test
def test(words: List[str]) -> None:
    for word in words:
        output = to_mm(word)
        print(f"{word} -> {output}")


if __name__ == "__main__":
    words = [
        "অং/গ্রেস/শিং/না",
        "অ/কায়/ব/শিং",
        "অ/কোই/বা",
        # "অ/গর/ট/লা/গী/দ/মক",
        "অ/কু?প্/পা",
    ]
    test(words)


# Algorithm: Syllable Splitting and Meetei Mayek Transformation

# Split Syllable Components Algorithm (split_syllable_components):

# Input: syllable (Bengali syllable in Unicode)

# Output: (onset, nucleus, coda)

# Initialize empty lists onset, nucleus, and coda.
# Create a mapping to_phoneme from Bengali characters to corresponding phonemes.
# Identify vowels and diphthongs using pre-defined lists.
# Iterate over the phonemes of the syllable:
# Transform Bengali characters into phonemes using to_phoneme.
# Combine adjacent phonemes into diphthongs if they match pre-defined combinations.
# Identify the nucleus by finding consecutive vowels.
# Split the components into onset, nucleus, and coda based on the nucleus.
# If there is no nucleus:
# If there are two consonant phonemes, split into onset and coda and add schwa in nucleus.
# If there is only one phoneme, add schwa in nucleus.
# Return (onset, nucleus, coda).
# Meetei Mayek Transformation Algorithm (write_mm):

# Input: onset, nucleus, and coda lists of phonemes

# Output: Meetei Mayek string

# Create dictionaries (begin_dict, end_dict, ngou_lonsum, cheitap, nung, apun) for Meetei Mayek characters.
# Use dictionaries to convert onset, nucleus, and coda phonemes into Meetei Mayek characters.
# If ngou_lonsum is used without cheitap on its left, replace it with nung.
# Add apun to denote consonant clusters in both onset and coda.
# Return the concatenated string formed using onset, nucleus, and coda.
# Main Transformation Algorithm (to_mm):

# Input: syllabified_word (Bengali word with syllables separated by a delimiter) and optional syllable_delimiter

# Output: Meetei Mayek representation of the word

# Split the input syllabified_word into individual syllables using the specified syllable_delimiter.
# For each syllable:
# Use split_syllable_components to get onset, nucleus, and coda.
# Use write_mm to transform phonemes into Meetei Mayek characters.
# Append the result to an output list.
# Concatenate the Meetei Mayek representations of individual syllables.
# Return the final Meetei Mayek representation.
# Test Algorithm (test):

# Input: words (list of Bengali words)

# Output: None

# For each word in the input list:
# Apply the to_mm function to get the Meetei Mayek representation.
# Print the original word and its Meetei Mayek representation.
