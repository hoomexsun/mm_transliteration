from enum import Enum
from typing import Dict, List, Set, Tuple


class PoA(Enum):
    """Place of Articulation Enum"""

    BILABIAL = "bilabial"
    ALVEOLAR = "alveolar"
    PALATAL = "palatal"
    VELAR = "velar"
    GLOTTAL = "glottal"


class MoA(Enum):
    """Manner of Articulation"""

    NASAL = "nasal"
    PLOSIVE = "plosive"
    FRICATIVE = "fricative"
    APPROXIMANT = "approximant"
    TAP_FLAP = "tap/flap"
    TRILL = "trill"
    LATERAL_FRICATIVE = "lateral fricative"
    LATERAL_APPROXIMANT = "lateral approximant"
    LATEAL_TAP_FLAP = "lateral tap/flap"


# 1. Phoneme Inventory
# 1.1. Meetei Mayek Phoneme
class MMPhoneme:
    """
    Class representing the phoneme inventory of Meetei Mayek.

    Attributes:
        ssp_sievers (Dict[int, str]): Sonority classes for SSP (Sievers 1876) based on relative loudness.
        ssp_parker (Dict[int, str]): Sonority classes for SSP (Parker 2002) based on acoustic intensity.
        to_ipa_map (Dict[str, str]): Mapping of phonemes to their IPA representations.
        to_phoneme_map (Dict[str, str]): Mapping of IPA symbols to phonemes.
        feats_consonant (Dict[str, Tuple[Tuple[int, int], Tuple[int, int, bool, bool]]]): Features for consonant phonemes.
        feats_vowels (Dict[str, Tuple[int, int, bool]]): Features for vowel phonemes.
    """

    def __init__(self) -> None:
        """Initialize the Meetei Mayek phoneme inventory."""
        self.ssp_sievers = {
            0: "phone_s",
            1: "obstruent",
            2: "nasal",
            3: "liquid",
            4: "glide",
        }
        self.ssp_parker = {
            0: "voiceless_stop/affricate/phone_?",
            1: "voiceless_fricative",
            2: "voiced_stop/affricate",
            3: "voiced_fricative",
            4: "phone_h",
            5: "nasal",
            6: "trill",
            7: "flap",
            8: "lateral",
            9: "rhotic",
            10: "glide",
        }
        self._define_phonemes()
        self.to_ipa_map, self.to_phoneme_map = self._generate_maps()
        self.feats_consonant, self.feats_vowels = self._generate_features()

    def _define_phonemes(self) -> None:
        """Define the 36 phonemes of Meetei Mayek."""
        # consonants
        self.phoneme_k: str = "K"
        self.phoneme_kh: str = "KH"
        self.phoneme_g: str = "G"
        self.phoneme_gh: str = "GH"
        self.phoneme_ng: str = "NG"
        self.phoneme_c: str = "C"
        self.phoneme_z: str = "Z"
        self.phoneme_zh: str = "ZH"
        self.phoneme_t: str = "T"
        self.phoneme_th: str = "TH"
        self.phoneme_d: str = "D"
        self.phoneme_dh: str = "DH"
        self.phoneme_n: str = "N"
        self.phoneme_p: str = "P"
        self.phoneme_ph: str = "PH"
        self.phoneme_b: str = "B"
        self.phoneme_bh: str = "BH"
        self.phoneme_m: str = "M"
        self.phoneme_j: str = "J"
        self.phoneme_r: str = "R"
        self.phoneme_w: str = "W"
        self.phoneme_l: str = "L"
        self.phoneme_s: str = "S"
        self.phoneme_h: str = "H"
        # vowels - monophthongs
        self.phoneme_i: str = "I"
        self.phoneme_e: str = "E"
        self.phoneme_a: str = "A"
        self.phoneme_x: str = "X"
        self.phoneme_u: str = "U"
        self.phoneme_o: str = "O"
        # vowel - diphthongs
        self.phoneme_ai: str = "AI"
        self.phoneme_xi: str = "XI"
        self.phoneme_ui: str = "UI"
        self.phoneme_oi: str = "OI"
        self.phoneme_au: str = "AU"
        self.phoneme_xu: str = "XU"

    def _generate_maps(self) -> Tuple[Dict[str, str], Dict[str, str]]:
        """Generate mappings for phonemes."""
        # phoneme: [list_of_ipas]
        corresponding_ipa_list: Dict[str, List[str]] = {
            self.phoneme_k: ["k"],
            self.phoneme_kh: ["kʰ"],
            self.phoneme_g: ["g"],
            self.phoneme_gh: ["gʰ"],
            self.phoneme_ng: ["ŋ"],
            self.phoneme_c: ["c", "tʃ"],
            self.phoneme_z: ["ɟ", "ʒ", "dʒ"],
            self.phoneme_zh: ["ɟʰ", "dʒʰ"],
            self.phoneme_t: ["t"],
            self.phoneme_th: ["tʰ", "θ"],
            self.phoneme_d: ["d"],
            self.phoneme_dh: ["dʰ", "ð"],
            self.phoneme_n: ["n"],
            self.phoneme_p: ["p"],
            self.phoneme_ph: ["pʰ", "f"],
            self.phoneme_b: ["b"],
            self.phoneme_bh: ["bʰ", "v"],
            self.phoneme_m: ["m"],
            self.phoneme_j: ["j"],
            self.phoneme_r: ["r"],
            self.phoneme_w: ["w"],
            self.phoneme_l: ["l"],
            self.phoneme_s: ["s", "ʃ"],
            self.phoneme_h: ["h"],
            # vowels - monophthongs
            self.phoneme_i: ["i"],
            self.phoneme_e: ["e", "æ", "ɛ"],
            self.phoneme_x: ["ɘ", "ʌ"],
            self.phoneme_u: ["u", "ʊ"],
            self.phoneme_o: ["o", "ɔ"],
            self.phoneme_a: ["a"],
            # vowel - diphthongs
            self.phoneme_ai: ["ai"],
            self.phoneme_xi: ["ɘi"],
            self.phoneme_ui: ["ui"],
            self.phoneme_oi: ["oi"],
            self.phoneme_au: ["au"],
            self.phoneme_xu: ["ɘu"],
        }
        # Phoneme -> IPA
        to_ipa_map = {
            phoneme: ipa_list[0] for phoneme, ipa_list in corresponding_ipa_list.items()
        }
        # IPA -> Phoneme
        to_phoneme_map = {
            ipa: phoneme
            for phoneme, ipa_list in corresponding_ipa_list.items()
            for ipa in ipa_list
        }
        return to_ipa_map, to_phoneme_map

    def _generate_features(
        self,
    ) -> Tuple[
        Dict[str, Tuple[Tuple[int, int], Tuple[int, int, bool, bool]]],
        Dict[str, Tuple[int, int, bool]],
    ]:
        """Generate features for phonemes."""
        # consonant_features
        # consonant_phoneme:(ssp_tuple, articulation_tuple)
        # ssp_tuple -> (siever_ssp_value, parker_ssp_value)
        # articulation_tuple -> (manner, place, voiced)
        consonant_features: Dict[str, Tuple[Tuple[int, int], Tuple[str, str, bool]]] = {
            self.phoneme_k: ((1, 0), (PoA.VELAR, MoA.PLOSIVE, False)),
            self.phoneme_kh: ((1, 0), (PoA.VELAR, MoA.PLOSIVE, False)),
            self.phoneme_g: ((1, 2), (PoA.VELAR, MoA.PLOSIVE, True)),
            self.phoneme_gh: ((1, 2), (PoA.VELAR, MoA.PLOSIVE, True)),
            self.phoneme_ng: ((2, 5), (PoA.VELAR, MoA.NASAL, True)),
            self.phoneme_c: ((1, 0), (PoA.PALATAL, MoA.PLOSIVE, False)),
            self.phoneme_z: ((1, 2), (PoA.PALATAL, MoA.PLOSIVE, True)),
            self.phoneme_zh: ((1, 2), (PoA.PALATAL, MoA.PLOSIVE, True)),
            self.phoneme_t: ((1, 0), (PoA.ALVEOLAR, MoA.PLOSIVE, False)),
            self.phoneme_th: ((1, 0), (PoA.ALVEOLAR, MoA.PLOSIVE, False)),
            self.phoneme_d: ((1, 2), (PoA.ALVEOLAR, MoA.PLOSIVE, True)),
            self.phoneme_dh: ((1, 2), (PoA.ALVEOLAR, MoA.PLOSIVE, True)),
            self.phoneme_n: ((2, 5), (PoA.ALVEOLAR, MoA.NASAL, True)),
            self.phoneme_p: ((1, 0), (PoA.BILABIAL, MoA.PLOSIVE, False)),
            self.phoneme_ph: ((1, 0), (PoA.BILABIAL, MoA.PLOSIVE, False)),
            self.phoneme_b: ((1, 2), (PoA.BILABIAL, MoA.PLOSIVE, True)),
            self.phoneme_bh: ((1, 2), (PoA.BILABIAL, MoA.PLOSIVE, True)),
            self.phoneme_m: ((2, 5), (PoA.BILABIAL, MoA.NASAL, True)),
            self.phoneme_j: ((4, 10), (PoA.PALATAL, MoA.APPROXIMANT, True)),
            self.phoneme_r: ((3, 9), (PoA.ALVEOLAR, MoA.APPROXIMANT, True)),
            self.phoneme_w: ((4, 10), (PoA.BILABIAL, MoA.APPROXIMANT, True)),
            self.phoneme_l: ((2, 8), (PoA.ALVEOLAR, MoA.LATERAL_APPROXIMANT, True)),
            self.phoneme_s: ((0, 1), (PoA.ALVEOLAR, MoA.FRICATIVE, False)),
            self.phoneme_h: ((1, 4), (PoA.GLOTTAL, MoA.FRICATIVE, False)),
        }
        # vowel_features -> (front-0/central-1/back-2, close-0/mid-1/open-2, is_rounded)
        vowel_features: Dict[str, Tuple[int, int, bool]] = {
            self.phoneme_i: (0, 0, False),
            self.phoneme_e: (0, 1, False),
            self.phoneme_x: (1, 1, False),
            self.phoneme_u: (2, 0, True),
            self.phoneme_o: (2, 1, True),
            self.phoneme_a: (2, 2, False),
        }
        return consonant_features, vowel_features

    def to_ipa(self, phoneme: str) -> str:
        """Convert phoneme to IPA."""
        return self.to_ipa_map.get(phoneme, phoneme)

    def to_phoneme(self, ipa: str) -> str:
        """Convert IPA to phoneme."""
        return self.to_phoneme_map.get(ipa, ipa)

    def _get_ssp(
        self, chars: str, tuple_element: int, ssp_map: Dict[int, str]
    ) -> Tuple[int, str]:
        """Helper method to get SSP value and name."""
        if chars in self.to_ipa_map or chars in self.to_phoneme_map:
            phoneme = self.to_phoneme_map.get(chars, chars)
            if phoneme not in self.feats_consonant:
                ssp_value = 5 if tuple_element == 0 else 11
                return ssp_value, "vowel"
            else:
                ssp_value = self.feats_consonant[phoneme][0][tuple_element]
                return ssp_value, ssp_map.get(ssp_value, "Unknown")
        else:
            return -1, "Error"

    def get_seivers(self, chars: str) -> Tuple[int, str]:
        """Get Sievers SSP value and name for a given character."""
        return self._get_ssp(chars, 0, self.ssp_sievers)

    def get_parker(self, chars: str) -> Tuple[int, str]:
        """Get Parker SSP value and name for a given character."""
        return self._get_ssp(chars, 1, self.ssp_parker)


