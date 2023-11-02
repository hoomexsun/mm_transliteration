import csv
import json
from pathlib import Path
from typing import Dict, List, Tuple
from .text import get_unicode_string


#! Snippet from speech_dataset/src/utils/file.py
def fget_list(file_path: Path | str) -> List[str]:
    return fread(file_path=Path(file_path)).split("\n")


def fread(file_path: Path | str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


def fwrite_text(
    content: str,
    file_path: Path | str,
    exist_ok: bool = True,
    unicode: bool = False,
    skip_newline: bool = False,
) -> None:
    file_path = Path(file_path)
    if unicode:
        content = get_unicode_string(content, skip_newline)
        file_path = file_path.parent / Path(file_path.stem + "_utf")
    fwrite(content=content, file_path=file_path.with_suffix(".txt"), exist_ok=exist_ok)


def fwrite_json(
    data: Dict,
    file_path: Path | str,
    unicode: bool = False,
) -> None:
    file_path = Path(file_path)
    if unicode:
        json_data = json.dumps(data)
        file_path = file_path.parent / Path(file_path.stem + "_utf")
    else:
        json_data = json.dumps(data, ensure_ascii=False)
    fwrite(content=json_data, file_path=file_path.with_suffix(".json"))


def fwrite_csv(data: Dict, fieldnames: Tuple, file_path: Path) -> None:
    file_path = Path(file_path)
    with open(
        file_path.with_suffix(".csv"), mode="w", encoding="utf-8", newline=""
    ) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for word_bn, word_mm in data.items():
            writer.writerow({fieldnames[0]: word_bn, fieldnames[1]: word_mm})


def fpath_unicode(file_path: Path) -> Path:
    file_name = file_path.stem + "_utf"
    return file_path.parent / file_name


def fwrite(content: str, file_path: Path | str, exist_ok: bool = True) -> None:
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=exist_ok)
    file_path.write_text(data=content, encoding="utf-8")


def change_path(file_path: Path, dir: Path, extension: str = "txt") -> Path:
    return dir / f"{file_path.stem}.{extension}"
