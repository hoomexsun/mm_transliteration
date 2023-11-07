from typing import Set


SIGN_CANDRABINDU = "\u0981"  # \u0981 -> ঁ
SIGN_ANUSVARA = "\u0982"  # \u0982 -> ং
SIGN_VISARGA = "\u0983"  # \u0983 -> ঃ
# Letters
LETTER_A: str = "\u0985"  # \u0985 -> অ
LETTER_AA: str = "\u0986"  # \u0986 -> আ
LETTER_I: str = "\u0987"  # \u0987 -> ই
LETTER_II: str = "\u0988"  # \u0988 -> ঈ
LETTER_U: str = "\u0989"  # \u0989 -> উ
LETTER_UU: str = "\u098a"  # \u098a -> ঊ
LETTER_R_VOCALIC: str = "\u098b"  # \u098b -> ঋ
LETTER_E: str = "\u098f"  # \u098f -> এ
LETTER_AI: str = "\u0990"  # \u0990 -> ঐ
LETTER_O: str = "\u0993"  # \u0993 -> ও
LETTER_AO: str = "\u0994"  # \u0994 -> ঔ
LETTER_KA: str = "\u0995"  # \u0995 -> ক
LETTER_KHA: str = "\u0996"  # \u0996 -> খ
LETTER_GA: str = "\u0997"  # \u0997 -> গ
LETTER_GHA: str = "\u0998"  # \u0998 -> ঘ
LETTER_NGA: str = "\u0999"  # \u0999 -> ঙ
LETTER_CA: str = "\u099a"  # \u099a -> চ
LETTER_CHA: str = "\u099b"  # \u099b -> ছ
LETTER_JA: str = "\u099c"  # \u099c -> জ
LETTER_JHA: str = "\u099d"  # \u099d -> ঝ
LETTER_NYA: str = "\u099e"  # \u099e -> ঞ
LETTER_TTA: str = "\u099f"  # \u099f -> ট
LETTER_TTHA: str = "\u09a0"  # \u09a0 -> ঠ
LETTER_DDA: str = "\u09a1"  # \u09a1 -> ড
LETTER_DDHA: str = "\u09a2"  # \u09a2 -> ঢ
LETTER_NNA: str = "\u09a3"  # \u09a3 -> ণ
LETTER_TA: str = "\u09a4"  # \u09a4 -> ত
LETTER_THA: str = "\u09a5"  # \u09a5 -> থ
LETTER_DA: str = "\u09a6"  # \u09a6 -> দ
LETTER_DHA: str = "\u09a7"  # \u09a7 -> ধ
LETTER_NA: str = "\u09a8"  # \u09a8 -> ন
LETTER_PA: str = "\u09aa"  # \u09aa -> প
LETTER_PHA: str = "\u09ab"  # \u09ab -> ফ
LETTER_BA: str = "\u09ac"  # \u09ac -> ব
LETTER_BHA: str = "\u09ad"  # \u09ad -> ভ
LETTER_MA: str = "\u09ae"  # \u09ae -> ম
LETTER_YA: str = "\u09af"  # \u09af -> য
LETTER_RA: str = "\u09b0"  # \u09b0 -> র
LETTER_LA: str = "\u09b2"  # \u09b2 -> ল
LETTER_SHA: str = "\u09b6"  # \u09b6 -> শ
LETTER_SSA: str = "\u09b7"  # \u09b7 -> ষ
LETTER_SA: str = "\u09b8"  # \u09b8 -> স
LETTER_H: str = "\u09b9"  # \u09b9 -> হ
# Vowel signs
VOWEL_AA: str = "\u09be"  # \u09be -> া
VOWEL_I: str = "\u09bf"  # \u09bf -> ি
VOWEL_II: str = "\u09c0"  # \u09c0 -> ী
VOWEL_U: str = "\u09c1"  # \u09c1 -> ু
VOWEL_UU: str = "\u09c2"  # \u09c2 -> ূ
VOWEL_R_VOCALIC: str = "\u09c3"  # \u09c3 -> ৃ
VOWEL_E: str = "\u09c7"  # \u09c7 -> ে
VOWEL_AI: str = "\u09c8"  # \u09c8 -> ৈ
VOWEL_O: str = "\u09cb"  # \u09cb ->  ো
VOWEL_AU: str = "\u09cc"  # \u09cc ->  ৌ
# Signs
SIGN_VIRAMA: str = "\u09cd"  # \u09cd -> ্
LETTER_KHANDA_TA: str = "\u09ce"  # \u09ce -> ৎ
MARK_AU: str = "\u09d7"  # \u09d7 -> ৗ
# Letters
LETTER_RRA: str = "\u09dc"  # \u09dc -> ড়
LETTER_RHA: str = "\u09dd"  # \u09dd -> ঢ়
LETTER_YYA: str = "\u09df"  # \u09df -> য়
# Digits
DIGIT_ZERO: str = "\u09e6"  # \u09e6 -> ০
DIGIT_ONE: str = "\u09e7"  # \u09e7 -> ১
DIGIT_TWO: str = "\u09e8"  # \u09e8 -> ২
DIGIT_THREE: str = "\u09e9"  # \u09e9 -> ৩
DIGIT_FOUR: str = "\u09ea"  # \u09ea -> ৪
DIGIT_FIVE: str = "\u09eb"  # \u09eb -> ৫
DIGIT_SIX: str = "\u09ec"  # \u09ec -> ৬
DIGIT_SEVEN: str = "\u09ed"  # \u09ed -> ৭
DIGIT_EIGHT: str = "\u09ee"  # \u09ee -> ৮
DIGIT_NINE: str = "\u09ef"  # \u09ef -> ৯
# Originally Bengali Letter Ra with Lower Diagonal
LETTER_W: str = "\u09F1"  # \u09f1 -> ৱ

