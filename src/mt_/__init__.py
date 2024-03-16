from typing import Dict, List, Set, Tuple

from tqdm import tqdm

from .e2b import E2B
from ..lon_ import Bengali

__all__ = ["MMTransliteration"]


class MMTransliteration:

    def transliterate_words(self, text: str) -> str:
        bn = Bengali()
        e2b = E2B()
        words = []
        for word in tqdm(text.split(), desc="Correcting Glyphs..."):
            words.append(self.transliterate(text=word, bn=bn, e2b=e2b))
        return "\n".join(words)

    def transliterate(self, text: str, bn: Bengali | None, e2b: E2B | None) -> str:
        if bn == None or e2b == None:
            bn = Bengali()
            e2b = E2B()

        self.virama = bn.sign_virama

        # Step 0: Adjusting s550 characters
        text = self.__adjust_glyph(text, charmap=e2b.premap)

        # Step 1: Mapping Bengali Alphabet
        text = self.__map_unicode(text, charmap=e2b.charmap)

        # Step 2: Fix suffix position of r and then mapping
        text = self.__fix_r_glyph(
            text, chars=e2b.s550_extra_chars, charmap=e2b.R_char_r
        )

        # Step 3: Fix prefix position of vowels and fix vowels
        text = self.__fix_vowels(
            text, chars=bn.L_vowels, enclosed_vowel_charmap=e2b.postmap_vowels
        )

        # Returns final content
        return text

    # Private methods
    def __adjust_glyph(self, text: str, charmap: Dict[str, str]) -> str:
        for key, value in charmap.items():
            text = text.replace(key, value)
        return text

    def __map_unicode(self, text: str, charmap: Dict[str, str]) -> str:
        # 1. Mapping to correct unicode values (in or of decreasing size of key length)
        sorted_keys = sorted(charmap.keys(), key=len, reverse=True)
        for key in sorted_keys:
            text = text.replace(key, charmap[key])
        # 2. Fix redundant virama
        num_mistypes: int = 2
        for num in range(num_mistypes + 1, 1, -1):
            text = text.replace(self.virama * num, self.virama)
        return text

    def __fix_r_glyph(self, text: str, chars: Set[str], charmap: Dict[str, str]) -> str:
        # 0. Remove extra chars
        for char in chars:
            text = text.replace(char, "")
        # 1. Fixing position of r glyph
        char_list = []
        for idx, char in enumerate(text):
            if char in charmap:
                start_idx = (
                    idx - 7
                    if idx > 6
                    else (idx - 5 if idx > 4 else (idx - 3 if idx > 2 else idx - 1))
                )
                substring, offset = self.__jump(text[start_idx : idx + 1][::-1])
                char_list = char_list[: idx - offset] + substring[::-1]
            else:
                char_list.append(char)
        # 2. Post mapping r
        text = "".join(char_list)
        for char, replacement in charmap.items():
            text = text.replace(char, replacement)

        # 3. Fix redundant virama
        num_mistypes: int = 2
        for num in range(num_mistypes + 1, 1, -1):
            text = text.replace(self.virama * num, self.virama)
        return text

    def __fix_vowels(
        self, text: str, chars: Set[str], enclosed_vowel_charmap: Dict[str, str]
    ) -> str:
        # 1. Fixing Left Vowels' position
        char_list = []
        skip_index = -1
        for idx, char in enumerate(text):
            if idx == skip_index:
                skip_index = -1
            elif char in chars:
                stop_idx = (
                    idx + 8
                    if idx <= len(text) - 7
                    else (idx + 6 if idx <= len(text) - 5 else idx + 4)
                )
                substring, offset = self.__jump(text[idx:stop_idx])
                char_list += substring
                skip_index = idx + offset
            elif idx > skip_index:
                char_list.append(char)

        text = "".join(char_list)
        # 2. Fixing enclosed vowels to correct unicode
        for char, replacement in enclosed_vowel_charmap.items():
            text = text.replace(char, replacement)
        return text

    def __jump(self, chars: str) -> Tuple[List[str], int]:
        char, *right = chars
        idx = 0
        while idx < len(right) - 1 and right[idx + 1] == self.virama:
            idx += 2
        if idx >= len(right):
            return list(chars), 1
        return (right[: idx + 1] + [char], idx + 1)
