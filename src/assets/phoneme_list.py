from typing import Dict, Set

# Phoneme List
# Consonants
PHONEME_K: str = "k"
PHONEME_KH: str = "kʰ"
PHONEME_G: str = "g"
PHONEME_GH: str = "gʰ"
PHONEME_NG: str = "ŋ"
PHONEME_C: str = "c"
PHONEME_Z: str = "ɟ"
PHONEME_ZH: str = "ɟʰ"
PHONEME_T: str = "t"
PHONEME_TH: str = "tʰ"
PHONEME_D: str = "d"
PHONEME_DH: str = "dʰ"
PHONEME_N: str = "n"
PHONEME_P: str = "p"
PHONEME_PH: str = "pʰ"
PHONEME_B: str = "b"
PHONEME_BH: str = "bʰ"
PHONEME_M: str = "m"
PHONEME_J: str = "j"
PHONEME_R: str = "r"
PHONEME_W: str = "w"
PHONEME_L: str = "l"
PHONEME_S: str = "s"
PHONEME_H: str = "h"
# Vowels - Monophthongs
PHONEME_I: str = "i"
PHONEME_E: str = "e"
PHONEME_A: str = "a"
PHONEME_X: str = "ɘ"
PHONEME_U: str = "u"
PHONEME_O: str = "o"
# Vowel - Diphthongs
PHONEME_AI: str = "ai"
PHONEME_XI: str = "ɘi"
PHONEME_UI: str = "ui"
PHONEME_OI: str = "oi"
PHONEME_AU: str = "au"
PHONEME_XU: str = "ɘu"

PHONEME_SET_MONOPHTHONGS: Set[str] = {
    PHONEME_I,
    PHONEME_E,
    PHONEME_A,
    PHONEME_X,
    PHONEME_U,
    PHONEME_O,
}

PHONEME_SET_DIPHTHONGS: Set[str] = {
    PHONEME_AI,
    PHONEME_XI,
    PHONEME_UI,
    PHONEME_OI,
    PHONEME_AU,
    PHONEME_XU,
}

PHONEME_VOWELS: Set[str] = PHONEME_SET_MONOPHTHONGS.union(PHONEME_SET_DIPHTHONGS)

# Phoneme To_Diphthong
PHONEME_DIPHTHONGS_COMBINATION: Dict[str, str] = {
    f"{PHONEME_A}{PHONEME_I}": PHONEME_AI,
    f"{PHONEME_U}{PHONEME_I}": PHONEME_UI,
    f"{PHONEME_O}{PHONEME_I}": PHONEME_OI,
    f"{PHONEME_A}{PHONEME_U}": PHONEME_AU,
    # Extra
    f"{PHONEME_A}{PHONEME_O}": PHONEME_AU,
    # With Semi-vowels
    f"{PHONEME_A}{PHONEME_J}": PHONEME_AI,
    f"{PHONEME_U}{PHONEME_J}": PHONEME_UI,
    f"{PHONEME_O}{PHONEME_J}": PHONEME_OI,
}


# Place of Articulation Set -> POA_SET
POA_SET_BILABIAL: Set[str] = {
    PHONEME_P,
    PHONEME_PH,
    PHONEME_B,
    PHONEME_BH,
    PHONEME_M,
    PHONEME_W,
}
POA_SET_ALVEOLAR: Set[str] = {
    PHONEME_T,
    PHONEME_TH,
    PHONEME_D,
    PHONEME_DH,
    PHONEME_N,
    PHONEME_R,
    PHONEME_L,
}
POA_SET_PALATAL: Set[str] = {
    PHONEME_C,
    PHONEME_Z,
    PHONEME_ZH,
    PHONEME_S,
    PHONEME_J,
}
POA_SET_VELAR: Set[str] = {
    PHONEME_K,
    PHONEME_KH,
    PHONEME_G,
    PHONEME_GH,
    PHONEME_NG,
}
POA_SET_GLOTTAL: Set[str] = {
    PHONEME_H,
}
# Manner of Articulation Set -> MOA_SET
MOA_SET_PLOSIVE_UNASPIRATED: Set[str] = {
    PHONEME_P,
    PHONEME_B,
    PHONEME_T,
    PHONEME_D,
    PHONEME_C,
    PHONEME_Z,
    PHONEME_K,
    PHONEME_G,
}
MOA_SET_PLOSIVE_ASPIRATED: Set[str] = {
    PHONEME_PH,
    PHONEME_BH,
    PHONEME_TH,
    PHONEME_DH,
    PHONEME_ZH,
    PHONEME_KH,
    PHONEME_GH,
}
MOA_SET_NASALS: Set[str] = {
    PHONEME_M,
    PHONEME_N,
    PHONEME_NG,
}
MOA_SET_FRICATIVE: Set[str] = {
    PHONEME_S,
    PHONEME_H,
}
MOA_SET_APPROXIMANT: Set[str] = {
    PHONEME_W,
    PHONEME_R,
    PHONEME_J,
}
MOA_SET_LATERAL_APPROXIMANT: Set[str] = {
    PHONEME_L,
}
# Voiced Set -> VCD_SET
VCD_SET: Set[str] = {
    PHONEME_B,
    PHONEME_BH,
    PHONEME_M,
    PHONEME_W,
    PHONEME_D,
    PHONEME_DH,
    PHONEME_N,
    PHONEME_R,
    PHONEME_L,
    PHONEME_Z,
    PHONEME_ZH,
    PHONEME_J,
    PHONEME_G,
    PHONEME_GH,
    PHONEME_NG,
}
# Voicedless Set -> VCL_SET
VCL_SET: Set[str] = {
    PHONEME_P,
    PHONEME_PH,
    PHONEME_T,
    PHONEME_TH,
    PHONEME_C,
    PHONEME_S,
    PHONEME_K,
    PHONEME_KH,
    PHONEME_H,
}

