# mm_transliteration 🚧

Break Build Morph Algorithm for Transliteration of Manipuri Bangla Script to Meetei/Meitei Mayek

🚧 This repository is currently under development!

## 1. Testing

Run `main.py` and check `data/`

## 2. Testing with custom input

1. Put file containing the bengali words in data directory
2. Run `main.py`

Intermediate output in `data/tokens.txt`

## 3. Use as Module

Clone `src` folder in your `main_project/src` and rename it to your choice, say `mm_transliteration`.

Then, Import and create `MMTransliteration` class from `mm_transliteration` and call `transliterate()` , `transliterate_script()` or `transliterate_utterances()`

```python
# From a python file inside main_project/src
from mm_transliteration import MMTransliteration

mt = MMTransliteration()

# 1. Transliterate bengali string
output_1 = mt.transliterate("<your-input-here>")

# 2. Transliterate bengali script
output_2 = mt.transliterate_script("<your-file-here>")

# 3. Transliterate bengali utterances
output_3 = mt.transliterate_utterances("<your-utterance-file-here>")
```

## 4. Generating wordmap 🚧

You can generate wordmap of your word list as follows

1. Put your `words.txt` inside `data`.
2. From `main.py`, write a function referring to `generate_wordmap` function and `main` function.
3. Run it.

Writing Wordmap file in text format, json format and csv format are all included as utility functions.

Refer `src/utils/file.py`

## 5. Correcting files in bulk 🚧

Put all files inside a directory say `data/inputs/` and write as

```python
# From a python file inside main_project/src
from mm_transliteration import MMTransliteration
from src.utils.dir import process_directory

input_dir = "data/inputs"
mt = MMTransliteration()

# For normal files
process_directory(gc.transliterate_script, dir=input_dir)

# For utterance files
process_directory(gc.transliterate_utterances, dir=input_dir)
```

Output files will be inside `data/outputs`

## 6. Script mode 🚧

usage: script.py [-h] [-f | -d] input_string

Transliterates Bengali Unicode to Meetei Mayek Unicode using a rule-based method, supporting transliteration through a wordmap

positional arguments:
input_string Input string to transliterate

options:

1. -h, --help show this help message and exit
2. -f, --file Input is a file name
3. -d, --dir Input is a directory

## 7. Algorithm 🚧

The Break-Build-Morph algorithm

Part 1: Syllabification

$w = w_1w_2w_3 ... w_n$ .................... [Word] ($n$ characters)

$t = t_1t_2t_3 ... t_n$ .................... [Character Types] ($n$ characters)

$p = p_1p_2p_3 ... p_n$ .................... [Phonemes] ($n$ characters)

$m = m_1m_2m_3 ... m_n+1$ .................... [Markers] ($n+1$ characters)

Part 2: Conversion
Algorithm
Input: Syllabified bengali word
Output: Transliterated meetei mayek word

convert each character into the respective phonemes
Improve the phoneme conversion by searching for diphthongs and treat it as single phoneme
Split word into syllables using a boundary character
For each syllable
Find the nucleus
Assign everything before nucleus as onset if it exist and after nucleus as coda
If there is no onset, map nucleus using PHONEME_TO_MM_BEGIN and code using PHONEME_TO_MM_END
Else, map onset using PHONEME_TO_MM_BEGIN, nucleus and coda using PHONEME_TO_MM_END
Add apun, if there are multiple character in onset or coda between the characters
Add apun, if nucleus ends with character other than MM_CHEITAPS and coda is not empty. [EXPERIMENTAL]
Join onset, nucleus, coda and return

## See also

- [Speech Dataset](https://github.com/hoomexsun/speech_dataset).
- [Meetei/Meitei Mayek Transliteration](https://github.com/hoomexsun/mm_transliteration).
- [Meetei/Meitei Mayek Keyboard for Windows](https://github.com/hoomexsun/mm_keyboard).
- [IPA Keyboard for Windows](https://github.com/hoomexsun/ipa_keyboard).
- [S-550 Glyph Correction](https://github.com/hoomexsun/s550_glyph_correction).
- [Epaomayek Glyph Correction](https://github.com/hoomexsun/epaomayek_glyph_correction).
