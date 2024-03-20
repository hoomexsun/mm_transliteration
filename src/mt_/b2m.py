from enum import Enum
from typing import Dict, List, Tuple

from lon_.basic import Bengali, MeeteiMayek

from ..lon_ import ARPABETPhoneme, MMPhoneme


class Tag(Enum):
    """Tag used in Syllabification"""

    NULL = "x"
    BOUNDARY = "B"
    CONTINUOUS = "C"
    # Extra
    ERROR = "e"


class Delimiter(Enum):
    """Delimiters used in Syllabification"""

    SYLLABLE = "/"
    UNCLEAR = "?"


class B2P:
    """Bengali to Phoneme"""

    def __init__(self) -> None:
        bn = Bengali()
        mmP = MMPhoneme()

        original_map: Dict[str, List[str]] = {
            mmP.phoneme_k: [bn.letter_ka],
            mmP.phoneme_kh: [bn.letter_kha],
            mmP.phoneme_g: [bn.letter_ga],
            mmP.phoneme_gh: [bn.letter_gha],
            mmP.phoneme_ng: [bn.sign_anusvara, bn.letter_nga],
            mmP.phoneme_c: [bn.letter_ca],
            mmP.phoneme_z: [bn.letter_ja],
            mmP.phoneme_zh: [bn.letter_jha],
            mmP.phoneme_t: [bn.letter_tta, bn.letter_ta, bn.letter_khanda_ta],
            mmP.phoneme_th: [bn.letter_ttha, bn.letter_tha],
            mmP.phoneme_d: [bn.letter_dda, bn.letter_da],
            mmP.phoneme_dh: [bn.letter_ddha, bn.letter_dha],
            mmP.phoneme_n: [bn.letter_nya, bn.letter_nna, bn.letter_na],
            mmP.phoneme_p: [bn.letter_pa],
            mmP.phoneme_ph: [bn.letter_pha],
            mmP.phoneme_b: [bn.letter_ba],
            mmP.phoneme_bh: [bn.letter_bha],
            mmP.phoneme_m: [bn.letter_ma],
            mmP.phoneme_j: [bn.letter_yya, bn.letter_ya],
            mmP.phoneme_r: [
                bn.letter_r_vocalic,
                bn.vowel_r_vocalic,
                bn.letter_rra,
                bn.letter_ra,
                bn.letter_rha,
            ],
            mmP.phoneme_w: [bn.letter_w],
            mmP.phoneme_l: [bn.letter_l],
            mmP.phoneme_s: [bn.letter_cha, bn.letter_ssa, bn.letter_sa, bn.letter_sha],
            mmP.phoneme_h: [bn.letter_h],
            # vowels - monophthongs
            mmP.phoneme_i: [bn.letter_i, bn.letter_ii, bn.vowel_i, bn.vowel_ii],
            mmP.phoneme_e: [bn.letter_e, bn.vowel_e],
            mmP.phoneme_x: [bn.letter_a],
            mmP.phoneme_u: [bn.letter_u, bn.letter_uu, bn.vowel_u, bn.vowel_uu],
            mmP.phoneme_o: [bn.letter_o, bn.vowel_o],
            mmP.phoneme_a: [bn.letter_aa, bn.vowel_aa],
            # vowel - diphthongs
            mmP.phoneme_ai: [
                f"{bn.letter_aa}{bn.letter_i}",
                f"{bn.letter_aa}{bn.letter_ii}",
                f"{bn.letter_aa}{bn.letter_ya}",
                f"{bn.letter_aa}{bn.letter_yya}",
                f"{bn.vowel_aa}{bn.letter_i}",
                f"{bn.vowel_aa}{bn.letter_ii}",
                f"{bn.vowel_aa}{bn.letter_ya}",
                f"{bn.vowel_aa}{bn.letter_yya}",
            ],
            mmP.phoneme_xi: [bn.letter_ai, bn.vowel_ai],
            mmP.phoneme_ui: [
                f"{bn.letter_u}{bn.letter_i}",
                f"{bn.letter_uu}{bn.letter_i}",
                f"{bn.letter_u}{bn.letter_ii}",
                f"{bn.letter_uu}{bn.letter_ii}",
                f"{bn.letter_u}{bn.letter_ya}",
                f"{bn.letter_uu}{bn.letter_ya}",
                f"{bn.letter_u}{bn.letter_yya}",
                f"{bn.letter_uu}{bn.letter_yya}",
                f"{bn.vowel_u}{bn.letter_i}",
                f"{bn.vowel_uu}{bn.letter_i}",
                f"{bn.vowel_u}{bn.letter_ii}",
                f"{bn.vowel_uu}{bn.letter_ii}",
                f"{bn.vowel_u}{bn.letter_ya}",
                f"{bn.vowel_uu}{bn.letter_ya}",
                f"{bn.vowel_u}{bn.letter_yya}",
                f"{bn.vowel_uu}{bn.letter_yya}",
            ],
            mmP.phoneme_oi: [
                f"{bn.letter_o}{bn.letter_i}",
                f"{bn.letter_o}{bn.letter_ii}",
                f"{bn.letter_o}{bn.letter_ya}",
                f"{bn.letter_o}{bn.letter_yya}",
                f"{bn.vowel_o}{bn.letter_i}",
                f"{bn.vowel_o}{bn.letter_ii}",
                f"{bn.vowel_o}{bn.letter_ya}",
                f"{bn.vowel_o}{bn.letter_yya}",
            ],
            mmP.phoneme_au: [
                f"{bn.letter_aa}{bn.letter_u}",
                f"{bn.letter_aa}{bn.letter_uu}",
                f"{bn.letter_aa}{bn.letter_o}",
                f"{bn.vowel_aa}{bn.letter_u}",
                f"{bn.vowel_aa}{bn.letter_uu}",
                f"{bn.vowel_aa}{bn.letter_o}",
            ],
            mmP.phoneme_xu: [bn.letter_ao, bn.vowel_ao],
        }

        self.charmap: Dict[str, str] = {
            char_bn: phoneme
            for phoneme, char_bn_list in original_map.items()
            for char_bn in char_bn_list
        }