# 1.2 ARPAbet Phoneme
class ARPABETPhoneme:
    """
    ARPABETPhoneme class represents the ARPABET phoneme system used for representing
    the pronunciation of words in American English. This class provides functionality
    to handle ARPABET phonemes with one or two-letter representations.

    Attributes:
        num_letters (int): The number of letters to use for representing ARPABET phonemes.
            It can be either 1 or 2. Default is 2.

    Methods:
        __init__(self, num_letters: int = 2) -> None:
            Initializes the ARPABETPhoneme instance with the specified number of letters
            for representing ARPABET phonemes.

        reload_version(self, num_letters):
            Reloads the ARPABET version with the specified number of letters.

        define_alphabet_1(self):
            Defines ARPABET phonemes using a single letter representation.

        define_alphabet_2(self):
            Defines ARPABET phonemes using a two-letter representation.
    """

    def __init__(self, num_letters: int = 2) -> None:
        """
        Initializes the ARPABETPhoneme instance with the specified number of letters
        for representing ARPABET phonemes.

        Args:
            num_letters (int): The number of letters to use for representing ARPABET phonemes.
                It can be either 1 or 2. Default is 2.
        """
        self.define_alphabet_1()
        self.reload_version(num_letters)

    def reload_version(self, num_letters: int) -> None:
        """
        Reloads the ARPABET version with the specified number of letters.

        Args:
            num_letters (int): The number of letters to use for representing ARPABET phonemes.
                It can be either 1 or 2.

        Raises:
            ValueError: If `num_letters` is neither 1 nor 2.
        """
        if num_letters == 1:
            self.define_alphabet_1()
        elif num_letters == 2:
            self.define_alphabet_2()
        else:
            raise ValueError("ARPABET has only 1 or 2 letter versions.")
        self.all_phonemes = {
            getattr(self, attribute)
            for attribute in dir(self)
            if attribute.startswith("phoneme_")
        }

    def define_alphabet_1(self) -> None:
        """
        Defines ARPABET phonemes using a single letter representation.
        """
        # vowels (19 nos)
        self.phoneme_AA = "a"
        self.phoneme_AE = "@"
        self.phoneme_AH = "A"
        self.phoneme_AO = "c"
        self.phoneme_AW = "W"
        self.phoneme_AX = "x"
        self.phoneme_AXR = ""
        self.phoneme_AY = "Y"
        self.phoneme_EH = "E"
        self.phoneme_ER = "R"
        self.phoneme_EY = "e"
        self.phoneme_IH = "I"
        self.phoneme_IX = "X"
        self.phoneme_IY = "i"
        self.phoneme_OW = "o"
        self.phoneme_OY = "O"
        self.phoneme_UH = "U"
        self.phoneme_UW = "u"
        self.phoneme_UX = ""
        # consonants (31 nos)
        self.phoneme_B = "b"
        self.phoneme_CH = "C"
        self.phoneme_D = "d"
        self.phoneme_DH = "D"
        self.phoneme_DX = "F"
        self.phoneme_EL = "L"
        self.phoneme_EM = "M"
        self.phoneme_EN = "N"
        self.phoneme_F = "f"
        self.phoneme_G = "g"
        self.phoneme_H = "h"
        self.phoneme_JH = "J"
        self.phoneme_K = "k"
        self.phoneme_L = "l"
        self.phoneme_M = "m"
        self.phoneme_N = "n"
        self.phoneme_NG = "G"
        self.phoneme_NX = ""
        self.phoneme_P = "p"
        self.phoneme_Q = "Q"
        self.phoneme_R = "r"
        self.phoneme_S = "s"
        self.phoneme_SH = "S"
        self.phoneme_T = "t"
        self.phoneme_TH = "T"
        self.phoneme_V = "v"
        self.phoneme_W = "w"
        self.phoneme_WH = "WH"
        self.phoneme_Y = "y"
        self.phoneme_Z = "z"
        self.phoneme_ZH = "Z"

    def define_alphabet_2(self) -> None:
        """Defines ARPABET phonemes using a two-letter representation."""
        attrs = dir(self)
        for attr in attrs:
            if attr.startswith("phoneme_"):
                content = attr.split("_", 1)[1]
                setattr(self, attr, content)


