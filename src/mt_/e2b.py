from typing import Dict, Set

from ..lon_ import Bengali


class E2B:
    def __init__(self) -> None:
        bn = Bengali()

        self.premap = {
            "\u00e5\u00a1\u00b8": "\u00b8\u00a1\u00e5",  # \u00e5\u00a1\00b8 -> å¡¸ : \u00b8\u00a1\u00e5 -> ¸¡å #! Eg: security, virtual,
        }

        self.en_punctuations = {
            "\u0021",  # \u0021 -> ! (Exclamation mark)
            "\u0025",  # \u0025 -> % (Percent sign)
            "\u0028",  # \u0028 -> ( (Left Parenthesis)
            "\u0029",  # \u0029 -> ) (Right Parenthesis)
            "\u002c",  # \u002c -> , (Comma)
            "\u002d",  # \u002d -> - (Hyphen-minus)
            "\u002e",  # \u002e -> . (Full stop)
            "\u003a",  # \u003a -> : (Colon)
            "\u003f",  # \u003f -> ? (Question mark)
            "\u2018",  # \u2018 ->  (Left Single Quotation mark)
            "\u2019",  # \u2019 ->  (Right Single Quotation mark)
        }

        self.charmap = {
            "\u0022": bn.letter_a,  # \u0022 -> " : অ #! MISSING SP
            "\u0022\u00e0": bn.letter_aa,  # \u0022\u00e0 -> "à : আ
            "\u0023": bn.letter_ii,  # \u0023 -> # : ঈ
            "\u0024": bn.letter_uu,  # \u0024 -> $ : ঊ
            "\u0026": bn.letter_e,  # \u0026 -> & : এ
            "\u0027": bn.letter_ai,  # \u0027 -> ' : ঐ
            "\u002a": bn.letter_o,  # \u002a -> * : ও
            "\u002b": bn.letter_ao,  # \u002b -> + : ঔ
            "\u002f": f"{bn.letter_ba}{bn.sign_virama}",  # \u002f -> / : ব্ #! Up as []
            "\u0030": bn.digit_zero,  # \u0030 -> 0 : ০
            "\u0031": bn.digit_one,  # \u0031 -> 1 : ১
            "\u0032": bn.digit_two,  # \u0032 -> 2 : ২
            "\u0033": bn.digit_three,  # \u0033 -> 3 : ৩
            "\u0034": bn.digit_four,  # \u0034 -> 4 : ৪
            "\u0035": bn.digit_five,  # \u0035 -> 5 : ৫
            "\u0036": bn.digit_six,  # \u0036 -> 6 : ৬
            "\u0037": bn.digit_seven,  # \u0037 -> 7 : ৭
            "\u0038": bn.digit_eight,  # \u0038 -> 8 : ৮
            "\u0039": bn.digit_nine,  # \u0039 -> 9 : ৯
            "\u003b": bn.letter_khanda_ta,  # \u003b -> ; : ৎ
            "\u003d": bn.letter_tha,  # \u003d -> = :  থ
            "\u003e": bn.letter_na,  # \u003e -> > : ন
            "\u0040": bn.sign_visarga,  # \u0040 -> @ : ঃ
            "\u0041": bn.letter_ka,  # \u0041 -> A : ক
            "\u0042": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_ka}",  # \u0042 -> B : ক্ক
            "\u0043": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_tta}",  # \u0043 -> C : ক্ট
            "\u0044": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_ta}{bn.sign_virama}{bn.letter_ba}",  # \u0044 -> D : ক্ত্ব
            "\u0045": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_ba}",  # \u0045 -> E : ক্ব
            "\u0046": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_ma}",  # \u0046 -> F : ক্ম
            "\u0047": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_sa}",  # \u0047 -> G : ক্স
            "\u0048": f"{bn.sign_virama}{bn.letter_ka}",  # \u0048 -> H :  ্ক #! Down as [sk]
            "\u0049": f"{bn.sign_virama}{bn.letter_ka}{bn.sign_virama}{bn.letter_ra}",  # \u0049 -> I : ্ক্র #! Down as [skr]
            "\u004a": bn.letter_kha,  # \u004a -> J : খ
            "\u004b": bn.letter_ga,  # \u004b -> K : গ
            "\u004c": f"{bn.letter_ga}{bn.sign_virama}{bn.letter_ga}",  # \u004c -> L : গ্গ
            "\u004d": f"{bn.letter_ga}{bn.sign_virama}{bn.letter_ba}",  # \u004d -> M : গ্ব
            "\u004e": f"{bn.letter_ga}{bn.sign_virama}",  # \u004e -> N : গ্ #! Up as [gn, gr, gl]
            "\u004f": f"{bn.letter_ga}{bn.sign_virama}",  # \u004f -> O : গ্ #! Left as []
            "\u0050": f"{bn.letter_ga}{bn.vowel_u}",  # \u0050 -> P : গু
            "\u0051": bn.letter_gha,  # \u0051 -> Q : ঘ
            "\u0052": bn.letter_nga,  # \u0052 -> R : ঙ
            "\u0053": f"{bn.letter_nga}{bn.sign_virama}{bn.letter_ka}",  # \u0053 -> S : ঙ্ক
            "\u0054": f"{bn.letter_nga}{bn.sign_virama}{bn.letter_kha}",  # \u0054 -> T : ঙ্খ
            "\u0055": f"{bn.letter_nga}{bn.sign_virama}{bn.letter_ga}",  # \u0055 -> U : ঙ্গ
            "\u0056": f"{bn.letter_nga}{bn.sign_virama}",  # \u0056 -> V : ঙ্ #! Left as [ng-gh]
            "\u0057": bn.letter_ca,  # \u0057 -> W : চ
            "\u0058": f"{bn.letter_ca}{bn.sign_virama}{bn.letter_nya}",  # \u0058 -> X : চ্ঞ
            "\u0059": f"{bn.letter_ca}{bn.sign_virama}{bn.letter_cha}{bn.sign_virama}{bn.letter_ba}",  # \u0059 -> Y : চ্ছ্ব
            "\u005a": f"{bn.letter_ca}{bn.sign_virama}",  # \u005a -> Z : চ্ #! Left as []
            "\u005b": bn.vowel_i,  # \u005b -> [ : ি
            "\u005c": bn.letter_ja,  # \u005c -> \ : জ
            "\u005d": f"{bn.mark_au}{bn.sign_candrabindu}",  # \u005d -> ] : ৗঁ
            "\u005e": f"{bn.letter_ja}{bn.sign_virama}{bn.letter_ja}{bn.sign_virama}{bn.letter_ba}",  # \u005e -> ^ : জ্জ্ব
            "\u005f": f"{bn.letter_ja}{bn.sign_virama}{bn.letter_jha}",  # \u005f -> _ : জ্ঝ
            "\u0060": f"{bn.letter_ja}{bn.sign_virama}{bn.letter_nya}",  # \u0060 -> ` : জ্ঞ
            "\u0061": f"{bn.letter_ja}{bn.sign_virama}{bn.letter_ba}",  # \u0061 -> a : জ্ব
            "\u0062": f"{bn.letter_ja}{bn.sign_virama}{bn.letter_ra}",  # \u0062 -> b : জ্র
            "\u0063": bn.letter_jha,  # \u0063 -> c :  ঝ
            "\u0064": bn.letter_nya,  # \u0064 -> d : ঞ
            "\u0065": f"{bn.letter_nya}{bn.sign_virama}{bn.letter_ca}",  # \u0065 -> e : ঞ্চ
            "\u0066": f"{bn.letter_nya}{bn.sign_virama}{bn.letter_cha}",  # \u0066 -> f : ঞ্ছ
            "\u0067": f"{bn.letter_nya}{bn.sign_virama}{bn.letter_ja}",  # \u0067 -> g : ঞ্জ
            "\u0068": f"{bn.letter_nya}{bn.sign_virama}{bn.letter_jha}",  # \u0068 -> h : ঞ্ঝ
            "\u0069": bn.letter_tta,  # \u0069 -> i : ট
            "\u006a": f"{bn.letter_tta}{bn.sign_virama}{bn.letter_tta}",  # \u006a -> j : ট্ট
            "\u006b": bn.letter_ttha,  # \u006b -> k : ঠ
            "\u006c": bn.letter_dda,  # \u006c -> l :  ড
            "\u006c\u00a1\u00fc": bn.letter_u,  # \u006c\u00a1\u00fc -> l¡ü : উ
            "\u006d": f"{bn.letter_dda}{bn.sign_virama}{bn.letter_dda}",  # \u006d -> m : ড্ড
            "\u006e": bn.letter_ddha,  # \u006e -> n : ঢ
            "\u006f": bn.letter_nna,  # \u006f -> o : ণ
            "\u0070": f"{bn.letter_nna}{bn.sign_virama}{bn.letter_nna}",  # \u0070 -> p : ণ্ণ
            "\u0071": f"{bn.letter_nna}{bn.sign_virama}{bn.letter_ttha}",  # \u0071 -> q : ণ্ঠ
            "\u0072": f"{bn.letter_nna}{bn.sign_virama}{bn.letter_dda}",  # \u0072 -> r : ণ্ড
            "\u0073": f"{bn.letter_nna}{bn.sign_virama}",  # \u0073 -> s : ণ্ #! Left as []
            "\u0074": bn.letter_ta,  # \u0074 -> t : ত
            "\u0075": f"{bn.letter_ta}{bn.sign_virama}{bn.letter_ma}",  # \u0075 -> u : ত্ম
            "\u0076": f"{bn.letter_ta}{bn.sign_virama}{bn.letter_ta}",  # \u0076 -> v : ত্ত
            "\u0076\u00a1\u00fb": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_ta}",  # \u0076\u00a1\u00fb -> v¡û : ক্ত
            "\u0077": f"{bn.letter_ta}{bn.sign_virama}{bn.letter_ta}{bn.sign_virama}{bn.letter_ba}",  # \u0077 -> w :ত্ত্ব
            "\u0078": f"{bn.letter_ta}{bn.sign_virama}{bn.letter_tha}",  # \u0078 -> x : ত্থ
            "\u0079": f"{bn.letter_ta}{bn.sign_virama}{bn.letter_ra}",  # \u0076 -> y : ত্র
            "\u0079\u00fb": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_ra}",  # \u0076\u00fb -> yû : ক্র
            "\u007a": f"{bn.sign_virama}{bn.letter_ta}",  # \u007a -> z : ্ত #! Down as [nt, st, str]
            "\u007b": f"{bn.vowel_i}{bn.sign_candrabindu}",  # \u007b -> { : িঁ
            "\u007c": f"{bn.sign_virama}{bn.letter_ta}{bn.sign_virama}{bn.letter_ra}",  # \u007c -> | : ্ত্র #! Down as [ntr, mtr, str]
            "\u0081": bn.letter_w,  # \u0081 -> (invisible) : ৱ #! \x81
            "\u008f": f"{bn.letter_na}{bn.sign_virama}{bn.letter_na}",  # \u008f ->  : ন্ন #! INVISIBLE
            "\u0090": f"{bn.letter_na}{bn.sign_virama}{bn.letter_sa}",  # \u0090 ->  : ন্স #! INVISIBLE
            "\u009d": f"{bn.letter_pa}{bn.sign_virama}{bn.letter_pa}",  # \u009d ->  : প্প #! INVISIBLE
            "\u00a3": f"{bn.sign_virama}{bn.letter_pha}",  # \u00a3 -> £ : ্ফ #! Ryt as [mf, lf]
            "\u00a4": bn.letter_ba,  # \u00a4 -> ¤ : ব
            "\u00a5": f"{bn.letter_ba}{bn.sign_virama}{bn.letter_tta}",  # \u00a5 -> ¥ : ব্ট
            "\u00a6": f"{bn.letter_ba}{bn.sign_virama}{bn.letter_da}",  # \u00a6 -> ¦ : ব্দ
            "\u00a7": f"{bn.letter_ba}{bn.sign_virama}{bn.letter_dha}",  # \u00a7 -> § : ব্ধ
            "\u00a8": f"{bn.letter_ba}{bn.sign_virama}{bn.letter_jha}",  # \u00a8 -> ¨ : ব্ঝ
            "\u00a9": f"{bn.letter_ba}{bn.sign_virama}{bn.letter_dda}",  # \u00a9 -> © : ব্ড
            "\u00aa": f"{bn.letter_ba}{bn.sign_virama}{bn.letter_ja}",  # \u00aa -> ª : ব্জ
            "\u00ab": f"{bn.sign_virama}{bn.letter_ba}",  # \u00ab -> « : ্ব #! Down as [tv, tw, sv, khv, thv]
            "\u00ac": f"{bn.sign_virama}{bn.letter_ba}",  # \u00ac -> ¬ : ্ব #! Down as [mb, sv]
            "\u00ae": bn.letter_bha,  # \u00ae -> ® : ভ
            "\u00af": f"{bn.letter_bha}{bn.sign_virama}{bn.letter_la}",  # \u00af -> ¯ : ভ্ল
            "\u00b0": f"{bn.letter_bha}{bn.sign_virama}{bn.letter_ra}",  # \u00b0 -> ° : ভ্র
            "\u00b1": f"{bn.sign_virama}{bn.letter_bha}",  # \u00b1 -> ± : ্ভ #! [mv]
            "\u00b2": f"{bn.sign_virama}{bn.letter_bha}{bn.sign_virama}{bn.letter_ra}",  # \u00b2 -> ² : ্ভ্র #! Down as []
            "\u00b3": bn.letter_ma,  # \u00b3 -> ³ : ম
            "\u00b4": f"{bn.letter_ma}{bn.sign_virama}",  # \u00b4 -> ´ : ম্ #! [mv]
            "\u00b5": f"{bn.sign_virama}{bn.letter_ma}",  # \u00b5 -> µ : ্ম #! [nm, lm, sm]
            "\u00b6": f"{bn.sign_virama}{bn.letter_ma}",  # \u00b6 -> ¶ : ্ম #! [mm, sm]
            "\u00b8": f"{bn.sign_virama}{bn.letter_ya}",  # \u00b8 -> ¸ : ্য #! [*many]
            "\u00b9": bn.letter_ra,  # \u00b9 -> ¹ : র
            "\u00ba": bn.letter_la,  # \u00ba -> º : ল
            "\u00bb": f"{bn.letter_la}{bn.sign_virama}{bn.letter_ka}",  # \u00bb -> » : ল্ক
            "\u00bc": f"{bn.letter_la}{bn.sign_virama}{bn.letter_ga}",  # \u00bc -> ¼ :  ল্গ
            "\u00bd": f"{bn.letter_la}{bn.sign_virama}{bn.letter_ga}{bn.vowel_u}",  # \u00bd -> ½ : ল্গু
            "\u00be": f"{bn.letter_la}{bn.sign_virama}{bn.letter_ba}",  # \u00be -> ¾ : ল্ব
            "\u00bf": f"{bn.letter_la}{bn.sign_virama}{bn.letter_pa}",  # \u00bf -> ¿ : ল্প
            "\u00c0": f"{bn.letter_la}{bn.sign_virama}{bn.letter_la}",  # \u00c0 -> À : ল্ল
            "\u00c1": f"{bn.letter_la}{bn.sign_virama}{bn.letter_dda}",  # \u00c1 -> Á : ল্ড
            "\u00c2": f"{bn.letter_la}{bn.sign_virama}",  # \u00c2 -> Â : ল্ #! Left as [lt, lm]
            "\u00c3": f"{bn.sign_virama}{bn.letter_la}",  # \u00c3 -> Ã : ্ল #! Down as [kl, gl, ml, pl, bl]
            "\u00c4": f"{bn.letter_la}{bn.sign_virama}",  # \u00c4 -> Ä : ল্ #! Left as [lf]
            "\u00c5": bn.letter_sha,  # \u00c5 -> Å : শ
            "\u00c6": f"{bn.letter_sha}{bn.sign_virama}",  # \u00c6 -> Æ : শ্ #! Left as [sm]
            "\u00c7": f"{bn.letter_sha}{bn.vowel_u}",  # \u00c7 -> Ç : শু
            "\u00c8": bn.letter_ssa,  # \u00c8 -> È : ষ
            "\u00c9": f"{bn.letter_ssa}{bn.sign_virama}{bn.letter_ba}",  # \u00c9 -> É : ষ্ব
            "\u00ca": f"{bn.letter_ssa}{bn.sign_virama}{bn.letter_tta}",  # \u00ca -> Ê : ষ্ট
            "\u00cb": f"{bn.letter_ssa}{bn.sign_virama}{bn.letter_ttha}",  # \u00cb -> Ë : ষ্ঠ
            "\u00cc": f"{bn.letter_ssa}{bn.sign_virama}{bn.letter_nna}",  # \u00cc -> Ì : ষ্ণ
            "\u00cd": f"{bn.letter_ssa}{bn.sign_virama}",  # \u00cd -> Í : ষ্ #! Up as []
            "\u00ce": bn.letter_sa,  # \u00ce -> Î : স
            "\u00cf": f"{bn.letter_sa}{bn.sign_virama}{bn.letter_kha}",  # \u00cf -> Ï : স্খ
            "\u00d0": f"{bn.letter_sa}{bn.sign_virama}{bn.letter_tta}",  # \u00d0 -> Ð : স্ট
            "\u00d1": f"{bn.letter_sa}{bn.sign_virama}",  # \u00d1 -> Ñ : স্ #! Left/Up as [sp, sk, sv, skr, st, sr]
            "\u00d2": bn.letter_h,  # \u00d2 -> Ò : হ
            "\u00d2\u00fc": bn.letter_i,  # \u00d2\u00fc -> Òü : ই
            "\u00d3": f"{bn.letter_h}{bn.sign_virama}{bn.letter_la}",  # \u00d3 -> Ó : হ্ল
            "\u00d4": f"{bn.letter_h}{bn.sign_virama}{bn.letter_ba}",  # \u00d4 -> Ô :  হ্ব
            "\u00d5": f"{bn.letter_h}{bn.sign_virama}{bn.letter_ma}",  # \u00d5 -> Õ : হ্ম
            "\u00d6": f"{bn.letter_h}{bn.sign_virama}{bn.letter_nna}",  # \u00d6 -> Ö : হ্ণ
            "\u00d7": f"{bn.letter_h}{bn.vowel_u}",  # \u00d7 -> × : হু
            "\u00d8": bn.letter_rra,  # \u00d8 -> Ø : ড়
            "\u00d9": bn.letter_rha,  # \u00d9 -> Ù : ঢ়
            "\u00da": bn.letter_yya,  # \u00da -> Ú : য়
            "\u00db": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_ssa}",  # \u00db -> Û : ক্ষ
            "\u00dc": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_ssa}{bn.sign_virama}{bn.letter_ma}",  # \u00dc -> Ü : ক্ষ্ম
            "\u00dd": f"{bn.letter_ka}{bn.sign_virama}{bn.letter_ssa}{bn.sign_virama}{bn.letter_na}",  # \u00dd -> Ý : ক্ষ্ন
            "\u00de\u00ea": f"{bn.letter_na}{bn.sign_virama}{bn.letter_dha}",  # \u00de\u00ea -> Þê : ন্ধ
            "\u00de\u00f8\u00fd": f"{bn.letter_na}{bn.sign_virama}{bn.letter_dha}{bn.sign_virama}{bn.letter_ra}",  # \u00de\u00f8\u00fd -> Þøý : ন্ধ্র
            "\u00df": f"{bn.letter_pa}{bn.sign_virama}{bn.letter_ra}",  # \u00df -> ß : প্র
            "\u00e0": bn.vowel_aa,  # \u00e0 -> à : া
            "\u00e1": bn.letter_cha,  # \u00e1 -> á : ছ
            "\u00e2": f"{bn.letter_ta}{bn.sign_virama}",  # \u00e2 -> â : ত্ #! UP as [tn, tv]
            "\u00e3": bn.vowel_ii,  # \u00e3 -> ã : ী #! sometimes followed by sp
            "\u00e4": f"{bn.letter_da}{bn.sign_virama}{bn.letter_da}{bn.sign_virama}{bn.letter_ba}",  # \u00e4 -> ä : দ্দ্ব
            "\u00e5": bn.vowel_u,  # \u00e5 -> å : ু
            "\u00e6": bn.vowel_u,  # \u00e6 -> æ : ু #! More Below - After combination
            "\u00e7": bn.vowel_u,  # \u00e7 -> ç :  ু #! On right
            "\u00e8": bn.vowel_uu,  # \u00e8 -> è :  ূ #! Check when followed by y
            "\u00e9": bn.vowel_uu,  # \u00e9 -> é : ূ #! NO occurence
            "\u00eb": bn.vowel_e,  # \u00eb -> ë : ে #! SP
            "\u00ec": bn.vowel_e,  # \u00ec -> ì : ে #! NOSP
            "\u00ed": bn.vowel_ai,  # \u00ed -> í : ৈ #! SP
            "\u00ee": bn.vowel_ai,  # \u00ee -> î : ৈ #! NOSP
            "\u00ef": bn.mark_au,  # \u00ef -> ï : ৗ
            "\u00f0": f"{bn.letter_ja}{bn.sign_virama}{bn.letter_ja}",  # \u00f0 -> ð :জ্জ
            "\u00f1": f"{bn.sign_virama}{bn.letter_ta}{bn.sign_virama}{bn.letter_ta}",  # \u00f1 -> ñ : ্ত্ত #! Down as [st-t]
            "\u00f2": f"\u00a2{bn.sign_virama}",  # \u00f2 -> ò : ্র #! MISUSED (\u0981 -> ঁ )
            "\u00f3": bn.letter_pha,  # \u00f3 -> ó : ফ
            "\u00f4": bn.sign_virama,  # \u00f4 -> ô : ্
            "\u00f5": bn.vowel_r_vocalic,  # \u00f5 -> õ : ৃ
            "\u00f6": f"{bn.sign_virama}{bn.letter_ra}",  # \u00f6 -> ö : ্র #! Down as [str, pr, dr, ptr]
            "\u00f7": f"{bn.sign_virama}{bn.letter_ra}",  # \u00f7 -> ÷ : ্র #! Down as [mr, sr]
            "\u00f8": f"{bn.sign_virama}{bn.letter_ra}",  # \u00f8 -> ø : ্র #! Down as [pr, khr, gr, dr, shr, br, fr]
            "\u00f9": f"{bn.sign_virama}{bn.letter_ra}",  # \u00f9 -> ù : ্র #! Down as []
            "\u00fa": " ",  # \u00fa -> ú : \u200c -> #! Actually cheikhei
            "\u0152": f"{bn.letter_dha}{bn.sign_virama}{bn.letter_ma}",  # \u0152 -> Œ :ধ্ম
            "\u0153": f"{bn.letter_pa}{bn.sign_virama}{bn.letter_ta}",  # \u0153 -> œ : প্ত
            "\u0160": f"{bn.letter_da}{bn.sign_virama}",  # \u0160 -> Š : দ্ #! Up as []
            "\u0161": bn.letter_pa,  # \u0022 -> š : প
            "\u0178": f"{bn.letter_pa}{bn.sign_virama}",  # \u0178 -> Ÿ : প্ #! Left as []
            "\u0192": bn.letter_da,  # \u0192 -> ƒ : দ
            "\u02c6": f"{bn.letter_da}{bn.sign_virama}{bn.letter_ma}",  # \u02c6 -> ˆ : দ্ম
            "\u02dc": bn.letter_r_vocalic,  # \u02dc -> ˜ : ঋ #! Unused
            "\u2013": f"{bn.letter_na}{bn.sign_virama}",  # \u2013 -> – : ন্ #! Left as [nd, nm, nt]
            "\u2014": f"{bn.sign_virama}{bn.letter_na}",  # \u2014 -> — : ্ন #! Left-Down as [kn, pn, mn, gn, tn]
            "\u201a": f"{bn.sign_virama}{bn.letter_tha}",  # \u201a -> ‚ : ্থ #! Down as [nth, sth]
            "\u201c": f"{bn.letter_na}{bn.sign_virama}{bn.letter_dda}",  # \u201c -> “ : ন্ড
            "\u201d": f"{bn.letter_na}{bn.sign_virama}",  # \u201d -> ” : ন্ #! Up as [nt, nth, ntr, ndr]
            "\u201e": f"{bn.letter_da}{bn.sign_virama}{bn.letter_da}",  # \u201e -> „ : দ্দ
            "\u2020": f"{bn.letter_da}{bn.sign_virama}{bn.letter_dha}{bn.sign_virama}{bn.letter_ba}",  # \u2020 -> † : দ্ধ্ব
            "\u2021": f"{bn.letter_da}{bn.sign_virama}{bn.letter_ba}",  # \u2021 -> ‡ : দ্ব
            "\u2021\u00fd": f"{bn.letter_da}{bn.sign_virama}{bn.letter_dha}",  # \u2021\u00fd -> ‡ý : দ্ধ
            "\u2022": f"{bn.sign_virama}{bn.letter_na}",  # \u2022 -> • : ্ন #! Down as [sn]
            "\u2026": f"{bn.vowel_ii}{bn.sign_candrabindu}",  # \u2026 -> … : ীঁ
            "\u2030": f"{bn.letter_da}{bn.sign_virama}{bn.letter_ra}",  # \u2030 -> ‰ : দ্র
            "\u2039": bn.letter_dha,  # \u2039 -> ‹ : ধ
            "\u203a": f"{bn.letter_pa}{bn.sign_virama}{bn.letter_sa}",  # \u203a -> › : প্স
            "\u2122": bn.letter_ya,  # \u2122 -> ™ : য
            "\u007d": bn.sign_anusvara,  # \u007d -> } : ং
        }

        self.postmap_vowels: Dict[str, str] = {
            f"{bn.vowel_e}{bn.vowel_aa}": bn.vowel_o,  # ে +  া :  ো
            f"{bn.vowel_e}{bn.mark_au}": bn.vowel_au,  # ে +  ৗ :  ৌ
        }

        self.R_char_r: Dict[str, str] = {
            "\u00a2": f"{bn.letter_ra}{bn.sign_virama}",  # \u00a2 -> ¢ : bn.letter_ra{bn.sign_virama} -> র্
        }

        self.s550_extra_chars: Set[str] = {
            "\u00a1",  #! \u00a1 -> ¡ : as joiner or space
            "\u00fc",  #! \u00fc -> ü : as top part of e or u
            "\u00ff",  #! \u00ff -> ÿ
            "\uf000",  #! \uf000 -> 
            "\u0040",  #! \u0040 -> @
            "\u003a",  #! -> :
            bn.sign_visarga,
        }
