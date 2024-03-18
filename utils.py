import csv
import json
import os
from pathlib import Path
from typing import Dict

import enchant
from matplotlib import pyplot as plt


def create_wordmap(content: str, output: str, wordmap_path: str | Path):
    wordmap = {
        word: transliterated
        for word, transliterated in zip(content.split("\n"), output.split("\n"))
    }

    # Save in txt format
    txt_path = Path(wordmap_path).with_suffix(".txt")
    txt_path.write_text(
        "\n".join([f"{word}\t{corrected}" for word, corrected in wordmap.items()]),
        encoding="utf-8",
    )

    # Save in json format
    json_path = Path(wordmap_path).with_suffix(".json")
    json_path.write_text(json.dumps(wordmap, ensure_ascii=False), encoding="utf-8")

    # Save in csv format
    csv_path = Path(wordmap_path).with_suffix(".csv")
    with csv_path.open(mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=("s550", "bn"))
        writer.writeheader()
        for word_s550, word_bn in wordmap.items():
            writer.writerow({"s550": word_s550, "bn": word_bn})


# \t as delimiter
def get_target_dict(labelled_data_path: str | Path) -> Dict[str, str]:
    lines = sorted(
        Path(labelled_data_path).read_text(encoding="utf-8").strip().split("\n")
    )
    target_dict = {}
    for line in lines:
        word, target = line.split("\t")
        target_dict[word] = target
    return target_dict


# CER -> normalize Levenshtein distance to [0, 1]
# d(a,b) / max(len(a), len(b))
def evaluate(target_dict: Dict[str, str], output_dict: Dict[str, str]):
    words = sorted(target_dict.keys())
    num_word_mismatch = 0
    total_edit_distance = 0
    total_chars = 0
    for word in words:
        target = target_dict.get(word, "")
        output = output_dict.get(word, "")
        if target != output:
            num_word_mismatch += 1
        edit_distance = enchant.utils.levenshtein(target, output)
        total_edit_distance += edit_distance
        total_chars += max(len(target), len(output))

    word_mismatch_rate = num_word_mismatch / len(words) * 100

    print(total_chars)
    print(total_edit_distance)
    cer = total_edit_distance / total_chars * 100
    word_accuracy = f"{100-word_mismatch_rate:02f}"
    character_accuracy = f"{100-cer:02f}"

    # Print evaluation
    print(f"Word Mismatch Rate (WMR) = {word_mismatch_rate}")
    print(f"Character Error Rate (CER) = {cer}")

    print()

    # Save evaluation
    os.makedirs("eval", exist_ok=True)
    Path("eval/eval.txt").write_text(
        f"WMR={word_mismatch_rate}\nCER={cer}\nAccuracy(word)={word_accuracy}"
        + f"\nAccuracy(character)={character_accuracy}"
    )

    # Save output
    Path("data/words.txt").write_text("\n".join(words), encoding="utf-8")
    outputs = [f"{word}\t{output}" for word, output in output_dict.items()]
    Path("data/outputs.txt").write_text("\n".join(outputs), encoding="utf-8")


#! OLD


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


def syllabified_word_to_phoneme(word: str, syllable_delimiter: str = "/") -> List[str]:
    syllables = word.split(syllable_delimiter)
    phonemes = []
    for syllable in syllables:
        onset, nucleus, coda = split_syllable_phonemes(syllable)
        phonemes = phonemes + onset + nucleus + coda
    return list(filter(None, phonemes))


def view_ssp(words_in_phonemes: List[str]) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    for i, phonemes in enumerate(words_in_phonemes):
        row = i // 2
        col = i % 2

        sonority_values = [
            calculate_sonority(phoneme, "parker") for phoneme in phonemes
        ]
        y = np.array(sonority_values)

        phoneme_labels = [f"{idx}/{phoneme}" for idx, phoneme in enumerate(phonemes)]

        axes[row, col].plot(phoneme_labels, y, marker="*", label=phonemes)

    plt.tight_layout()
    plt.show()