# Sets
BN_INDEPENDENT_VELAR = {
    LETTER_KA,
    LETTER_KHA,
    LETTER_GA,
    LETTER_GHA,
    LETTER_NGA,
}

#! Arrange the LETTERacters according to SSP arranged using acoustic intensity (11->1)
#! glide > rhotic > lateral > flap > trill > nasal > h > voiced fricative >
#! voiced stop/affricate > voiceless fricative > voiceless stop/affricate

GLIDE: Set[str] = {}
RHOTIC: Set[str] = {}
LATERAL: Set[str] = {}
FLAP: Set[str] = {}
TRILL: Set[str] = {}
NASAL: Set[str] = {}
H: Set[str] = {}
VOICED_FRICATIVE: Set[str] = {}
VOICED_AFFRICATE: Set[str] = {}
VOICELESS_FRICATIVE: Set[str] = {}
VOICELESS_AFFRICATE: Set[str] = {}


BN_DEPENDENT_CONSONANT: Set[str] = {
    VOWEL_R_VOCALIC,
    LETTER_KHANDA_TA,
    SIGN_ANUSVARA,
}

BN_INDEPENDENT_VOWEL: Set[str] = {
    LETTER_A,
    LETTER_AA,
    LETTER_I,
    LETTER_II,
    LETTER_U,
    LETTER_UU,
    LETTER_E,
    LETTER_AI,
    LETTER_O,
    LETTER_AO,
}

BN_DEPENDENT_VOWEL: Set[str] = {
    VOWEL_AA,
    VOWEL_I,
    VOWEL_II,
    VOWEL_U,
    VOWEL_UU,
    VOWEL_E,
    VOWEL_AI,
    VOWEL_O,
    VOWEL_AU,
}

DIPHTHONGS_AI: Set[str] = {
    VOWEL_AA + LETTER_I,  # \u09be\u0987 -> াই
    VOWEL_AA + LETTER_YA,  # \u09be\u09af -> ায
    VOWEL_AA + LETTER_YYA,  # \u09be\u09df -> ায়
}
DIPHTHONGS_OI: Set[str] = {
    VOWEL_O + LETTER_I,  # \u09cb\u0987 ->  োই
    VOWEL_O + LETTER_YA,  # \u09cb\u09af ->  োয
    VOWEL_O + LETTER_YYA,  # \u09cb\u09df ->  োয়
}
DIPHTHONGS_UI: Set[str] = {
    VOWEL_U + LETTER_I,  # \u09c1\u0987 -> ুই
    VOWEL_U + LETTER_YA,  # \u09c1\u09af -> ুয
    VOWEL_U + LETTER_YYA,  # \u09c1\u09df -> ুয়
    VOWEL_UU + LETTER_I,  # \u09c2\u0987 -> ূই
    VOWEL_UU + LETTER_YA,  # \u09c2\u09af -> ূয
    VOWEL_UU + LETTER_YYA,  # \u09c2\u09df -> ূয়
}
DIPHTHONGS_AO: Set[str] = {
    VOWEL_AA + LETTER_U,  # \u09be\u0989 -> াউ
    VOWEL_AA + LETTER_UU,  # \u09be\u098a -> াঊ
    VOWEL_AA + LETTER_O,  # \u09be\u0993 -> াও
}
BN_DEPENDENT_DIPHTHONGS: Set[str] = DIPHTHONGS_AI.union(
    DIPHTHONGS_OI, DIPHTHONGS_UI, DIPHTHONGS_AO
)

BN_PUNCTUATION: Set[str] = {
    SIGN_VISARGA,
}

BN_NUMERAL: Set[str] = {
    DIGIT_ZERO,
    DIGIT_ONE,
    DIGIT_TWO,
    DIGIT_THREE,
    DIGIT_FOUR,
    DIGIT_FIVE,
    DIGIT_SIX,
    DIGIT_SEVEN,
    DIGIT_EIGHT,
    DIGIT_NINE,
}