# Sonority Classes for SSP (Sievers 1876) - Based on Relative loudness
# Vowels(5) > Glides(4) > Liquids(3) > Nasals(2) > Obstruents(1) > s (extra - 0)
SIEVERS_VOWEL: Set[str] = {
    PHONEME_I,
    PHONEME_E,
    PHONEME_A,
    PHONEME_X,
    PHONEME_U,
    PHONEME_O,
    PHONEME_AI,
    PHONEME_XI,
    PHONEME_UI,
    PHONEME_OI,
    PHONEME_AU,
    PHONEME_XU,
}
SIEVERS_GLIDE: Set[str] = {
    PHONEME_J,
    PHONEME_W,
}
SIEVERS_LIQUID: Set[str] = {
    PHONEME_R,
    PHONEME_L,
}
SIEVERS_NASAL: Set[str] = {
    PHONEME_M,
    PHONEME_N,
    PHONEME_NG,
}
SIEVERS_FRICATIVE: Set[str] = {
    PHONEME_H,
}
SIEVERS_PLOSIVE: Set[str] = {
    PHONEME_P,
    PHONEME_B,
    PHONEME_T,
    PHONEME_D,
    PHONEME_C,
    PHONEME_Z,
    PHONEME_K,
    PHONEME_G,
    PHONEME_PH,
    PHONEME_BH,
    PHONEME_TH,
    PHONEME_DH,
    PHONEME_ZH,
    PHONEME_KH,
    PHONEME_GH,
}
SIEVERS_CLICK: Set[str] = {}
SIEVERS_OBSTRUENT: Set[str] = SIEVERS_FRICATIVE.union(
    SIEVERS_PLOSIVE,
    SIEVERS_CLICK,
)
SIEVERS_S: Set[str] = {
    PHONEME_S,
}

# Sonority Classes for SSP (Parker 2002) - Based on acoustic intensity
# Glide > Rhotic > Lateral > Flap > Trill > Nasal > H > Voiced fricative >
# Voiced stop/affricate > Voiceless fricative > Voiceless stop/affricate/?
PARKER_GLIDE: Set[str] = {
    PHONEME_J,
    PHONEME_W,
}
PARKER_RHOTIC: Set[str] = {
    PHONEME_R,
}
PARKER_LATERAL: Set[str] = {
    PHONEME_L,
}
PARKER_FLAP: Set[str] = {}
PARKER_TRILL: Set[str] = {}
PARKER_NASAL: Set[str] = {
    PHONEME_M,
    PHONEME_N,
    PHONEME_NG,
}
PARKER_H: Set[str] = {
    PHONEME_H,
}
PARKER_VOICED_FRICATIVE: Set[str] = {}
PARKER_VOICED_STOP: Set[str] = {
    PHONEME_P,
    PHONEME_BH,
    PHONEME_D,
    PHONEME_DH,
    PHONEME_Z,
    PHONEME_ZH,
    PHONEME_G,
    PHONEME_GH,
}
PARKER_VOICED_AFFRICATE: Set[str] = {}
PARKER_VOICELESS_FRICATIVE: Set[str] = {
    PHONEME_S,
}
PARKER_VOICELESS_STOP: Set[str] = {
    PHONEME_P,
    PHONEME_PH,
    PHONEME_T,
    PHONEME_TH,
    PHONEME_C,
    PHONEME_K,
    PHONEME_KH,
}
PARKER_VOICELESS_AFFRICATE: Set[str] = {}

# ʰ Aspirated <- diacritic
# ◌̃ Nasalised

PHONEME_LIST = {}
# Other Phonemes

# Phoneme Adjustment

