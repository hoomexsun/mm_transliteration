from pathlib import Path
from typing import List


def compare_syllable(syllable_path: str, output_path: str):

    syllables: List[str] = [
        str(syllable_pair.split()[1:])
        for syllable_pair in Path(syllable_path).read_text(encoding="utf-8").split("\n")
    ]
    outputs: List[str] = [
        str(output_pair.split()[1:])
        for output_pair in Path(output_path).read_text(encoding="utf-8").split("\n")
    ]

    num_total = len(syllables)
    num_left = 0
    num_done_manual = 0
    num_done_algo = 0

    for syllable, output in zip(syllables, outputs):
        if output.find("?") == -1:
            num_done_algo += 1
        elif syllable.find("?") == -1:
            num_done_manual += 1
        else:
            num_left += 1

    print(
        f"Number of words syllabified: {num_done_algo + num_done_manual}/{num_total} | Percentage: {100 * (num_done_algo + num_done_manual) / num_total:.02f}%\n"
        f"---Algorithm: {num_done_algo}/{num_total} | Percentage: {100 * num_done_algo / num_total:.02f}%\n"
        f"---Manual: {num_done_manual}/{num_total} | Percentage: {100 * num_done_manual / num_total:.02f}%\n"
        f"Number of words unsyllabified: {num_left}/{num_total} | Percentage: {100 * num_left / num_total:.02f}%"
    )


if __name__ == "__main__":
    # Test Compare
    syllable_path = "data/syllables.txt"
    output_path = "data/output.txt"
    compare_syllable(syllable_path, output_path)
