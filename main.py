from src import MMTransliteration
from src.utils.file import read_file, write_csv, write_json, write_text

TEST_DATA_PATH = "data/words.txt"
OUTPUT_PATH = "data/output.txt"
WORDMAP_PATH = "data/wordmap"


def main():
    print(f"Reading from {TEST_DATA_PATH}")
    content = read_file(TEST_DATA_PATH)
    mt = MMTransliteration()
    print(f"Transliterating bengali words..")
    output = mt.transliterate(content)
    write_text(output, OUTPUT_PATH)
    print(f"Saved output in {OUTPUT_PATH}")
    generate_wordmap(content=content, output=output)


def generate_wordmap(content: str, output: str):
    wordmap = {
        word: corrected
        for word, corrected in zip(content.split("\n"), output.split("\n"))
    }
    write_text(
        content="\n".join(
            [f"{word}\t{corrected}" for word, corrected in wordmap.items()]
        ),
        dest=WORDMAP_PATH,
    )
    write_json(wordmap, dest=WORDMAP_PATH)
    write_csv(wordmap, fieldnames=("s550", "bn"), dest=WORDMAP_PATH)
    print(f"Saved wordmap in {WORDMAP_PATH} (text, json and csv)")


if __name__ == "__main__":
    main()