# BN characters
BN_SIGN_CANDRABINDU = "\u0981"  # \u0981 -> ঁ
BN_SIGN_ANUSVARA = "\u0982"  # \u0982 -> ং
BN_SIGN_VISARGA = "\u0983"  # \u0983 -> ঃ
# Letters
BN_LETTER_A: str = "\u0985"  # \u0985 -> অ
BN_LETTER_AA: str = "\u0986"  # \u0986 -> আ
BN_LETTER_I: str = "\u0987"  # \u0987 -> ই
BN_LETTER_II: str = "\u0988"  # \u0988 -> ঈ
BN_LETTER_U: str = "\u0989"  # \u0989 -> উ
BN_LETTER_UU: str = "\u098a"  # \u098a -> ঊ
BN_LETTER_R_VOCALIC: str = "\u098b"  # \u098b -> ঋ
BN_LETTER_E: str = "\u098f"  # \u098f -> এ
BN_LETTER_AI: str = "\u0990"  # \u0990 -> ঐ
BN_LETTER_O: str = "\u0993"  # \u0993 -> ও
BN_LETTER_AO: str = "\u0994"  # \u0994 -> ঔ
BN_LETTER_KA: str = "\u0995"  # \u0995 -> ক
BN_LETTER_KHA: str = "\u0996"  # \u0996 -> খ
BN_LETTER_GA: str = "\u0997"  # \u0997 -> গ
BN_LETTER_GHA: str = "\u0998"  # \u0998 -> ঘ
BN_LETTER_NGA: str = "\u0999"  # \u0999 -> ঙ
BN_LETTER_CA: str = "\u099a"  # \u099a -> চ
BN_LETTER_CHA: str = "\u099b"  # \u099b -> ছ
BN_LETTER_JA: str = "\u099c"  # \u099c -> জ
BN_LETTER_JHA: str = "\u099d"  # \u099d -> ঝ
BN_LETTER_NYA: str = "\u099e"  # \u099e -> ঞ
BN_LETTER_TTA: str = "\u099f"  # \u099f -> ট
BN_LETTER_TTHA: str = "\u09a0"  # \u09a0 -> ঠ
BN_LETTER_DDA: str = "\u09a1"  # \u09a1 -> ড
BN_LETTER_DDHA: str = "\u09a2"  # \u09a2 -> ঢ
BN_LETTER_NNA: str = "\u09a3"  # \u09a3 -> ণ
BN_LETTER_TA: str = "\u09a4"  # \u09a4 -> ত
BN_LETTER_THA: str = "\u09a5"  # \u09a5 -> থ
BN_LETTER_DA: str = "\u09a6"  # \u09a6 -> দ
BN_LETTER_DHA: str = "\u09a7"  # \u09a7 -> ধ
BN_LETTER_NA: str = "\u09a8"  # \u09a8 -> ন
BN_LETTER_PA: str = "\u09aa"  # \u09aa -> প
BN_LETTER_PHA: str = "\u09ab"  # \u09ab -> ফ
BN_LETTER_BA: str = "\u09ac"  # \u09ac -> ব
BN_LETTER_BHA: str = "\u09ad"  # \u09ad -> ভ
BN_LETTER_MA: str = "\u09ae"  # \u09ae -> ম
BN_LETTER_YA: str = "\u09af"  # \u09af -> য
BN_LETTER_RA: str = "\u09b0"  # \u09b0 -> র
BN_LETTER_LA: str = "\u09b2"  # \u09b2 -> ল
BN_LETTER_SHA: str = "\u09b6"  # \u09b6 -> শ
BN_LETTER_SSA: str = "\u09b7"  # \u09b7 -> ষ
BN_LETTER_SA: str = "\u09b8"  # \u09b8 -> স
BN_LETTER_H: str = "\u09b9"  # \u09b9 -> হ
# Vowel signs
BN_VOWEL_AA: str = "\u09be"  # \u09be -> া
BN_VOWEL_I: str = "\u09bf"  # \u09bf -> ি
BN_VOWEL_II: str = "\u09c0"  # \u09c0 -> ী
BN_VOWEL_U: str = "\u09c1"  # \u09c1 -> ু
BN_VOWEL_UU: str = "\u09c2"  # \u09c2 -> ূ
BN_VOWEL_R_VOCALIC: str = "\u09c3"  # \u09c3 -> ৃ
BN_VOWEL_E: str = "\u09c7"  # \u09c7 -> ে
BN_VOWEL_AI: str = "\u09c8"  # \u09c8 -> ৈ
BN_VOWEL_O: str = "\u09cb"  # \u09cb ->  ো
BN_VOWEL_AU: str = "\u09cc"  # \u09cc ->  ৌ
# Signs
BN_SIGN_VIRAMA: str = "\u09cd"  # \u09cd -> ্
BN_LETTER_KHANDA_TA: str = "\u09ce"  # \u09ce -> ৎ
MARK_AU: str = "\u09d7"  # \u09d7 -> ৗ
# Letters
BN_LETTER_RRA: str = "\u09dc"  # \u09dc -> ড়
BN_LETTER_RHA: str = "\u09dd"  # \u09dd -> ঢ়
BN_LETTER_YYA: str = "\u09df"  # \u09df -> য়
# Digits
BN_DIGIT_ZERO: str = "\u09e6"  # \u09e6 -> ০
BN_DIGIT_ONE: str = "\u09e7"  # \u09e7 -> ১
BN_DIGIT_TWO: str = "\u09e8"  # \u09e8 -> ২
BN_DIGIT_THREE: str = "\u09e9"  # \u09e9 -> ৩
BN_DIGIT_FOUR: str = "\u09ea"  # \u09ea -> ৪
BN_DIGIT_FIVE: str = "\u09eb"  # \u09eb -> ৫
BN_DIGIT_SIX: str = "\u09ec"  # \u09ec -> ৬
BN_DIGIT_SEVEN: str = "\u09ed"  # \u09ed -> ৭
BN_DIGIT_EIGHT: str = "\u09ee"  # \u09ee -> ৮
BN_DIGIT_NINE: str = "\u09ef"  # \u09ef -> ৯
# Originally Bengali Letter Ra with Lower Diagonal
BN_LETTER_W: str = "\u09F1"  # \u09f1 -> ৱ

