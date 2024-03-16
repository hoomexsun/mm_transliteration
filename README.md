# mm_transliteration 🚧

**SyPhell Algorithm** for transliteration of Manipuri Bengali Script to Meetei/Meitei Mayek.

## Status

🚧 This repository is currently under development!

## Quickstart

1. Clone this repository.

   ```sh
   git clone https://github.com/hoomexsun/mm_transliteration.git
   ```

2. Install python requirements. Please refer [requirements.txt](requirements.txt)
3. Now, run `main.py`.

## Custom Usage

After Step 1 & 2 from Quickstart.

1. Add your file.
2. Extract the string from the file and call either `mt.transliterate()` or `mt.transliterate_words()`.

   ```python
   # main.py
   from pathlib import Path
   from src.mt_ import MMTransliteration

   content = Path("<YOUR_FILE_PATH>").read_text(encoding="utf-8")
   gc = MMTransliteration()

   output_1 = mt.transliterate_words(content) # For huge text
   # or
   output_2 = mt.transliterate(content) # Simpler
   ```

3. Now, run `main.py`.

## Use in your repository (as submodule)

1. Add this repository as submodule

   ```bash
   git submodule add https://github.com/hoomexsun/mm_transliteration.git
   ```

2. Create a `MMTransliteration` object after importing and then use its functions.

   ```python
   from mm_transliteration import MMTransliteration
   gc = MMTransliteration()
   ...
   ```

## Evaluation (WER & CER)

🚧 Currently under development!

## GUI

Check out gui built using tkinter on [XLIT](https://github.com/hoomexsun/xlit).

## Algorithm 2 (Syllabification)

🚧 Currently under development!

## Algorithm 3 (Spell)

**Input:** List of phonemes, P or {p₀, p₁, …, pₙ₋₁}
**Output:** Meetei Mayek String, **S**

1. initialize **S** ← mm_begin[p₀]
2. assign flag ← True if p₀ is vowel else False
3. for each phoneme pᵢ from i ← 1 to n-1:
   - if pᵢ₋₁ and pᵢ are both consonants:
     append mm_char_apun to **S**
   - if flag is True:
     append mm_end[pᵢ] to **S**
   - else if pᵢ is consonant:
     append mm_begin[pᵢ] to **S**
   - else:
     flag ← True
4. Return the resulting string **S**

## See also

- [Glyph Correction](https://github.com/hoomexsun/glyph_correction).
- [Meetei/Meitei Mayek Transliteration](https://github.com/hoomexsun/mm_transliteration).
- [Meetei/Meitei Mayek Keyboard for Windows](https://github.com/hoomexsun/mm_keyboard).
- [Wahei Tool](https://https://github.com/hoomexsun/wahei).
