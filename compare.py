from pathlib import Path
from typing import List

from src.utils.file import read_list
from src.utils.text import pct


syllable_path = Path("data/syllables.txt")
output_path = Path("data/output.txt")


syllables: List[str] = [
    str(syllable_pair.split()[1:]) for syllable_pair in read_list(syllable_path)
]
outputs: List[str] = [
    str(output_pair.split()[1:]) for output_pair in read_list(output_path)
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
    f"Number of words syllabified: {num_done_algo + num_done_manual}/{num_total} | Percentage: {pct(num_done_algo + num_done_manual, num_total)}"
)
print(
    f"---Algorithm: {num_done_algo}/{num_total} | Percentage: {pct(num_done_algo, num_total)}"
)
print(
    f"---Manual: {num_done_manual}/{num_total} | Percentage: {pct(num_done_manual, num_total)}"
)

print(
    f"Number of words unsyllabified: {num_left}/{num_total} | Percentage: {pct(num_left, num_total)}"
)
