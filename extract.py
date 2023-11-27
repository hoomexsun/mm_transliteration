from typing import Dict, List, Tuple

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

map_mm: Dict[str, str] = {}


def process(word: str) -> str:
    print(word)
    # 1. Split syllables
    syllable_delimiter = "/"
    syllables = word.split(syllable_delimiter)
    output_str = []
    for syllable in syllables:
        # print(f"{syllable=}")
        onset, nucleus, coda = split_components(syllable)
        # print(f"{onset=} | {nucleus=} | {coda=}")
        if not onset:
            nucleus = [PHONEME_TO_MM_BEGIN.get(unit, "") for unit in nucleus]
            coda = [PHONEME_TO_MM_END.get(unit, "") for unit in coda]
        else:
            onset = [PHONEME_TO_MM_BEGIN.get(unit, "") for unit in onset]
            nucleus = [PHONEME_TO_MM_END.get(unit, "") for unit in nucleus]
            coda = [PHONEME_TO_MM_END.get(unit, "") for unit in coda]

        # Special: Use of MM_VOWEL_NUNG
        if (
            coda
            and nucleus
            and coda[0] == MM_LETTER_NGOU_LONSUM
            and nucleus[-1] not in MM_CHEITAP
        ):
            # print("Found use case of nung")
            coda[0] = MM_VOWEL_NUNG

        # print(f"{onset=} | {nucleus=} | {coda=}")
        onset = (
            str(onset[0])
            if len(onset) == 1
            else MM_APUN_IYEK.join(list(filter(None, onset)))
        )
        coda = (
            str(coda[0])
            if len(coda) == 1
            else MM_APUN_IYEK.join(list(filter(None, coda)))
        )
        nucleus = "".join(nucleus)

        # print(f"{onset=} | {nucleus=} | {coda=}")
        output_str.append(f"{onset}{nucleus}{coda}")
    return "".join(output_str)


def split_components(syllable: str) -> Tuple[List[str], List[str], List[str]]:
    onset, nucleus, coda = [], [], []
    to_phoneme = BN_TO_PHONEME
    vowels = PHONEME_VOWELS
    init_phonemes = [to_phoneme.get(char, "") for char in syllable]
    phonemes = []
    # print(f"{init_phonemes=}")
    start_idx = -1
    num_vowel = 0

    comb = PHONEME_DIPHTHONGS_COMBINATION
    diph_found = False
    for idx, phoneme in enumerate(init_phonemes):
        phoneme_pair = "".join(init_phonemes[idx : idx + 2])
        # print(f"{phoneme_pair=}")
        if diph_found:
            diph_found = False
        elif phoneme_pair in comb.keys():
            # print(f"Found diphthong {phoneme_pair}")
            phonemes.append(comb.get(phoneme_pair, phoneme_pair))
            diph_found = True
        else:
            phonemes.append(phoneme)

    # print(f"{phonemes=}")

    for idx, phoneme in enumerate(phonemes):
        if phoneme in vowels:
            # print(f"Found vowel at {idx} and {phoneme=}")
            start_idx = idx
            num_vowel = 1
            while (
                idx + num_vowel < len(phonemes) and phonemes[idx + num_vowel] in vowels
            ):
                num_vowel += 1
                print(f"{idx=} | {num_vowel=}")
            break
    # print(f"{start_idx=} | {idx=} | {num_vowel=}")
    if start_idx != -1:
        onset = phonemes[:start_idx]
        nucleus = phonemes[start_idx : start_idx + num_vowel]
        coda = phonemes[start_idx + num_vowel :]
    elif len(phonemes) == 2:
        onset = phonemes[0]
        nucleus = [PHONEME_X]
        coda = phonemes[1]
    else:
        onset = phonemes
        nucleus = [PHONEME_X]

    return onset, nucleus, coda


if __name__ == "__main__":
    output = process("অং/গ্রেস/শিং/না")
    print(output)
    output = process("অ/কায়/ব/শিং")
    print(output)
    output = process("অ/কোই/বা")
    print(output)
    output = process("অ/গর/ট/লা/গী/দ/মক")
    print(output)

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


# Pass 2 left to combine phoneme
