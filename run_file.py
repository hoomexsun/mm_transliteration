from pathlib import Path
from typing import List

from tqdm import tqdm

from src.utils.file import read_list, write_text
from syllabification import syllabify
from to_mm import split_syllable_phonemes, to_mm


def main():
    words_path = Path("data/words.txt")
    tokens_path = Path("data/tokens.txt")
    syllabified_words_path = Path("data/syllabified_words.txt")
    transliterated_words_path = Path("data/transliterated_words.txt")

    syllable_delimiter = "/"
    unclear_marker = "?"

    words: List[str] = read_list(words_path)
    tokens = {}
    syllabified_words = {}
    transliterated_words = {}
    for word in tqdm(words, desc="Transliterating"):
        syllabified_word = syllabify(word)[:-1]
        syllabification_done = unclear_marker not in syllabified_word
        # 1. Syllabified word
        syllabified_words[word] = syllabified_word
        phonemes = []
        changed = syllabified_word.replace(unclear_marker, syllable_delimiter)
        for syllable in changed.split(syllable_delimiter):
            onset, nucleus, coda = split_syllable_phonemes(syllable)
            phonemes = phonemes + onset + nucleus + coda
        phonemes = " ".join(phonemes)
        # 2. Transliterated word
        transliterated_word = to_mm(changed) if syllabification_done else ""
        transliterated_words[word] = transliterated_word
        # 3. Token
        tokens[
            word
        ] = f"{syllabified_word}\t{phonemes}\t{transliterated_word}\t{syllabification_done}"

    syllabified_words_list: List[str] = [
        f"{word}\t{syllabified_word}"
        for word, syllabified_word in syllabified_words.items()
    ]
    write_text("\n".join(syllabified_words_list), syllabified_words_path)

    transliterated_words_list: List[str] = [
        f"{word}\t{transliterated_word}"
        for word, transliterated_word in transliterated_words.items()
    ]
    write_text("\n".join(transliterated_words_list), transliterated_words_path)

    tokens_list: List[str] = [f"{word}\t{token}" for word, token in tokens.items()]
    write_text("\n".join(tokens_list), tokens_path)


if __name__ == "__main__":
    main()
