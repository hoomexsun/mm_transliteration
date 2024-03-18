from pathlib import Path
from src.mt_ import MMTransliteration
from utils import (
    create_wordmap,
    evaluate,
    get_target_dict,
    syllabified_word_to_phoneme,
    to_mm,
    view_ssp,
)


def run(mk_wmap: bool = True) -> None:
    mt = MMTransliteration()

    root_dir = "data"
    data_path = f"{root_dir}/words.txt"
    output_path = f"{root_dir}/output.txt"
    wordmap_path = f"{root_dir}/wordmap"

    content: str = Path(data_path).read_text(encoding="utf-8")
    output: str = mt.correct_words(content)
    Path(output_path).write_text(output, encoding="utf-8")
    Path(output_path).with_suffix(".min").write_text(
        "\n".join(
            sorted({word.strip() for word in output.split("\n") if word.strip()})
        ),
        encoding="utf-8",
    )
    if mk_wmap:
        create_wordmap(content, output, wordmap_path)


def eval() -> None:
    mt = MMTransliteration()
    root_dir = "eval"
    output_path = f"{root_dir}/output.txt"
    labelled_data_path = f"{root_dir}/labelled_data.txt"
    target_dict = get_target_dict(labelled_data_path)
    words = sorted(target_dict.keys())
    output_dict = {word: mt.transliterate(word) for word in words}
    evaluate(target_dict=target_dict, output_dict=output_dict)


def test_ssp():
    words = [
        "অং/গ্রেস/শিং/না",
        "অ/কায়/ব/শিং",
        "ষ্টোক্/কী",
        "অ/গর/ট/লা/গী/দ/মক",
    ]
    words_in_phonemes = [syllabified_word_to_phoneme(word) for word in words]
    view_ssp(words_in_phonemes)


def test_spell():
    words = [
        "অং/গ্রেস/শিং/না",
        "অ/কায়/ব/শিং",
        "অ/কোই/বা",
        # "অ/গর/ট/লা/গী/দ/মক",
        "অ/কু?প্/পা",
    ]
    for word in words:
        output = to_mm(word)
        print(f"{word} -> {output}")


if __name__ == "__main__":
    # run()
    eval()