BN_INDEPENDENT_CONSONANT: Set[str] = {
    BN_LETTER_R_VOCALIC,
    BN_LETTER_KA,
    BN_LETTER_KHA,
    BN_LETTER_GA,
    BN_LETTER_GHA,
    BN_LETTER_NGA,
    BN_LETTER_CA,
    BN_LETTER_CHA,
    BN_LETTER_JA,
    BN_LETTER_JHA,
    BN_LETTER_NYA,
    BN_LETTER_TTA,
    BN_LETTER_TTHA,
    BN_LETTER_DDA,
    BN_LETTER_DDHA,
    BN_LETTER_NNA,
    BN_LETTER_TA,
    BN_LETTER_THA,
    BN_LETTER_DA,
    BN_LETTER_DHA,
    BN_LETTER_NA,
    BN_LETTER_PA,
    BN_LETTER_PHA,
    BN_LETTER_BA,
    BN_LETTER_BHA,
    BN_LETTER_MA,
    BN_LETTER_YA,
    BN_LETTER_RA,
    BN_LETTER_LA,
    BN_LETTER_SHA,
    BN_LETTER_SSA,
    BN_LETTER_SA,
    BN_LETTER_H,
    BN_LETTER_RRA,
    BN_LETTER_RHA,
    BN_LETTER_YYA,
    BN_LETTER_W,
}

BN_DEPENDENT_CONSONANT: Set[str] = {
    BN_VOWEL_R_VOCALIC,
    BN_LETTER_KHANDA_TA,
    BN_SIGN_ANUSVARA,
}

BN_INDEPENDENT_VOWEL: Set[str] = {
    BN_LETTER_A,
    BN_LETTER_AA,
    BN_LETTER_I,
    BN_LETTER_II,
    BN_LETTER_U,
    BN_LETTER_UU,
    BN_LETTER_E,
    BN_LETTER_AI,
    BN_LETTER_O,
    BN_LETTER_AO,
}

BN_DEPENDENT_VOWEL: Set[str] = {
    BN_VOWEL_AA,
    BN_VOWEL_I,
    BN_VOWEL_II,
    BN_VOWEL_U,
    BN_VOWEL_UU,
    BN_VOWEL_E,
    BN_VOWEL_AI,
    BN_VOWEL_O,
    BN_VOWEL_AU,
}

BN_PUNCTUATION: Set[str] = {
    BN_SIGN_VISARGA,
}

BN_NUMERAL: Set[str] = {
    BN_DIGIT_ZERO,
    BN_DIGIT_ONE,
    BN_DIGIT_TWO,
    BN_DIGIT_THREE,
    BN_DIGIT_FOUR,
    BN_DIGIT_FIVE,
    BN_DIGIT_SIX,
    BN_DIGIT_SEVEN,
    BN_DIGIT_EIGHT,
    BN_DIGIT_NINE,
}

# Bengali disohthongs
BN_DIPHTHONG_AI: Set[str] = {
    BN_VOWEL_AA + BN_LETTER_I,  # \u09be\u0987 -> াই
    BN_VOWEL_AA + BN_LETTER_YA,  # \u09be\u09af -> ায
    BN_VOWEL_AA + BN_LETTER_YYA,  # \u09be\u09df -> ায়
}
BN_DIPHTHONG_OI: Set[str] = {
    BN_VOWEL_O + BN_LETTER_I,  # \u09cb\u0987 ->  োই
    BN_VOWEL_O + BN_LETTER_YA,  # \u09cb\u09af ->  োয
    BN_VOWEL_O + BN_LETTER_YYA,  # \u09cb\u09df ->  োয়
}
BN_DIPHTHONG_UI: Set[str] = {
    BN_VOWEL_U + BN_LETTER_I,  # \u09c1\u0987 -> ুই
    BN_VOWEL_U + BN_LETTER_YA,  # \u09c1\u09af -> ুয
    BN_VOWEL_U + BN_LETTER_YYA,  # \u09c1\u09df -> ুয়
    BN_VOWEL_UU + BN_LETTER_I,  # \u09c2\u0987 -> ূই
    BN_VOWEL_UU + BN_LETTER_YA,  # \u09c2\u09af -> ূয
    BN_VOWEL_UU + BN_LETTER_YYA,  # \u09c2\u09df -> ূয়
}
BN_DIPHTHONG_AO: Set[str] = {
    BN_VOWEL_AA + BN_LETTER_U,  # \u09be\u0989 -> াউ
    BN_VOWEL_AA + BN_LETTER_UU,  # \u09be\u098a -> াঊ
    BN_VOWEL_AA + BN_LETTER_O,  # \u09be\u0993 -> াও
}
BN_DEPENDENT_DIPHTHONGS: Set[str] = BN_DIPHTHONG_AI.union(
    BN_DIPHTHONG_OI,
    BN_DIPHTHONG_UI,
    BN_DIPHTHONG_AO,
)


