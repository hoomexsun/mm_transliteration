from src import MMTransliteration
from src.utils.file import fread, fwrite_csv, fwrite_json, fwrite_text

TEST_DATA_PATH = "data/words.txt"
OUTPUT_PATH = "data/output.txt"
WORDMAP_PATH = "data/wordmap"


def main():
    print(f"Reading from {TEST_DATA_PATH}")
    content = fread(TEST_DATA_PATH)
    mt = MMTransliteration()
    print(f"Transliterating bengali words..")
    output = mt.transliterate(content)
    fwrite_text(output, OUTPUT_PATH)
    print(f"Saved output in {OUTPUT_PATH}")
    generate_wordmap(content=content, output=output)


def generate_wordmap(content: str, output: str):
    wordmap = {
        word: corrected
        for word, corrected in zip(content.split("\n"), output.split("\n"))
    }
    fwrite_text(
        content="\n".join(
            [f"{word}\t{corrected}" for word, corrected in wordmap.items()]
        ),
        file_path=WORDMAP_PATH,
    )
    fwrite_json(wordmap, file_path=WORDMAP_PATH)
    fwrite_csv(wordmap, fieldnames=("s550", "bn"), file_path=WORDMAP_PATH)
    print(f"Saved wordmap in {WORDMAP_PATH} (text, json and csv)")


if __name__ == "__main__":
    main()