class P2M:
    """Phoneme to Meetei Mayek"""

    def __init__(self) -> None:
        mmP = MMPhoneme()
        mm = MeeteiMayek()

        original_map: Dict[str, Tuple[str, str, str]] = {
            mmP.phoneme_k: (mm.letter_kok, mm.letter_kok_lonsum, mm.letter_kok_lonsum),
            mmP.phoneme_kh: (mm.letter_khou.mm_letter_khou, mm.letter_kok_lonsum),
            mmP.phoneme_g: (mm.letter_gok, mm.letter_gok, mm.letter_kok_lonsum),
            mmP.phoneme_gh: (mm.letter_ghou, mm.letter_ghou, mm.letter_kok_lonsum),
            mmP.phoneme_ng: (
                mm.letter_ngou,
                mm.letter_ngou_lonsum,
                mm.letter_ngou_lonsum,
            ),
            mmP.phoneme_c: (mm.letter_chil, mm.letter_chil, mm.letter_chil),
            mmP.phoneme_z: (mm.letter_jil, mm.letter_jil, mm.letter_jil),
            mmP.phoneme_zh: (mm.letter_jham, mm.letter_jham, mm.letter_jil),
            mmP.phoneme_t: (mm.letter_til, mm.letter_til_lonsum, mm.letter_til_lonsum),
            mmP.phoneme_th: (mm.letter_thou, mm.letter_thou, mm.letter_til_lonsum),
            mmP.phoneme_d: (mm.letter_dil, mm.letter_dil, mm.letter_til_lonsum),
            mmP.phoneme_dh: (mm.letter_dhou, mm.letter_dhou, mm.letter_til_lonsum),
            mmP.phoneme_n: (mm.letter_na, mm.letter_na_lonsum, mm.letter_na_lonsum),
            mmP.phoneme_p: (mm.letter_pa, mm.letter_pa_lonsum, mm.letter_pa_lonsum),
            mmP.phoneme_ph: (mm.letter_pham, mm.letter_pham, mm.letter_pa_lonsum),
            mmP.phoneme_b: (mm.letter_ba, mm.letter_ba, mm.letter_pa_lonsum),
            mmP.phoneme_bh: (mm.letter_bham, mm.letter_bham, mm.letter_pa_lonsum),
            mmP.phoneme_m: (mm.letter_mit, mm.letter_mit_lonsum, mm.letter_mit_lonsum),
            mmP.phoneme_j: (mm.letter_yang, mm.letter_i_lonsum, mm.letter_i_lonsum),
            mmP.phoneme_r: (mm.letter_rai, mm.letter_rai, mm.letter_rai),
            mmP.phoneme_w: (mm.letter_wai, "", ""),
            mmP.phoneme_l: (mm.letter_lai, mm.letter_lai_lonsum, mm.letter_lai_lonsum),
            mmP.phoneme_s: (mm.letter_sam, mm.letter_sam, mm.letter_sam),
            mmP.phoneme_h: (mm.letter_huk, "", ""),
            # vowels - monophthongs
            mmP.phoneme_i: (mm.letter_i, mm.vowel_inap, mm.vowel_inap),
            mmP.phoneme_e: (
                f"{mm.letter_atiya}{mm.vowel_yenap}",
                mm.vowel_yenap,
                mm.vowel_yenap,
            ),
            mmP.phoneme_x: (mm.letter_atiya, "", ""),
            mmP.phoneme_u: (mm.letter_un, mm.vowel_unap, mm.vowel_unap),
            mmP.phoneme_o: (
                f"{mm.letter_atiya}{mm.vowel_onap}",
                mm.vowel_onap,
                mm.vowel_onap,
            ),
            mmP.phoneme_a: (
                f"{mm.letter_atiya}{mm.vowel_anap}",
                mm.vowel_anap,
                mm.vowel_anap,
            ),
            # vowel - diphthongs
            mmP.phoneme_ai: (
                f"{mm.letter_atiya}{mm.vowel_anap}{mm.letter_i_lonsum}",
                f"{mm.vowel_anap}{mm.letter_i_lonsum}",
                f"{mm.vowel_anap}{mm.letter_i_lonsum}",
            ),
            mmP.phoneme_xi: (
                f"{mm.letter_atiya}{mm.vowel_cheinap}",
                mm.vowel_cheinap,
                mm.vowel_cheinap,
            ),
            mmP.phoneme_ui: (
                f"{mm.letter_un}{mm.letter_i_lonsum}",
                f"{mm.letter_unap}{mm.letter_i_lonsum}",
                f"{mm.letter_unap}{mm.letter_i_lonsum}",
            ),
            mmP.phoneme_oi: (
                f"{mm.letter_atiya}{mm.vowel_onap}{mm.letter_i_lonsum}",
                f"{mm.vowel_onap}{mm.letter_i_lonsum}",
                f"{mm.vowel_onap}{mm.letter_i_lonsum}",
            ),
            mmP.phoneme_au: (
                f"{mm.letter_atiya}{mm.vowel_anap}{mm.letter_un}",
                f"{mm.vowel_anap}{mm.letter_un}",
                f"{mm.vowel_anap}{mm.letter_un}",
            ),
            mmP.phoneme_xu: (
                f"{mm.letter_atiya}{mm.vowel_sounap}",
                mm.vowel_sounap,
                mm.vowel_sounap,
            ),
        }

        self.mm_begin, self.mm_end, self.mm_end_2 = {}, {}, {}
        for key, value in original_map.items():
            self.mm_begin[key] = value[0]
            self.mm_end[key] = value[1]
            self.mm_end_2[key] = value[2]