# MM Characters
MM_LETTER_KOK: str = "\uabc0"  # \uabc0 -> ꯀ
MM_LETTER_SAM: str = "\uabc1"  # \uabc1 -> ꯁ
MM_LETTER_LAI: str = "\uabc2"  # \uabc2 -> ꯂ
MM_LETTER_MIT: str = "\uabc3"  # \uabc3 -> ꯃ
MM_LETTER_PA: str = "\uabc4"  # \uabc4 -> ꯄ
MM_LETTER_NA: str = "\uabc5"  # \uabc5 -> ꯅ
MM_LETTER_CHIL: str = "\uabc6"  # \uabc6 -> ꯆ
MM_LETTER_TIL: str = "\uabc7"  # \uabc7 -> ꯇ
MM_LETTER_KHOU: str = "\uabc8"  # \uabc8 -> ꯈ
MM_LETTER_NGOU: str = "\uabc9"  # \uabc9 -> ꯉ
MM_LETTER_THOU: str = "\uabca"  # \uabca -> ꯊ
MM_LETTER_WAI: str = "\uabcb"  # \uabcb -> ꯋ
MM_LETTER_YANG: str = "\uabcc"  # \uabcc -> ꯌ
MM_LETTER_HUK: str = "\uabcd"  # \uabcd -> ꯍ
MM_LETTER_UN: str = "\uabce"  # \uabce -> ꯎ
MM_LETTER_I: str = "\uabcf"  # \uabcf -> ꯏ
MM_LETTER_PHAM: str = "\uabd0"  # \uabd0 -> ꯐ
MM_LETTER_ATIYA: str = "\uabd1"  # \uabd1 -> ꯑ
MM_LETTER_GOK: str = "\uabd2"  # \uabd2 -> ꯒ
MM_LETTER_JHAM: str = "\uabd3"  # \uabd3 -> ꯓ
MM_LETTER_RAI: str = "\uabd4"  # \uabd4 -> ꯔ
MM_LETTER_BA: str = "\uabd5"  # \uabd5 -> ꯕ
MM_LETTER_JIL: str = "\uabd6"  # \uabd6 -> ꯖ
MM_LETTER_DIL: str = "\uabd7"  # \uabd7 -> ꯗ
MM_LETTER_GHOU: str = "\uabd8"  # \uabd8 -> ꯘ
MM_LETTER_DHOU: str = "\uabd9"  # \uabd9 -> ꯙ
MM_LETTER_BHAM: str = "\uabda"  # \uabda -> ꯚ
# Lonsum
MM_LETTER_KOK_LONSUM: str = "\uabdb"  # \uabdb -> ꯛ
MM_LETTER_LAI_LONSUM: str = "\uabdc"  # \uabdc -> ꯜ
MM_LETTER_MIT_LONSUM: str = "\uabdd"  # \uabdd -> ꯝ
MM_LETTER_PA_LONSUM: str = "\uabde"  # \uabde -> ꯞ
MM_LETTER_NA_LONSUM: str = "\uabdf"  # \uabdf -> ꯟ
MM_LETTER_TIL_LONSUM: str = "\uabe0"  # \uabe0 -> ꯠ
MM_LETTER_NGOU_LONSUM: str = "\uabe1"  # \uabe1 -> ꯡ
MM_LETTER_I_LONSUM: str = "\uabe2"  # \uabe2 -> ꯢ
# Cheitap
MM_VOWEL_ONAP: str = "\uabe3"  # \uabe3 -> ꯣ
MM_VOWEL_INAP: str = "\uabe4"  # \uabe4 -> ꯤ
MM_VOWEL_ANAP: str = "\uabe5"  # \uabe5 -> ꯥ
MM_VOWEL_YENAP: str = "\uabe6"  # \uabe6 -> ꯦ
MM_VOWEL_SOUNAP: str = "\uabe7"  # \uabe7 -> ꯧ
MM_VOWEL_UNAP: str = "\uabe8"  # \uabe8 -> ꯨ
MM_VOWEL_CHEINAP: str = "\uabe9"  # \uabe9 -> ꯩ
MM_VOWEL_NUNG: str = "\uabea"  # \uabea -> ꯪ

MM_MAPUM_CONSONANT: Set[str] = {
    MM_LETTER_KOK,
    MM_LETTER_SAM,
    MM_LETTER_LAI,
    MM_LETTER_MIT,
    MM_LETTER_PA,
    MM_LETTER_NA,
    MM_LETTER_CHIL,
    MM_LETTER_TIL,
    MM_LETTER_KHOU,
    MM_LETTER_NGOU,
    MM_LETTER_THOU,
    MM_LETTER_WAI,
    MM_LETTER_YANG,
    MM_LETTER_HUK,
    MM_LETTER_PHAM,
    MM_LETTER_GOK,
    MM_LETTER_JHAM,
    MM_LETTER_RAI,
    MM_LETTER_BA,
    MM_LETTER_JIL,
    MM_LETTER_DIL,
    MM_LETTER_GHOU,
    MM_LETTER_DHOU,
    MM_LETTER_BHAM,
}

MM_MAPUM_VOWEL: Set[str] = {
    MM_LETTER_UN,
    MM_LETTER_I,
    MM_LETTER_ATIYA,
}

