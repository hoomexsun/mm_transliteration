import csv
import json

from pathlib import Path
from src.mt_ import MMTransliteration

TEST_DATA_PATH = "data/words.txt"
OUTPUT_PATH = "data/output.txt"
WORDMAP_PATH = "data/wordmap"


def main(
    data_path: str | Path = TEST_DATA_PATH,
    output_path: str | Path = OUTPUT_PATH,
    mk_wmap: bool = True,
    wordmap_path: str | Path = WORDMAP_PATH,
):
    content: str = Path(data_path).read_text(encoding="utf-8")
    mt = MMTransliteration()
    output: str = mt.transliterate_words(content)
    Path(output_path).write_text(output, encoding="utf-8")
    Path(output_path).with_suffix(".min").write_text(
        "\n".join(
            sorted({word.strip() for word in output.split("\n") if word.strip()})
        ),
        encoding="utf-8",
    )
    if mk_wmap:
        wordmap = {
            word: transliterated
            for word, transliterated in zip(content.split("\n"), output.split("\n"))
        }
        # 1. Save in txt format
        txt_path = Path(wordmap_path).with_suffix(".txt")
        txt_path.write_text(
            "\n".join([f"{word}\t{corrected}" for word, corrected in wordmap.items()]),
            encoding="utf-8",
        )
        # 2. Save in json format
        json_path = Path(wordmap_path).with_suffix(".json")
        json_path.write_text(json.dumps(wordmap, ensure_ascii=False), encoding="utf-8")
        # 3. Save in csv format
        csv_path = Path(wordmap_path).with_suffix(".csv")
        with csv_path.open(mode="w", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=("s550", "bn"))
            writer.writeheader()
            for word_s550, word_bn in wordmap.items():
                writer.writerow({"s550": word_s550, "bn": word_bn})


if __name__ == "__main__":
    main()
