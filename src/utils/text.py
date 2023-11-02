import io
from typing import Dict, List, Tuple


#! Snippet from speech_dataset/src/utils/text.py
def remove_chars(content: str, chars: List[str]) -> str:
    for char in chars:
        content = content.replace(char, "")
    return content


def replace_chars(content: str, charmap: Dict[str, str]) -> str:
    for char, replacement in charmap.items():
        content = content.replace(char, replacement)
    return content


def fix_mistypes(content: str, chars: List[str], num_mistypes: int = 2) -> str:
    for char in chars:
        for num in range(num_mistypes + 1, 1, -1):
            content = content.replace(char * num, char)
    return content


#! Basic
def get_unicode_string(content: str, skip_newline: bool = False) -> str:
    ss = io.StringIO()
    for char in content:
        if char == "\n" and skip_newline:
            ss.write("\n")
        else:
            try:
                ss.write("\\u" + format(ord(char), "x").zfill(4))
            except UnicodeEncodeError:
                ss.write("\\x" + char.encode("utf-8").hex())
    return ss.getvalue()


def utt_dict_to_content(utterances_dict: Dict[str, str]) -> str:
    return "\n".join(f"{utt_id}\t{utt}" for utt_id, utt in utterances_dict.items())


def utt_content_to_dict(content: str) -> Dict[str, str]:
    if not content:
        return {}
    lines = content.split("\n")
    utt_ids, utterances = [], []
    for line in lines:
        utt_id, *utterance = line.split("\t")
        utt_ids.append(utt_id)
        utterances.extend(utterance)
    return utt_lists_to_dict(utt_ids, utterances)


def utt_lists_to_dict(utt_ids: List[str], utterances: List[str]) -> Dict[str, str]:
    return {utt_id: utt for utt_id, utt in zip(utt_ids, utterances)}


def looks_like_utt(content: str) -> bool:
    return True


def utt_lists_to_content(utt_ids: List[str], utterances: List[str]) -> str:
    return "".join(f"{utt_id}\t{utt}\n" for utt_id, utt in zip(utt_ids, utterances))


def utt_lists_to_dict(utt_ids: List[str], utterances: List[str]) -> Dict[str, str]:
    return {utt_id: utt for utt_id, utt in zip(utt_ids, utterances)}


def utt_dict_to_content(utterances_dict: Dict[str, str]) -> str:
    return "\n".join(f"{utt_id}\t{utt}" for utt_id, utt in utterances_dict.items())


def utt_content_to_dict(content: str) -> Dict[str, str]:
    if not content:
        return {}
    lines = content.split("\n")
    utt_ids, utterances = [], []
    for line in lines:
        utt_id, *utterance = line.split("\t")
        utt_ids.append(utt_id)
        utterances.extend(utterance)
    return utt_lists_to_dict(utt_ids, utterances)


def split_id_and_utt(content: str) -> Tuple[List, List]:
    lines = content.split("\n")
    utt_ids, utterances = [], []
    for line in lines:
        utt_id, *utterance = line.split("\t")
        utt_ids.append(utt_id)
        utterances.extend(utterance)
    return utt_ids, utterances