MM_MAPUM = MM_MAPUM_CONSONANT.union(MM_MAPUM_VOWEL)

MM_LONSUM_CONSONANT: Set[str] = {
    MM_LETTER_KOK_LONSUM,
    MM_LETTER_LAI_LONSUM,
    MM_LETTER_MIT_LONSUM,
    MM_LETTER_PA_LONSUM,
    MM_LETTER_NA_LONSUM,
    MM_LETTER_TIL_LONSUM,
    MM_LETTER_NGOU_LONSUM,
}

MM_LONSUM_VOWEL: Set[str] = {
    MM_LETTER_I_LONSUM,
}

MM_LONSUM = MM_LONSUM_CONSONANT.union(MM_LONSUM_VOWEL)

MM_CHEITAP_CONSONANT: Set[str] = {
    MM_VOWEL_NUNG,
}

MM_CHEITAP_VOWEL: Set[str] = {
    MM_VOWEL_ONAP,
    MM_VOWEL_INAP,
    MM_VOWEL_ANAP,
    MM_VOWEL_YENAP,
    MM_VOWEL_SOUNAP,
    MM_VOWEL_UNAP,
    MM_VOWEL_CHEINAP,
}

MM_CHEITAP = MM_CHEITAP_CONSONANT.union(MM_CHEITAP_VOWEL)
# Khudam / Punctuations
MM_CHEIKHEI: str = "\uabeb"  # \uabeb -> ꯫
MM_LUM_IYEK: str = "\uabec"  # \uabec -> ꯬
MM_APUN_IYEK: str = "\uabed"  # \uabed -> ꯭
# Cheising / Digits
MM_DIGIT_ZERO: str = "\uabf0"  # \uabf0 -> ꯰
MM_DIGIT_ONE: str = "\uabf1"  # \uabf1 -> ꯱
MM_DIGIT_TWO: str = "\uabf2"  # \uabf2 -> ꯲
MM_DIGIT_THREE: str = "\uabf3"  # \uabf3 -> ꯳
MM_DIGIT_FOUR: str = "\uabf4"  # \uabf4 -> ꯴
MM_DIGIT_FIVE: str = "\uabf5"  # \uabf5 -> ꯵
MM_DIGIT_SIX: str = "\uabf6"  # \uabf6 -> ꯶
MM_DIGIT_SEVEN: str = "\uabf7"  # \uabf7 -> ꯷
MM_DIGIT_EIGHT: str = "\uabf8"  # \uabf8 -> ꯸
MM_DIGIT_NINE: str = "\uabf9"  # \uabf9 -> ꯹

# BN -> PHONEME
BN_TO_PHONEME: Dict[str, str] = {
    BN_SIGN_ANUSVARA: PHONEME_NG,  # ং ->
    BN_LETTER_A: PHONEME_X,  # অ ->
    BN_LETTER_AA: PHONEME_A,  # আ ->
    BN_LETTER_I: PHONEME_I,  # ই ->
    BN_LETTER_II: PHONEME_I,  # ঈ ->
    BN_LETTER_U: PHONEME_U,  # উ ->
    BN_LETTER_UU: PHONEME_U,  # ঊ ->
    BN_LETTER_R_VOCALIC: PHONEME_R,  # ঋ ->
    BN_LETTER_E: PHONEME_E,  # এ ->
    BN_LETTER_AI: PHONEME_XI,  # ঐ ->
    BN_LETTER_O: PHONEME_O,  # ও ->
    BN_LETTER_AO: PHONEME_XU,  # ঔ ->
    BN_LETTER_KA: PHONEME_K,  # ক ->
    BN_LETTER_KHA: PHONEME_KH,  # খ ->
    BN_LETTER_GA: PHONEME_G,  # গ ->
    BN_LETTER_GHA: PHONEME_GH,  # ঘ ->
    BN_LETTER_NGA: PHONEME_NG,  # ঙ ->
    BN_LETTER_CA: PHONEME_C,  # চ ->
    BN_LETTER_CHA: PHONEME_S,  # ছ ->
    BN_LETTER_JA: PHONEME_Z,  # জ ->
    BN_LETTER_JHA: PHONEME_ZH,  # ঝ ->
    BN_LETTER_NYA: PHONEME_N,  # ঞ ->
    BN_LETTER_TTA: PHONEME_T,  #  ট ->
    BN_LETTER_TTHA: PHONEME_TH,  # ঠ ->
    BN_LETTER_DDA: PHONEME_D,  # ড ->
    BN_LETTER_DDHA: PHONEME_DH,  # ঢ ->
    BN_LETTER_NNA: PHONEME_N,  # ণ ->
    BN_LETTER_TA: PHONEME_T,  # ত ->
    BN_LETTER_THA: PHONEME_TH,  # থ ->
    BN_LETTER_DA: PHONEME_D,  # দ ->
    BN_LETTER_DHA: PHONEME_DH,  # ধ ->
    BN_LETTER_NA: PHONEME_N,  # ন ->
    BN_LETTER_PA: PHONEME_P,  # প ->
    BN_LETTER_PHA: PHONEME_PH,  # ফ ->
    BN_LETTER_BA: PHONEME_B,  # ব ->
    BN_LETTER_BHA: PHONEME_BH,  # ভ ->
    BN_LETTER_MA: PHONEME_M,  # ম ->
    BN_LETTER_YA: PHONEME_J,  # য ->
    BN_LETTER_RA: PHONEME_R,  # র ->
    BN_LETTER_LA: PHONEME_L,  # ল ->
    BN_LETTER_SHA: PHONEME_S,  # শ ->
    BN_LETTER_SSA: PHONEME_S,  # ষ ->
    BN_LETTER_SA: PHONEME_S,  # স ->
    BN_LETTER_H: PHONEME_H,  # হ ->
    BN_VOWEL_AA: PHONEME_A,  # া ->
    BN_VOWEL_I: PHONEME_I,  # ি ->
    BN_VOWEL_II: PHONEME_I,  # ী ->
    BN_VOWEL_U: PHONEME_U,  # ু ->
    BN_VOWEL_UU: PHONEME_U,  # ূ ->
    BN_VOWEL_R_VOCALIC: PHONEME_R,  # ৃ ->
    BN_VOWEL_E: PHONEME_E,  # ে ->
    BN_VOWEL_AI: PHONEME_XI,  # ৈ ->
    BN_VOWEL_O: PHONEME_O,  # ো ->
    BN_VOWEL_AU: PHONEME_XU,  #  ৌ ->
    BN_LETTER_KHANDA_TA: PHONEME_T,  # ৎ ->
    BN_LETTER_RRA: PHONEME_R,  # ড় ->
    BN_LETTER_RHA: PHONEME_R,  # ঢ় ->
    BN_LETTER_YYA: PHONEME_J,  # য় ->
    BN_LETTER_W: PHONEME_W,  # ৱ ->
}

