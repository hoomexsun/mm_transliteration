from pathlib import Path
from typing import Dict
from src.mt_ import make_tokens
from utils import (
    syllabified_word_to_phoneme,
    syllabify,
    to_mm,
    plot_ssp,
)


SYLLABIFIED_WORDS = [
    "ষ্টোক্/কী",
    "অং/গ্রেস/শিং/না",
    "অ/কায়/ব/শিং",
    "অ/কোই/বা",
    "অ/কু?প্/পা",
    "অ/গর/ট/লা/গী/দ/মক",
]


def test_ssp():
    words_in_phonemes = [
        syllabified_word_to_phoneme(word) for word in SYLLABIFIED_WORDS[:4]
    ]
    plot_ssp(words_in_phonemes)


def test_spell():
    for word in SYLLABIFIED_WORDS:
        output = to_mm(word)
        print(f"{word} -> {output}")


# Test
def test_algo() -> None:
    words = [word.replace("/", "") for word in SYLLABIFIED_WORDS]
    for word in words:
        output = syllabify(word)
        print(f"{word} -> {output}")


# Tokens from test.py
def test_tokens():
    word1 = "অকাম্পাৎ"
    words = [word1]

    words = Path(f"data/words.txt").read_text(encoding="utf-8").strip().split("\n")

    token_path = Path(f"exp2/tokens.txt")
    output_path = Path(f"exp2/output.txt")

    tokens: Dict[str, str] = make_tokens(words)

    token_content = "\n".join([f"{word}\t{token}" for word, token in tokens.items()])
    token_path.write_text(token_content, encoding="utf-8")

    output_content = "\n".join(
        [f"{word}\t{token.split()[0]}" for word, token in tokens.items()]
    )
    output_path.write_text(output_content, encoding="utf-8")


# All from utils.py
def test_main_all():
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
        tokens[word] = (
            f"{syllabified_word}\t{phonemes}\t{transliterated_word}\t{syllabification_done}"
        )

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
