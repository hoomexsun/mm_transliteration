from pathlib import Path


def main():
    input_path = Path("labelled_data/labelled_data.txt")
    content = input_path.read_text(encoding="utf-8")
    indices = {}
    out = ""
    for line_num, line in enumerate(content.split("\n")):
        num_words = len(line.split())
        out += f"{num_words}\n"
        indices.setdefault(num_words, []).append(line_num + 1)

    output_path = input_path.parent / Path("output_data.txt")
    output_path.write_text(data=out, encoding="utf-8")

    for num, all_line_nums in indices.items():
        index_path = input_path.parent / Path(f"{num}.txt")
        index_path.write_text(data="\n".join(map(str, all_line_nums)), encoding="utf-8")


if __name__ == "__main__":
    main()
