from pathlib import Path
from typing import List

from src.utils.text import get_unicode_string


#! Snippet from speech_dataset/src/utils/file.py
def fget_list(file_path: Path | str) -> List[str]:
    return fread(file_path=Path(file_path)).split("\n")


def fread(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8")


def fwrite_text(
    content: str,
    file_path: Path,
    exist_ok: bool = True,
    unicode: bool = False,
    skip_newline: bool = False,
) -> None:
    if unicode:
        content = get_unicode_string(content, skip_newline)
        file_path = file_path.parent / Path(file_path.stem + "_utf")
    fwrite(content=content, file_path=file_path.with_suffix(".txt"), exist_ok=exist_ok)


def fpath_unicode(file_path: Path) -> Path:
    file_name = file_path.stem + "_utf"
    return file_path.parent / file_name


def fwrite(content: str, file_path: Path, exist_ok: bool = True) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=exist_ok)
    file_path.write_text(data=content, encoding="utf-8")
