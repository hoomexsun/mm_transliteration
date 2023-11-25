from pathlib import Path
from tqdm import tqdm

from src.utils.file import read_list, write_file, write_text


words_path = Path("data/words.txt")
target_path = Path("data/target.txt")

words = read_list(words_path)
targets = read_list(target_path)

data = [f"{word}\t{target}\t" for word, target in zip(words, targets)]


students_roll = [
    "4017",
    "3041",
    "3040",
    "3037",
    "3036",
    "3033",
    "3025",
    "1012",
]

last_index = 0
num_to_take = 100

for idx, roll in tqdm(enumerate(students_roll), desc="Writing file"):
    start_idx = last_index + idx * num_to_take
    end_idx = last_index + (idx + 1) * num_to_take
    write_text(
        content="\n".join(data[start_idx:end_idx]),
        dest=Path(f"students/{roll}_{start_idx+1}_{end_idx}"),
    )
    temp_index = end_idx
last_index = temp_index

print(f"{last_index=}")
