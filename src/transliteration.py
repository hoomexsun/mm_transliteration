from pathlib import Path
from src.utils.file import fread
from src.utils.text import (
    utt_content_to_dict,
    utt_dict_to_content,
)


class MMTransliteration:
    def __init__(self) -> None:
        self.__init_vars()

    def __str__(self) -> str:
        return "Transliteration"

    # Initializations
    def __init_vars(self):
        self.virama = "\u09cd"

    # Public methods
    def transliterate_script(self, file_path: Path) -> str:
        return self.transliterate(fread(file_path=file_path))

    def transliterate_utterances(self, file_path: Path) -> str:
        utterances_dict = utt_content_to_dict(fread(file_path=file_path))
        return utt_dict_to_content(
            {utt_id: self.transliterate(utt) for utt_id, utt in utterances_dict.items()}
        )

    def transliterate(self, content: str) -> str:
        # Returns final data
        return content