PHONEME_TO_MM_BEGIN: Dict[str, str] = {
    PHONEME_K: MM_LETTER_KOK,  # -> ꯀ
    PHONEME_KH: MM_LETTER_KHOU,  # -> ꯈ
    PHONEME_G: MM_LETTER_GOK,  # -> ꯒ
    PHONEME_GH: MM_LETTER_GHOU,  # -> ꯘ
    PHONEME_NG: MM_LETTER_NGOU,  # -> ꯉ
    PHONEME_C: MM_LETTER_CHIL,  # -> ꯆ
    PHONEME_Z: MM_LETTER_JIL,  # -> ꯖ
    PHONEME_ZH: MM_LETTER_JHAM,  # -> ꯓ
    PHONEME_T: MM_LETTER_TIL,  # -> ꯇ
    PHONEME_TH: MM_LETTER_THOU,  # -> ꯊ
    PHONEME_D: MM_LETTER_DIL,  # -> ꯗ
    PHONEME_DH: MM_LETTER_DHOU,  # -> ꯙ
    PHONEME_N: MM_LETTER_NA,  # -> ꯅ
    PHONEME_P: MM_LETTER_PA,  # -> ꯄ
    PHONEME_PH: MM_LETTER_PHAM,  # -> ꯐ
    PHONEME_B: MM_LETTER_BA,  # -> ꯕ
    PHONEME_BH: MM_LETTER_BHAM,  # -> ꯚ
    PHONEME_M: MM_LETTER_MIT,  # -> ꯃ
    PHONEME_J: MM_LETTER_YANG,  # -> ꯌ
    PHONEME_R: MM_LETTER_RAI,  # -> ꯔ
    PHONEME_W: MM_LETTER_WAI,  # -> ꯋ
    PHONEME_L: MM_LETTER_LAI,  # -> ꯂ
    PHONEME_S: MM_LETTER_SAM,  # -> ꯁ
    PHONEME_H: MM_LETTER_HUK,  # -> ꯍ
    PHONEME_I: MM_LETTER_I,  # -> ꯏ
    PHONEME_E: f"{MM_LETTER_ATIYA}{MM_VOWEL_YENAP}",  # -> ꯑꯦ
    PHONEME_A: f"{MM_LETTER_ATIYA}{MM_VOWEL_ANAP}",  # -> ꯁꯥ
    PHONEME_X: MM_LETTER_ATIYA,  # -> ꯑ
    PHONEME_U: MM_LETTER_UN,  # -> ꯎ
    PHONEME_O: f"{MM_LETTER_ATIYA}{MM_VOWEL_ONAP}",  # -> ꯑꯣ
    PHONEME_AI: f"{MM_LETTER_ATIYA}{MM_VOWEL_ANAP}{MM_LETTER_I_LONSUM}",  # -> ꯑꯥꯢ
    PHONEME_XI: f"{MM_LETTER_ATIYA}{MM_VOWEL_CHEINAP}",  # -> ꯑꯩ
    PHONEME_UI: f"{MM_LETTER_UN}{MM_LETTER_I_LONSUM}",  # -> ꯎꯢ
    PHONEME_OI: f"{MM_LETTER_ATIYA}{MM_VOWEL_ONAP}{MM_LETTER_I_LONSUM}",  # -> ꯑꯣꯢ
    PHONEME_AU: f"{MM_LETTER_ATIYA}{MM_VOWEL_ANAP}{MM_LETTER_UN}",  # -> ꯑꯥꯎ
    PHONEME_XU: f"{MM_LETTER_ATIYA}{MM_VOWEL_SOUNAP}",  # -> ꯑꯧ
}

