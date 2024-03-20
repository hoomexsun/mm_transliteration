from pathlib import Path
from src.mt_ import MMTransliteration
from utils import (
    create_wordmap,
    evaluate,
    get_target_dict,
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
    root_dir = "exp"
    output_path = f"{root_dir}/output.txt"
    labelled_data_path = f"{root_dir}/labelled_data.txt"
    target_dict = get_target_dict(labelled_data_path)
    words = sorted(target_dict.keys())
    output_dict = {word: mt.transliterate(word) for word in words}
    evaluate(target_dict=target_dict, output_dict=output_dict)


if __name__ == "__main__":
    # run()
    eval()
