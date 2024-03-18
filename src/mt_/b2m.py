from typing import Dict, List

from ..lon_ import ARPABETPhoneme, MMPhoneme


class B2Phoneme:
    pass


def arpa_to_mm(phoneme: str = ""):
    arpabet_to_mm = get_map()
    print(arpabet_to_mm)


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


arpa_to_mm()
