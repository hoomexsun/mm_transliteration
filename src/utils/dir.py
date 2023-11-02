from pathlib import Path
from typing import Callable, Dict

import tqdm

from .file import change_path, fget_list, fwrite_text
from .text import utt_content_to_dict


#! Snippet from speech_dataset/src/utils/dir.py
OUTPUT_DIR = Path("data/outputs")


def process_directory(
    func: Callable,
    dir: Path,
    output_dir: Path | str = OUTPUT_DIR,
    desc: str = "Running...",
    return_dict: bool = False,
) -> Dict:
    output_dir = Path(output_dir)
    content_dict = {}
    files = fget_list(dir=dir, extension="txt")
    for file_path in tqdm(files, total=len(files), desc=desc):
        content = func(file_path=file_path)
        fwrite_text(
            content=content,
            file_path=change_path(file_path=file_path, dir=output_dir),
        )
        if return_dict:
            content_dict.update(utt_content_to_dict(content))
    return content_dict