class ARPA2MM:
    def get_map():
        mm = MMPhoneme()
        arpa = ARPABETPhoneme(num_letters=2)
        mm_to_arpabet: Dict[str | List[str]] = {
            mm.phoneme_k: [arpa.phoneme_K],
            mm.phoneme_kh: [],
            mm.phoneme_g: [arpa.phoneme_G],
            mm.phoneme_gh: [],
            mm.phoneme_ng: [arpa.phoneme_NG],
            mm.phoneme_c: [arpa.phoneme_CH],
            mm.phoneme_z: [arpa.phoneme_JH, arpa.phoneme_Z, arpa.phoneme_ZH],
            mm.phoneme_zh: [],
            mm.phoneme_t: [arpa.phoneme_DX, arpa.phoneme_T],
            mm.phoneme_th: [arpa.phoneme_TH],
            mm.phoneme_d: [arpa.phoneme_D],
            mm.phoneme_dh: [arpa.phoneme_DH],
            mm.phoneme_n: [arpa.phoneme_N, arpa.phoneme_NX],
            mm.phoneme_p: [arpa.phoneme_P],
            mm.phoneme_ph: [arpa.phoneme_F],
            mm.phoneme_b: [arpa.phoneme_B],
            mm.phoneme_bh: [arpa.phoneme_V],
            mm.phoneme_m: [arpa.phoneme_M],
            mm.phoneme_j: [arpa.phoneme_Y],
            mm.phoneme_r: [arpa.phoneme_R],
            mm.phoneme_w: [arpa.phoneme_W, arpa.phoneme_WH],
            mm.phoneme_l: [arpa.phoneme_L],
            mm.phoneme_s: [arpa.phoneme_S, arpa.phoneme_SH],
            mm.phoneme_h: [arpa.phoneme_H],
            # vowels - monophthongs
            mm.phoneme_i: [arpa.phoneme_IH, arpa.phoneme_IX, arpa.phoneme_IY],
            mm.phoneme_e: [arpa.phoneme_AE, arpa.phoneme_EH],
            mm.phoneme_x: [arpa.phoneme_AH, arpa.phoneme_AX, arpa.phoneme_Q],
            mm.phoneme_u: [arpa.phoneme_UH, arpa.phoneme_UW, arpa.phoneme_UX],
            mm.phoneme_o: [arpa.phoneme_AO, arpa.phoneme_OW],
            mm.phoneme_a: [arpa.phoneme_AA],
            # extras
            mm.phoneme_au: [arpa.phoneme_AW],
            f"{mm.phoneme_x}{mm.phoneme_r}": [arpa.phoneme_AXR, arpa.phoneme_ER],
            mm.phoneme_ai: [arpa.phoneme_AY, arpa.phoneme_EY],
            mm.phoneme_oi: [arpa.phoneme_OY],
            f"{mm.phoneme_x}{mm.phoneme_l}": [arpa.phoneme_EL],
            f"{mm.phoneme_x}{mm.phoneme_m}": [arpa.phoneme_EM],
            f"{mm.phoneme_x}{mm.phoneme_n}": [arpa.phoneme_EN],
        }
        return {
            ipa: phoneme
            for phoneme, ipa_list in mm_to_arpabet.items()
            for ipa in ipa_list
            if ipa_list
        }
