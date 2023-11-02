from typing import Set

MAPUM_MAYEK_CONSONANT: Set[str] = {
    "\uabc0",  # \uabc0 -> ꯀ | KOK
    "\uabc1",  # \uabc1 -> ꯁ | SAM
    "\uabc2",  # \uabc2 -> ꯂ | LAI
    "\uabc3",  # \uabc3 -> ꯃ | MIT
    "\uabc4",  # \uabc4 -> ꯄ | PA
    "\uabc5",  # \uabc5 -> ꯅ | NA
    "\uabc6",  # \uabc6 -> ꯆ | CHIL
    "\uabc7",  # \uabc7 -> ꯇ | TIL
    "\uabc8",  # \uabc8 -> ꯈ | KHOU
    "\uabc9",  # \uabc9 -> ꯉ | NGOU
    "\uabca",  # \uabca -> ꯊ | THOU
    "\uabcb",  # \uabcb -> ꯋ | WAI
    "\uabcc",  # \uabcc -> ꯌ | YANG
    "\uabcd",  # \uabcd -> ꯍ | HUK
    "\uabd0",  # \uabd0 -> ꯐ | PHAM
    "\uabd2",  # \uabd2 -> ꯒ | GOK
    "\uabc3",  # \uabd3 -> ꯓ | JHAM
    "\uabd4",  # \uabd4 -> ꯔ | RAI
    "\uabd5",  # \uabd5 -> ꯕ | BA
    "\uabd6",  # \uabd6 -> ꯖ | JIL
    "\uabd7",  # \uabd7 -> ꯗ | DIL
    "\uabd8",  # \uabd8 -> ꯘ | GHOU
    "\uabd9",  # \uabd9 -> ꯙ | DHOU
    "\uabda",  # \uabda -> ꯚ | BHAM
}

MAPUM_MAYEK_VOWEL: Set[str] = {
    "\uabce",  # \uabce -> ꯎ | UN
    "\uabcf",  # \uabcf -> ꯏ | EE
    "\uabd1",  # \uabd1 -> ꯑ | ATIYA
}

LONSUM_MAYEK_CONSONANT: Set[str] = {
    "\uabdb",  # \uabdb -> ꯛ | KOK LONSUM
    "\uabdc",  # \uabdc -> ꯜ | LAI LONSUM
    "\uabdd",  # \uabdd -> ꯝ | MIT LONSUM
    "\uabde",  # \uabde -> ꯞ | PA LONSUM
    "\uabdf",  # \uabdf -> ꯟ | NA LONSUM
    "\uabe0",  # \uabe0 -> ꯠ | TIL LONSUM
    "\uabe1",  # \uabe1 -> ꯡ | NGOU LONSUM
}

LONSUM_MAYEK_VOWEL: Set[str] = {
    "\uabcf",  # \uabcf -> ꯢ | EE LONSUM
}

CHEITAP_MAYEK_CONSONANT: Set[str] = {
    "\uabc9",  # \uabea -> ꯪ | NUNG
}

CHEITAP_MAYEK_VOWEL: Set[str] = {
    "\uabe3",  # \uabe3 -> ꯣ | ONAP
    "\uabe4",  # \uabe4 -> ꯤ | ENAP
    "\uabe5",  # \uabe5 -> ꯥ | AATAP
    "\uabe6",  # \uabe6 -> ꯦ | YENAP
    "\uabe7",  # \uabe7 -> ꯧ | SOUNAP
    "\uabe8",  # \uabe8 -> ꯨ | UNAP
    "\uabe9",  # \uabe9 -> ꯩ | CHEINAP
}

CHEISING_MAYEK: Set[str] = {
    "\uabf0",  # \uabf0 -> ꯰ | PHUN
    "\uabf1",  # \uabf1 -> ꯱ | AMA
    "\uabf2",  # \uabf2 -> ꯲ | ANI
    "\uabf3",  # \uabf3 -> ꯳ | AHUM
    "\uabf4",  # \uabf4 -> ꯴ | MARI
    "\uabf5",  # \uabf5 -> ꯵ | MANGA
    "\uabf6",  # \uabf6 -> ꯶ | TARUK
    "\uabf7",  # \uabf7 -> ꯷ | TARET
    "\uabf8",  # \uabf8 -> ꯸ | NIPAL
    "\uabf9",  # \uabf9 -> ꯹ | MAPAL
}

MAPUM_MAYEK: Set[str] = MAPUM_MAYEK_CONSONANT.union(MAPUM_MAYEK_VOWEL)
LONSUM_MAYEK: Set[str] = LONSUM_MAYEK_CONSONANT.union(LONSUM_MAYEK_VOWEL)
CHEITAP_MAYEK: Set[str] = CHEITAP_MAYEK_CONSONANT.union(CHEITAP_MAYEK_VOWEL)