# Approach: Nearest phoneme
PHONEME_TO_MM_END: Dict[str, str] = {
    PHONEME_K: MM_LETTER_KOK_LONSUM,  # -> ꯛ
    PHONEME_KH: MM_LETTER_KOK_LONSUM,  # -> ꯛ
    PHONEME_G: MM_LETTER_KOK_LONSUM,  # -> ꯛ
    PHONEME_GH: MM_LETTER_KOK_LONSUM,  # -> ꯛ
    PHONEME_NG: MM_LETTER_NGOU_LONSUM,  # -> ꯡ
    PHONEME_C: MM_LETTER_CHIL,  # -> ꯆ
    PHONEME_Z: MM_LETTER_JIL,  # -> ꯖ
    PHONEME_ZH: MM_LETTER_JIL,  # -> ꯖ
    PHONEME_T: MM_LETTER_TIL_LONSUM,  # -> ꯠ
    PHONEME_TH: MM_LETTER_TIL_LONSUM,  # -> ꯠ
    PHONEME_D: MM_LETTER_TIL_LONSUM,  # -> ꯠ
    PHONEME_DH: MM_LETTER_TIL_LONSUM,  # -> ꯠ
    PHONEME_N: MM_LETTER_NA_LONSUM,  # -> ꯟ
    PHONEME_P: MM_LETTER_PA_LONSUM,  # -> ꯞ
    PHONEME_PH: MM_LETTER_PHAM,  # -> ꯐ
    PHONEME_B: MM_LETTER_BA,  # -> ꯕ
    PHONEME_BH: MM_LETTER_BHAM,  # -> ꯚ
    PHONEME_M: MM_LETTER_MIT_LONSUM,  # -> ꯝ
    PHONEME_R: MM_LETTER_RAI,  # -> ꯔ
    PHONEME_L: MM_LETTER_LAI_LONSUM,  # -> ꯜ
    PHONEME_S: MM_LETTER_SAM,  # -> ꯁ
    PHONEME_I: MM_VOWEL_INAP,  # -> ꯤ
    PHONEME_E: MM_VOWEL_YENAP,  # -> ꯦ
    PHONEME_A: MM_VOWEL_ANAP,  # -> ꯥ
    PHONEME_U: MM_VOWEL_UNAP,  # -> ꯨ
    PHONEME_O: MM_VOWEL_ONAP,  # -> ꯣ
    PHONEME_AI: f"{MM_VOWEL_ANAP}{MM_LETTER_I_LONSUM}",  # -> ꯥꯥꯢ
    PHONEME_XI: MM_VOWEL_CHEINAP,  # -> ꯩ
    PHONEME_UI: f"{MM_VOWEL_UNAP}{MM_LETTER_I_LONSUM}",  # -> ꯨꯢ
    PHONEME_OI: f"{MM_VOWEL_ONAP}{MM_LETTER_I_LONSUM}",  # -> ꯣꯢ
    PHONEME_AU: f"{MM_VOWEL_ANAP}{MM_LETTER_UN}",  # -> ꯥꯎ
    PHONEME_XU: MM_VOWEL_SOUNAP,  # -> ꯧ
}

SSP_TYPE_SIEVERS = "sievers"
SSP_TYPE_PARKER = "parker"


def calculate_sonority(phoneme: str, method: str = SSP_TYPE_SIEVERS) -> int:
    if method == SSP_TYPE_SIEVERS:
        if phoneme in SIEVERS_VOWEL:
            return 5
        elif phoneme in SIEVERS_GLIDE:
            return 4
        elif phoneme in SIEVERS_LIQUID:
            return 3
        elif phoneme in SIEVERS_NASAL:
            return 2
        elif phoneme in SIEVERS_OBSTRUENT:
            return 1
        elif phoneme in SIEVERS_S:
            return 0
        else:
            return -1
    elif method == SSP_TYPE_PARKER:
        if phoneme in SIEVERS_VOWEL:
            return 12
        elif phoneme in PARKER_GLIDE:
            return 11
        elif phoneme in PARKER_RHOTIC:
            return 10
        elif phoneme in PARKER_LATERAL:
            return 9
        elif phoneme in PARKER_FLAP:
            return 8
        elif phoneme in PARKER_TRILL:
            return 7
        elif phoneme in PARKER_NASAL:
            return 6
        elif phoneme in PARKER_H:
            return 5
        elif phoneme in PARKER_VOICED_FRICATIVE:
            return 4
        elif phoneme in PARKER_VOICED_STOP.union(PARKER_VOICED_AFFRICATE):
            return 3
        elif phoneme in PARKER_VOICELESS_FRICATIVE:
            return 1  # Modified 2 -> 1
        elif phoneme in PARKER_VOICELESS_STOP.union(PARKER_VOICELESS_AFFRICATE):
            return 2  # Modified 1 -> 2
        elif phoneme in SIEVERS_S:
            return 0
        else:
            return -1
    else:
        return -1
