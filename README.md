# mm_transliteration 🚧

Break Build Morph Algorithm for Transliteration of Manipuri Bangla Script to Meetei/Meitei Mayek

🚧 This repository is currently under development!

## 1. Testing

1. Put file containing the bengali words in data directory
2. Run `main.py`

ntermediate output in data/tokens.txt

## 2. Use as Module

Clone `mm_transliteration.py` and `src` folder inside a folder of your choice, say `my_folder`.

Then, Import and create `MMTransliteration` class from `my_folder.mm_transliteration` and call `transliterate()` , `transliterate_script()` or `transliterate_utterances()`

```python
from my_folder.mm_transliteration import MMTransliteration

t = MMTransliteration()
output = t.transliterate("<your-input-here>")
```

or

You can create `__init__.py` inside `my_folder` and write

```python
# __init__.py
from .mm_transliteration import MMTransliteration

__all__ = ["MMTransliteration"]
```

Then you can import directly as

```python
from my_folder import MMTransliteration

t = MMTransliteration()

# 1. Transliterate string
output_1 = t.transliterate("<your-input-here>")

# 2. Transliterate script
output_2 = t.transliterate_script("<your-file-here>")

# 3. Transliterate utterances
output_3 = t.transliterate_utterances("<your-utterance-file-here>")
```

## See also

- [Speech Dataset](https://github.com/hoomexsun/speech_dataset).
- [Meetei/Meitei Mayek Transliteration](https://github.com/hoomexsun/mm_transliteration).
- [Meetei/Meitei Mayek Keyboard for Windows](https://github.com/hoomexsun/mm_keyboard).
- [IPA Keyboard for Windows](https://github.com/hoomexsun/ipa_keyboard).
- [S-550 Glyph Correction](https://github.com/hoomexsun/s550_glyph_correction).
- [Epaomayek Glyph Correction](https://github.com/hoomexsun/epaomayek_glyph_correction).
