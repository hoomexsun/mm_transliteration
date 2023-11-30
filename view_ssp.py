import matplotlib.pyplot as plt
import numpy as np


from typing import List

from phoneme_list import calculate_sonority
from to_mm import split_syllable_phonemes


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


def syllabified_word_to_phoneme(word: str, syllable_delimiter: str = "/") -> List[str]:
    syllables = word.split(syllable_delimiter)
    phonemes = []
    for syllable in syllables:
        onset, nucleus, coda = split_syllable_phonemes(syllable)
        phonemes = phonemes + onset + nucleus + coda
    return list(filter(None, phonemes))


def test(words: List[str]):
    words_in_phonemes = [syllabified_word_to_phoneme(word) for word in words]
    view_ssp(words_in_phonemes)


if __name__ == "__main__":
    words = [
        "অং/গ্রেস/শিং/না",
        "অ/কায়/ব/শিং",
        "ষ্টোক্/কী",
        "অ/গর/ট/লা/গী/দ/মক",
    ]
    test(words)