# 2. Language Alphabet Inventory
# 2.0. Alphabet Class
class Alphabet:
    """Base class for language alphabets."""

    def __init__(self) -> None:
        """Initialize alphabet."""
        self._define_alphabet()
        self._define_extras()
        self._define_ranges()
        self._define_sets()

    def _define_alphabet(self) -> None:
        """Initialize alphabet characters."""
        pass

    def _define_extras(self) -> None:
        """Initialize extra characters or combinations."""
        pass

    def _define_ranges(self) -> None:
        """Initialize character ranges."""
        pass

    def _define_sets(self) -> None:
        """Initialize character sets."""
        pass

    def has_char(self, char: str) -> bool:
        """Check if the character exists in the alphabet."""
        return self.check_in_range(self.alphabet_range, char)

    def has_digit(self, char: str) -> bool:
        """Check if the character is a digit."""
        return self.check_in_range(self.digits_range, char)

    def check_in_range(self, char_range: Tuple[str, str], char: str) -> bool:
        """Check if the character is within the specified range."""
        return char_range[0] <= char <= char_range[1]


# 2.1. Meetei Mayek Alphabet Class
class MeeteiMayek(Alphabet):
    """Class representing Meetei Mayek alphabet."""

    def __init__(self) -> None:
        """Initialize Meetei Mayek alphabet."""
        super().__init__()

    def _define_alphabet(self) -> None:
        """Initialize Meetei Mayek alphabet characters."""
        self.letter_kok: str = "\uabc0"  # \uabc0 -> ꯀ
        self.letter_sam: str = "\uabc1"  # \uabc1 -> ꯁ
        self.letter_lai: str = "\uabc2"  # \uabc2 -> ꯂ
        self.letter_mit: str = "\uabc3"  # \uabc3 -> ꯃ
        self.letter_pa: str = "\uabc4"  # \uabc4 -> ꯄ
        self.letter_na: str = "\uabc5"  # \uabc5 -> ꯅ
        self.letter_chil: str = "\uabc6"  # \uabc6 -> ꯆ
        self.letter_til: str = "\uabc7"  # \uabc7 -> ꯇ
        self.letter_khou: str = "\uabc8"  # \uabc8 -> ꯈ
        self.letter_ngou: str = "\uabc9"  # \uabc9 -> ꯉ
        self.letter_thou: str = "\uabca"  # \uabca -> ꯊ
        self.letter_wai: str = "\uabcb"  # \uabcb -> ꯋ
        self.letter_yang: str = "\uabcc"  # \uabcc -> ꯌ
        self.letter_huk: str = "\uabcd"  # \uabcd -> ꯍ
        self.letter_un: str = "\uabce"  # \uabce -> ꯎ
        self.letter_i: str = "\uabcf"  # \uabcf -> ꯏ
        self.letter_pham: str = "\uabd0"  # \uabd0 -> ꯐ
        self.letter_atiya: str = "\uabd1"  # \uabd1 -> ꯑ
        self.letter_gok: str = "\uabd2"  # \uabd2 -> ꯒ
        self.letter_jham: str = "\uabd3"  # \uabd3 -> ꯓ
        self.letter_rai: str = "\uabd4"  # \uabd4 -> ꯔ
        self.letter_ba: str = "\uabd5"  # \uabd5 -> ꯕ
        self.letter_jil: str = "\uabd6"  # \uabd6 -> ꯖ
        self.letter_dil: str = "\uabd7"  # \uabd7 -> ꯗ
        self.letter_ghou: str = "\uabd8"  # \uabd8 -> ꯘ
        self.letter_dhou: str = "\uabd9"  # \uabd9 -> ꯙ
        self.letter_bham: str = "\uabda"  # \uabda -> ꯚ
        self.letter_kok_lonsum: str = "\uabdb"  # \uabdb -> ꯛ
        self.letter_lai_lonsum: str = "\uabdc"  # \uabdc -> ꯜ
        self.letter_mit_lonsum: str = "\uabdd"  # \uabdd -> ꯝ
        self.letter_pa_lonsum: str = "\uabde"  # \uabde -> ꯞ
        self.letter_na_lonsum: str = "\uabdf"  # \uabdf -> ꯟ
        self.letter_til_lonsum: str = "\uabe0"  # \uabe0 -> ꯠ
        self.letter_ngou_lonsum: str = "\uabe1"  # \uabe1 -> ꯡ
        self.letter_i_lonsum: str = "\uabe2"  # \uabe2 -> ꯢ
        self.vowel_onap: str = "\uabe3"  # \uabe3 -> ꯣ
        self.vowel_inap: str = "\uabe4"  # \uabe4 -> ꯤ
        self.vowel_anap: str = "\uabe5"  # \uabe5 -> ꯥ
        self.vowel_yenap: str = "\uabe6"  # \uabe6 -> ꯦ
        self.vowel_sounap: str = "\uabe7"  # \uabe7 -> ꯧ
        self.vowel_unap: str = "\uabe8"  # \uabe8 -> ꯨ
        self.vowel_cheinap: str = "\uabe9"  # \uabe9 -> ꯩ
        self.vowel_nung: str = "\uabea"  # \uabea -> ꯪ
        self.cheikhei: str = "\uabeb"  # \uabeb -> ꯫
        self.lum_iyek: str = "\uabec"  # \uabec -> ꯬
        self.apun_iyek: str = "\uabed"  # \uabed -> ꯭
        self.digit_zero: str = "\uabf0"  # \uabf0 -> ꯰
        self.digit_one: str = "\uabf1"  # \uabf1 -> ꯱
        self.digit_two: str = "\uabf2"  # \uabf2 -> ꯲
        self.digit_three: str = "\uabf3"  # \uabf3 -> ꯳
        self.digit_four: str = "\uabf4"  # \uabf4 -> ꯴
        self.digit_five: str = "\uabf5"  # \uabf5 -> ꯵
        self.digit_six: str = "\uabf6"  # \uabf6 -> ꯶
        self.digit_seven: str = "\uabf7"  # \uabf7 -> ꯷
        self.digit_eight: str = "\uabf8"  # \uabf8 -> ꯸
        self.digit_nine: str = "\uabf9"  # \uabf9 -> ꯹)

    def _define_extras(self):
        """Initialize extra characters or combinations."""
        self.diphthong_ai: str = f"{self.vowel_anap}{self.letter_i_lonsum}"  # ꯥꯢ (AI)
        self.diphthong_xi: str = self.vowel_cheinap  # ꯩ (XI)
        self.diphthong_oi: str = f"{self.vowel_onap}{self.letter_i_lonsum}"  # ꯣꯢ (OI)
        self.diphthong_ui: str = f"{self.vowel_unap}{self.letter_i_lonsum}"  # ꯨꯢ (UI)
        self.diphthong_au: str = f"{self.vowel_anap}{self.letter_un}"  # ꯥꯎ (AU)
        self.diphthong_xu: str = self.vowel_sounap  # ꯧ (XU)

    def _define_ranges(self) -> None:
        """Initialize character ranges."""
        self.alphabet_range: Tuple[str, str] = (self.letter_kok, self.digit_nine)
        self.digits_range: Tuple[str, str] = (self.digit_zero, self.digit_nine)

    def _define_sets(self) -> None:
        """Initialize character sets."""
        # Vowels
        self.mapum_vowel_set: Set[str] = {
            self.letter_un,
            self.letter_i,
            self.letter_atiya,
        }
        self.cheitap_vowel_set: Set[str] = {
            chr(char)
            for char in range(ord(self.vowel_onap), ord(self.vowel_cheinap) + 1)
        }
        self.lonsum_vowel_set: Set[str] = {self.letter_i_lonsum}
        # Consonants
        self.mapum_consonant_set: Set[str] = {
            chr(char) for char in range(ord(self.letter_kok), ord(self.letter_huk) + 1)
        }.union(
            {self.letter_pham},
            {
                chr(char)
                for char in range(ord(self.letter_gok), ord(self.letter_bham) + 1)
            },
        )
        self.cheitap_consonant_set: Set[str] = {self.vowel_nung}
        self.lonsum_consonant_set: Set[str] = {
            chr(char)
            for char in range(
                ord(self.letter_kok_lonsum), ord(self.letter_ngou_lonsum) + 1
            )
        }
        # Main letters
        self.mapum_set: Set[str] = self.mapum_consonant_set.union(self.mapum_vowel_set)
        self.cheitap_set: Set[str] = self.cheitap_consonant_set.union(
            self.cheitap_vowel_set
        )
        self.lonsum_set: Set[str] = self.lonsum_consonant_set.union(
            self.lonsum_vowel_set
        )
        # Diphthongs
        self.dependent_diphthongs_set: Set[str] = {
            self.diphthong_ai,
            self.diphthong_xi,
            self.diphthong_oi,
            self.diphthong_ui,
            self.diphthong_au,
            self.diphthong_xu,
        }

        # Linguistic Sets (Syllabic)
        self.dependent_nucleus_set: Set[str] = self.cheitap_vowel_set.union(
            self.dependent_diphthongs_set
        )

        self.i2d_v_map = {
            chars: self.get_independent_diphthongs(chars)
            for chars in self.dependent_nucleus_set
        }
        self.d2i_v_map = {val: key for key, val in self.i2d_v_map.items()}

    def get_independent_diphthongs(self, chars: str):
        if chars == self.vowel_inap:
            return self.letter_i
        elif chars == self.vowel_unap:
            return self.letter_un
        elif chars == self.diphthong_au:
            return f"{self.letter_un}{self.letter_i_lonsum}"
        else:
            return f"{self.letter_atiya}{chars}"

    def to_independent_nuclues(self, substr: str):
        if substr not in self.dependent_nucleus_set:
            raise Exception("Invalid vowel/diphthong")

    def has_mapum(self, char: str) -> bool:
        char_range = (self.letter_kok, self.letter_bham)
        return self.check_in_range(char_range, char)

    def has_lonsum(self, char: str) -> bool:
        char_range = (self.letter_kok, self.letter_bham)
        return self.check_in_range(char_range, char)

    def has_cheitap(self, char: str) -> bool:
        char_range = (self.vowel_onap, self.vowel_nung)
        return self.check_in_range(char_range, char)

    def has_khudam(self, char: str) -> bool:
        char_range = (self.cheikhei, self.lum_iyek)
        return self.check_in_range(char_range, char)


