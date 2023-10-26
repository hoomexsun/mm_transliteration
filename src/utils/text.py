import io
from typing import Dict, List


#! Snippet from speech_dataset/src/utils/text.py
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