# 2.2. Bengali Alphabet Class
class Bengali(Alphabet):
    """Class representing Bengali alphabet."""

    def __init__(self) -> None:
        """Initialize Bengali alphabet."""
        super().__init__()

    def _define_alphabet(self):
        """Initialize Bengali alphabet characters."""
        self.sign_candrabindu: str = "\u0981"  # \u0981 -> ঁ
        self.sign_anusvara: str = "\u0982"  # \u0982 -> ং
        self.sign_visarga: str = "\u0983"  # \u0983 -> ঃ
        self.letter_a: str = "\u0985"  # \u0985 -> অ
        self.letter_aa: str = "\u0986"  # \u0986 -> আ
        self.letter_i: str = "\u0987"  # \u0987 -> ই
        self.letter_ii: str = "\u0988"  # \u0988 -> ঈ
        self.letter_u: str = "\u0989"  # \u0989 -> উ
        self.letter_uu: str = "\u098a"  # \u098a -> ঊ
        self.letter_r_vocalic: str = "\u098b"  # \u098b -> ঋ
        self.letter_e: str = "\u098f"  # \u098f -> এ
        self.letter_ai: str = "\u0990"  # \u0990 -> ঐ
        self.letter_o: str = "\u0993"  # \u0993 -> ও
        self.letter_ao: str = "\u0994"  # \u0994 -> ঔ
        self.letter_ka: str = "\u0995"  # \u0995 -> ক
        self.letter_kha: str = "\u0996"  # \u0996 -> খ
        self.letter_ga: str = "\u0997"  # \u0997 -> গ
        self.letter_gha: str = "\u0998"  # \u0998 -> ঘ
        self.letter_nga: str = "\u0999"  # \u0999 -> ঙ
        self.letter_ca: str = "\u099a"  # \u099a -> চ
        self.letter_cha: str = "\u099b"  # \u099b -> ছ
        self.letter_ja: str = "\u099c"  # \u099c -> জ
        self.letter_jha: str = "\u099d"  # \u099d -> ঝ
        self.letter_nya: str = "\u099e"  # \u099e -> ঞ
        self.letter_tta: str = "\u099f"  # \u099f -> ট
        self.letter_ttha: str = "\u09a0"  # \u09a0 -> ঠ
        self.letter_dda: str = "\u09a1"  # \u09a1 -> ড
        self.letter_ddha: str = "\u09a2"  # \u09a2 -> ঢ
        self.letter_nna: str = "\u09a3"  # \u09a3 -> ণ
        self.letter_ta: str = "\u09a4"  # \u09a4 -> ত
        self.letter_tha: str = "\u09a5"  # \u09a5 -> থ
        self.letter_da: str = "\u09a6"  # \u09a6 -> দ
        self.letter_dha: str = "\u09a7"  # \u09a7 -> ধ
        self.letter_na: str = "\u09a8"  # \u09a8 -> ন
        self.letter_pa: str = "\u09aa"  # \u09aa -> প
        self.letter_pha: str = "\u09ab"  # \u09ab -> ফ
        self.letter_ba: str = "\u09ac"  # \u09ac -> ব
        self.letter_bha: str = "\u09ad"  # \u09ad -> ভ
        self.letter_ma: str = "\u09ae"  # \u09ae -> ম
        self.letter_ya: str = "\u09af"  # \u09af -> য
        self.letter_ra: str = "\u09b0"  # \u09b0 -> র
        self.letter_la: str = "\u09b2"  # \u09b2 -> ল
        self.letter_sha: str = "\u09b6"  # \u09b6 -> শ
        self.letter_ssa: str = "\u09b7"  # \u09b7 -> ষ
        self.letter_sa: str = "\u09b8"  # \u09b8 -> স
        self.letter_h: str = "\u09b9"  # \u09b9 -> হ
        self.vowel_aa: str = "\u09be"  # \u09be -> া
        self.vowel_i: str = "\u09bf"  # \u09bf -> ি
        self.vowel_ii: str = "\u09c0"  # \u09c0 -> ী
        self.vowel_u: str = "\u09c1"  # \u09c1 -> ু
        self.vowel_uu: str = "\u09c2"  # \u09c2 -> ূ
        self.vowel_r_vocalic: str = "\u09c3"  # \u09c3 -> ৃ
        self.vowel_e: str = "\u09c7"  # \u09c7 -> ে
        self.vowel_ai: str = "\u09c8"  # \u09c8 -> ৈ
        self.vowel_o: str = "\u09cb"  # \u09cb ->  ো
        self.vowel_au: str = "\u09cc"  # \u09cc ->  ৌ
        self.sign_virama: str = "\u09cd"  # \u09cd -> ্
        self.letter_khanda_ta: str = "\u09ce"  # \u09ce -> ৎ
        self.mark_au: str = "\u09d7"  # \u09d7 -> ৗ
        self.letter_rra: str = "\u09dc"  # \u09dc -> ড়
        self.letter_rha: str = "\u09dd"  # \u09dd -> ঢ়
        self.letter_yya: str = "\u09df"  # \u09df -> য়
        self.digit_zero: str = "\u09e6"  # \u09e6 -> ০
        self.digit_one: str = "\u09e7"  # \u09e7 -> ১
        self.digit_two: str = "\u09e8"  # \u09e8 -> ২
        self.digit_three: str = "\u09e9"  # \u09e9 -> ৩
        self.digit_four: str = "\u09ea"  # \u09ea -> ৪
        self.digit_five: str = "\u09eb"  # \u09eb -> ৫
        self.digit_six: str = "\u09ec"  # \u09ec -> ৬
        self.digit_seven: str = "\u09ed"  # \u09ed -> ৭
        self.digit_eight: str = "\u09ee"  # \u09ee -> ৮
        self.digit_nine: str = "\u09ef"  # \u09ef -> ৯
        self.letter_w: str = "\u09f1"  # \u09f1 -> ৱ

    def _define_extras(self):
        """Initialize extra characters or combinations."""
        # self.diphthong_ai: str = f"{self.vowel_anap}{self.letter_i_lonsum}"  # ꯥꯢ (AI)
        # self.diphthong_xi: str = self.vowel_cheinap  # ꯩ (XI)
        # self.diphthong_oi: str = f"{self.vowel_onap}{self.letter_i_lonsum}"  # ꯣꯢ (OI)
        # self.diphthong_ui: str = f"{self.vowel_unap}{self.letter_i_lonsum}"  # ꯨꯢ (UI)
        # self.diphthong_au: str = f"{self.vowel_anap}{self.letter_un}"  # ꯥꯎ (AU)
        # self.diphthong_xu: str = self.vowel_sounap  # ꯧ (XU)
        pass

    def _define_ranges(self) -> None:
        """Initialize character ranges."""
        self.alphabet_range = (self.sign_candrabindu, self.letter_w)
        self.digits_range = (self.digit_zero, self.digit_nine)

    def _define_sets(self) -> None:
        """Initialize character sets."""
        # Independent Vowels
        self.independent_vowel_set: Set[str] = {
            chr(char) for char in range(ord(self.letter_a), ord(self.letter_ao) + 1)
        }
        # Independent Consonants
        self.independent_consonant_set: Set[str] = {
            chr(char) for char in range(ord(self.letter_ka), ord(self.letter_h) + 1)
        }.union(
            {self.letter_rra, self.letter_rha, self.letter_yya, self.letter_w},
        )
        # Dependent Vowels
        self.dependent_vowel_set: Set[str] = {
            chr(char) for char in range(ord(self.vowel_aa), ord(self.vowel_au) + 1)
        }.difference({self.vowel_r_vocalic})
        # Dependent Consonants
        self.dependent_consonant_set: Set[str] = {
            self.vowel_r_vocalic,
            self.letter_khanda_ta,
            self.sign_anusvara,
        }
        # Vowel written left
        self.L_vowels: Set[str] = {self.vowel_i, self.vowel_e, self.vowel_ai}

        # Vowel written right
        self.R_vowels: Set[str] = {self.vowel_aa, self.vowel_ii}

        # Vowel written at bottom
        self.B_vowels: Set[str] = {self.vowel_u, self.vowel_uu}

        # Vowel written as enclosed
        self.E_vowels: Set[str] = {self.vowel_o, self.vowel_au}
