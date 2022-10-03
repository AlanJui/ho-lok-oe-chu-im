# %%
import pandas as pd
import re

# ==========================================================
# 自漢字的「注音碼」，分析出：聲母、韻母、調號
# ==========================================================

siann_pattern = re.compile(r"(b|chh|ch|g|h|j|kh|k|l|m|ng|n|ph|p|s|th|t|q)")

def split_chu_im(chu_im):
    result = []

    siann_bu = siann_pattern.match(chu_im).group()
    un_bu = chu_im[len(siann_bu):len(chu_im)-1]
    diau = chu_im[len(chu_im)-1]

    result += [siann_bu]
    result += [un_bu]
    result += [diau]
    return result


# %%

# ==========================================================
# 韻母處理
# ==========================================================
un_mu_dict = {
    'un_code': ['a', 'ann', 'ah', 'ahnn', 'ai', 'ainn', 'ak', 'am', 'an', 'ang', 'ap', 'at', 'au', 'auh', 'e', 'enn', 'eh', 'ehnn', 'ek', 'eng', 'i', 'inn', 'ia', 'iann', 'iah', 'iannh', 'iak', 'iam', 'ian', 'iang', 'iap', 'iat', 'iau', 'iaunn', 'iauh', 'ih', 'im', 'in', 'io', 'ioh', 'iok', 'iong', 'ip', 'it', 'iu', 'iunn', 'iunnh', 'm', 'mh', 'ng', 'ngh', 'o', 'onn', 'oo', 'oa', 'oann', 'oah', 'oai', 'oainn', 'oan', 'oang', 'oat', 'oe', 'oenn', 'oeh', 'oh', 'onnh', 'ok', 'om', 'ong', 'u', 'uh', 'ui', 'un', 'ut'],
    'IPA': ['a', 'ã', 'a?', 'ã?', 'ai', 'ãĩ', 'ak̚', 'am', 'an', 'aŋ', 'ap̚', 'at̚', 'aʊ', 'au?', 'e', 'ẽ', 'e?', 'ẽ?', 'ik̚', 'ɪŋ', 'i', 'ĩ', 'ia', 'ĩã', 'ia?', 'iãh', 'iak̚', 'iam', 'ian', 'iaŋ', 'iap̚', 'iat̚', 'iaʊ', 'ĩãũ', 'iau?', 'i?', 'im', 'in', 'io', 'iə?', 'iɔk̚', 'iɔŋ', 'ip̚', 'it̚', 'iu', 'ĩũ', 'iũh', 'm̩', 'm̩h', 'ŋ̍', 'ŋ̍h', 'o', 'ɔ̃', 'ɔ', 'ua', 'ũã', 'ua?', 'uai', 'ũãĩ', 'uan', 'uaŋ', 'uat̚', 'ue', 'ũẽ', 'ue?', 'ə?', 'ɔ̃?', 'ɔk̚', 'ɔm', 'ɔŋ', 'u', 'u?', 'ui', 'un', 'ut̚'],
    'sip_ngoo_im': ['膠', '監', '膠', '監', '皆', '閒', '江', '甘', '干', '江', '甘', '干', '交', '交', '伽', '更', '伽', '更', '經', '經', '居', '梔', '迦', '驚', '迦', '驚', '姜', '兼', '堅', '姜', '兼', '堅', '嬌', '嘄', '嬌', '居', '金', '巾', '茄', '茄', '恭', '恭', '金', '巾', '丩', '牛', '牛', '姆', '姆', '鋼', '鋼', '高', '姑', '沽', '瓜', '官', '瓜', '乖', '閂', '觀', '光', '觀', '檜', '糜', '檜', '高', '姑', '公', '箴', '公', '艍', '艍', '規', '君', '君'],
    'POJ': ['a', 'aⁿ', 'ah', 'ahⁿ', 'ai', 'aiⁿ', 'ak', 'am', 'an', 'ang', 'ap', 'at', 'au', 'auh', 'e', 'eⁿ', 'eh', 'ehⁿ', 'ek', 'eng', 'i', 'iⁿ', 'ia', 'iaⁿ', 'iah', 'iahⁿ', 'iak', 'iam', 'ian', 'iang', 'iap', 'iat', 'iau', 'iauⁿ', 'iauh', 'ih', 'im', 'in', 'io', 'ioh', 'iok', 'iong', 'ip', 'it', 'iu', 'iuⁿ', 'iuhⁿ', 'm', 'mh', 'ng', 'ngh', 'o', 'oⁿ', 'o͘', 'oa', 'oaⁿ', 'oah', 'oai', 'oaiⁿ', 'oan', 'oang', 'oat', 'oe', 'oenn', 'oeh', 'oh', 'ohⁿ', 'ok', 'om', 'ong', 'u', 'uh', 'ui', 'un', 'ut'],
    'TL': ['a', 'ann', 'ah', 'annh', 'ai', 'ainn', 'ak', 'am', 'an', 'ang', 'ap', 'ap', 'au', 'auh', 'e', 'enn', 'eh', 'ennh', 'ik', 'ing', 'i', 'inn', 'ia', 'iann', 'iah', 'iannh', 'iak', 'iam', 'ian', 'iang', 'iap', 'iat', 'iau', 'iaunn', 'iauh', 'ih', 'im', 'in', 'io', 'ioh', 'iok', 'iong', 'ip', 'it', 'iu', 'iunn', 'iunnh', 'm', 'mh', 'ng', 'ngh', 'o', 'onn', 'oo', 'ua', 'uann', 'uah', 'uai', 'uainn', 'uan', 'uang', 'uat', 'ue', 'uenn', 'ueh', 'oh', 'onnh', 'ok', 'om', 'ong', 'u', 'uh', 'ui', 'un', 'ut'],
    'BP': ['a', 'na', 'ah', 'nah', 'ai', 'nai', 'ak', 'am', 'an', 'ang', 'ap', 'at', 'ao', 'aoh', 'e', 'ne', 'eh', 'neh', 'ik', 'ing', 'i', 'ni', 'ia', 'nia', 'iah', 'niah', 'iak', 'iam', 'ian', 'iang', 'iap', 'iat', 'iao', 'niao', 'iaoh', 'ih', 'im', 'in', 'io', 'ioh', 'iok', 'iong', 'ip', 'it', 'iu', 'niu', 'niuh', 'm', 'mh', 'ng', 'ngh', 'o', 'noo', 'oo', 'ua', 'nua', 'uah', 'uai', 'nuai', 'uan', 'uang', 'uat', 'ue', 'nue', 'ueh', 'oh', 'nooh', 'ok', 'om', 'ong', 'u', 'uh', 'ui', 'un', 'ut'],
    'TPS': ['ㄚ', 'ㆩ', 'ㄚㆷ', 'ㆩㆷ', 'ㄞ', 'ㆮ', 'ㄚㆻ', 'ㆰ', 'ㄢ', 'ㄤ', 'ㄚㆴ', 'ㄚㆵ', 'ㄠ', 'ㄠㆷ', 'ㆤ', 'ㆥ', 'ㆤㆷ', 'ㆥㆷ', 'ㄧㆻ', 'ㄧㄥ', 'ㄧ', 'ㆪ', 'ㄧㄚ', 'ㄧㆩ', 'ㄧㄚㆷ', 'ㄧㆩㆷ', 'ㄧㄚㆻ', 'ㄧㆰ', 'ㄧㄢ', 'ㄧㄤ', 'ㄧㄚㆴ', 'ㄧㄚㆵ', 'ㄧㄠ', 'ㄧㆯ', 'ㄧㄠㆷ', 'ㄧㆷ', 'ㄧㆬ', 'ㄧㄣ', 'ㄧㄜ', 'ㄧㄜㆷ', 'ㄧㆦㆻ', 'ㄧㆲ', 'ㄧㆴ', 'ㄧㆵ', 'ㄧㄨ', 'ㄧㆫ', 'ㄧㆫㆷ', 'ㆬ', 'ㆬㆷ', 'ㆭ', 'ㆭㆷ', 'ㄜ', 'ㆧ', 'ㆦ', 'ㄨㄚ', 'ㄨㆩ', 'ㄨㄚㆷ', 'ㄨㄞ', 'ㄨㆮ', 'ㄨㄢ', 'ㄨㄤ', 'ㄨㄚㆵ', 'ㄨㆤ', 'ㄨㆥ', 'ㄨㆤㆷ', 'ㄜㆷ', 'ㆧㆷ', 'ㆦㆻ', 'ㆱ', 'ㆲ', 'ㄨ', 'ㄨㆷ', 'ㄨㄧ', 'ㄨㄣ', 'ㄨㆵ'],
    'sip_ngoo_im_id': ['28', '26', '28', '26', '16', '40', '21', '19', '6', '21', '19', '6', '23', '23', '39', '31', '39', '31', '9', '9', '29', '34', '24', '36', '24', '36', '18', '22', '2', '18', '22', '2', '12', '46', '12', '29', '3', '17', '33', '33', '14', '14', '3', '17', '30', '50', '50', '42', '42', '38', '38', '15', '41', '11', '20', '37', '20', '8', '44', '10', '43', '10', '25', '45', '25', '15', '41', '7', '47', '7', '27', '27', '4', '1', '1'],
}
df_un_bu = pd.DataFrame(un_mu_dict)

# 自 DataFrame 取出，欄標題名為：un_code 的部份，並將之轉換成 list
un_list = df_un_bu["un_code"].values.tolist()
sip_ngoo_im_un_mu_list = df_un_bu["sip_ngoo_im_id"].values.tolist()

# ==========================================================
# 找韻母的「索引編號」
# ==========================================================

def get_un_idx(un_bu):
    try:
        un_idx = un_list.index(un_bu)
    except ValueError:
        un_idx = -1
        print(f'Un-bu: {un_bu} does not exist')

    return un_idx

def get_sip_ngoo_im_idx(un_bu_index):
    try:
        sip_ngoo_im_idx = int(sip_ngoo_im_un_mu_list[un_bu_index])
    except ValueError:
        sip_ngoo_im_idx = -1
        print(f'Sip-Ngoo-Im-Un-Bu Index: "{un_bu_index}" does not exist')

    return sip_ngoo_im_idx


# %%

# ==========================================================
# 聲母處理
# ==========================================================
siann_bu_dict = {
    'siann_code': ['b', 'ch', 'chh', 'g', 'h', 'j', 'k', 'kh', 'l', 'm', 'n', 'ng', 'p', 'ph', 's', 't', 'th', 'q'],
    'IPA': ['b', 'ʦ', 'ʦʰ', 'ɡ', 'h', 'ʣ', 'k', 'kʰ', 'l', 'm', 'n', 'ŋ', 'p', 'pʰ', 's', 't', 'tʰ', ' '],
    'sip_ngoo_im': ['門', '曾', '出', '語', '喜', '入', '求', '去', '柳', '毛', '耐', '雅', '邊', '頗', '時', '地', '他', '英'],
    'POJ': ['b', 'ch', 'chh', 'g', 'h', 'j', 'k', 'kh', 'l', 'm', 'n', 'ng', 'p', 'ph', 's', 't', 'th', ' '],
    'TL': ['b', 'ts', 'tsh', 'g', 'h', 'j', 'k', 'kh', 'l', 'm', 'n', 'ng', 'p', 'ph', 's', 't', 'th', ' '],
    'BP': ['bb', 'z', 'c', 'gg', 'h', 'zz', 'g', 'k', 'l', 'bbn', 'ln', 'ggn', 'b', 'p', 's', 'd', 't', ' '],
    'TPS': ['ㆠ', 'ㄗ', 'ㄘ', 'ㆣ', 'ㄏ', 'ㆡ', 'ㄍ', 'ㄎ', 'ㄌ', 'ㄇ', 'ㄋ', 'ㄫ', 'ㄅ', 'ㄆ', 'ㄙ', 'ㄉ', 'ㄊ', ' '],
}
df_siann_bu = pd.DataFrame(siann_bu_dict)

# 自 DataFrame 取出，欄標題名為：siann_code 的部份，並將之轉換成 list
siann_list = df_siann_bu["siann_code"].values.tolist()

# ==========================================================
# 找聲母的「索引編號」
# ==========================================================

def get_siann_idx(siann_bu):
    siann_idx = siann_list.index(siann_bu)

    return siann_idx


# %%
# 將字串轉換成 List
# Python code to convert string to list character-wise
def convert_string_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


# %%
# ==========================================================
# 十五音注音
# ==========================================================

sip_ngoo_im_tiau_dict = {
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    7: "七",
    8: "八",
}

def get_sip_ngoo_im_un_bu(idx):
    # return df_un_bu["sip_ngoo_im"].values.tolist()[idx]
    return df_un_bu["sip_ngoo_im"][idx]

def get_sip_ngoo_im_siann_bu(idx):
    return df_siann_bu["sip_ngoo_im"][idx]

def get_sip_ngoo_im_tiau_ho(idx):
    return sip_ngoo_im_tiau_dict[idx]

def get_sip_ngoo_im_chu_im(siann_idx, un_idx, tiau_ho):
    sni_un = get_sip_ngoo_im_un_bu(un_idx)
    sni_tiau = get_sip_ngoo_im_tiau_ho(int(tiau_ho))
    sni_siann = get_sip_ngoo_im_siann_bu(siann_idx)

    return (f"{sni_un}{sni_tiau}{sni_siann}")

# %%
# ==========================================================
# 方音符號(TPS)
# ==========================================================


TPS_mapping_dict = {
    'p': 'ㆴ˙',
    't': 'ㆵ˙',
    'k': 'ㆻ˙',
    'h': 'ㆷ˙',
}

TPS_remap_dict = {
    'ㄗㄧ': 'ㄐㄧ',
    'ㄘㄧ': 'ㄑㄧ',
    'ㄙㄧ': 'ㄒㄧ',
    'ㆡㄧ': 'ㆢㄧ',
}

TPS_tiau_dict = {
    1: "",
    2: "ˋ",
    3: "˪",
    4: "",
    5: "ˊ",
    7: "˫",
    8: "\u02D9",
}

def get_TPS_un_bu(idx):
    # return df_un_bu["TPS"].values.tolist()[idx]
    return df_un_bu["TPS"][idx]

def get_TPS_siann_bu(idx):
    return df_siann_bu["TPS"][idx]

def get_TPS_tiau_ho(idx):
    return TPS_tiau_dict[idx]

def get_TPS_chu_im(siann_idx, un_idx, tiau_ho):
    sni_un = get_TPS_un_bu(un_idx)
    sni_tiau = get_TPS_tiau_ho(int(tiau_ho))
    sni_siann = get_TPS_siann_bu(siann_idx)

    TPS_chu_im = f"{sni_siann}{sni_un}{sni_tiau}"

    pattern = r"(ㄗㄧ|ㄘㄧ|ㄙㄧ|ㆡㄧ)"
    searchObj = re.search(pattern, TPS_chu_im, re.M | re.I)
    if searchObj:
        key_value = searchObj.group(1)
        TPS_chu_im = TPS_chu_im.replace(key_value,
                                        TPS_remap_dict[key_value])

    return TPS_chu_im


# %%
"""
白話字（POJ）
順序：《o＞e＞a＞u＞i＞ng＞m》；而 ng 標示在字母 n 上。
例外
oai、oan、oat、oah 標在 a 上。
oeh 標在 e 上。
"""
pattern1 = r"(oai|oan|oah|oeh)"
pattern2 = r"(o|e|a|u|i|ng|m)"

POJ_tiau_dict = {
    'a1': 'a',
    'a2': 'á',
    'a3': 'à',
    'a4': 'a',
    'a5': 'â',
    'a7': 'ā',
    'a8': 'a̍',
    'e1': 'e',
    'e2': 'é',
    'e3': 'è',
    'e4': 'e',
    'e5': 'ê',
    'e7': 'ē',
    'e8': 'e̍',
    'i1': 'i',
    'i2': 'í',
    'i3': 'ì',
    'i4': 'i',
    'i5': 'î',
    'i7': 'ī',
    'i8': 'i̍',
    'o1': 'o',
    'o2': 'ó',
    'o3': 'ò',
    'o4': 'o',
    'o5': 'ô',
    'o7': 'ō',
    'o8': 'o̍',
    'u1': 'u',
    'u2': 'ú',
    'u3': 'ù',
    'u4': 'u',
    'u5': 'û',
    'u7': 'ū',
    'u8': 'u̍',
    'n1': 'u',
    'n2': 'ú',
    'n3': 'ù',
    'n4': 'u',
    'n5': 'û',
    'n7': 'ū',
    'n8': 'u̍',
    'n1': 'u',
    'n2': 'ú',
    'n3': 'ù',
    'n4': 'u',
    'n5': 'û',
    'n7': 'ū',
    'u8': 'u̍',
    'n1': 'n',
    'n2': 'ń',
    'n3': 'ǹ',
    'n4': 'n',
    'n5': 'n̂',
    'n7': 'n̄',
    'n8': 'n̍',
    'm1': 'm',
    'm2': 'ḿ',
    'm3': 'm̀',
    'm4': 'm',
    'm5': 'm̌',
    'm7': 'm̄',
    'm8': 'm̍',
}

def get_POJ_un_bu(idx):
    return df_un_bu["POJ"][idx]

def get_POJ_siann_bu(idx):
    return df_siann_bu["POJ"][idx]

def get_POJ_tiau_ho(goan_im, idx):
    goan_im_idx = f"{goan_im}{idx}"
    return POJ_tiau_dict[goan_im_idx]

def get_POJ_chu_im(siann_idx, un_idx, tiau):
    un = get_POJ_un_bu(un_idx)
    siann = get_POJ_siann_bu(siann_idx)

    POJ_chu_im = f"{siann}{un}"

    # pattern1 = r"(oai|oan|oah|oeh)"
    searchObj = re.search(pattern1, POJ_chu_im, re.M | re.I)
    if searchObj:
        goan_im = searchObj.group(1)[1]
        POJ_chu_im = POJ_chu_im.replace(goan_im,
                                        get_POJ_tiau_ho(goan_im, tiau))
    else:
        # pattern2 = r"(o|e|a|u|i|ng|m)"
        searchObj2 = re.search(pattern2, POJ_chu_im, re.M | re.I)
        if searchObj2:
            goan_im = searchObj2.group(1)
            if goan_im != "ng":
                POJ_chu_im = POJ_chu_im.replace(goan_im,
                                                get_POJ_tiau_ho(goan_im, tiau))
            else:
                POJ_chu_im = POJ_chu_im.replace("n",
                                                get_POJ_tiau_ho(goan_im, tiau))

    return POJ_chu_im


# %%
"""
閩拼（BP）

【調號標示規則】

當一個音節有多個字母時，調號得標示在響度最大的字母上面（通常在韻腹）。由規則可以判定確切的字母：

 - 響度優先順序： a > oo > (e = o) > (i = u)〈低元音 > 高元音 > 無擦通音 > 擦音 > 塞音〉
 - 二合字母 iu 及 ui ，調號都標在後一個字母上；因為前一個字母是介音。
 - m 作韻腹時則標於字母 m 上。
 - 二合字母 oo 及 ng，標於前一個字母上；比如 ng 標示在字母 n 上。
 - 三合字母 ere，標於最後的字母 e 上。
"""

# 將「傳統八聲調」轉換成閩拼使用的調號
BP_tiau_remap_dict = {
    1: 1,  # 陰平: 44
    2: 3,  # 上聲：53
    3: 5,  # 陰去：21
    4: 7,  # 上聲：53
    5: 2,  # 陽平：24
    7: 6,  # 陰入：3?
    8: 8,  # 陽入：4?
}

pattern = r"[a|oo|ere|(iu|ui)|(e|o)|(i|u)|ng|m]"

BP_tiau_hu_dict = {
    1: "\u0304",    # 陰平
    2: "\u0341",    # 陽平
    3: "\u030C",    # 上声
    5: "\u0340",    # 陰去
    6: "\u0302",    # 陽去
    7: "\u0304",    # 陰入
    8: "\u0341",    # 陽入
}

BP_tiau_dict = {
    'a1': 'ā',
    'a2': 'á',
    'a3': 'ǎ',
    'a5': 'à',
    'a6': 'â',
    'a7': 'ā',
    'a8': 'á',
    'e1': 'ē',
    'e2': 'é',
    'e3': 'ě',
    'e5': 'è',
    'e6': 'ê',
    'e7': 'ē',
    'e8': 'é',
    'i1': 'ī',
    'i2': 'í',
    'i3': 'ǐ',
    'i5': 'ì',
    'i6': 'î',
    'i7': 'ī',
    'i8': 'í',
    'o1': 'ō',
    'o2': 'ó',
    'o3': 'ǒ',
    'o5': 'ò',
    'o6': 'ô',
    'o7': 'ō',
    'o8': 'ó',
    'u1': 'ū',
    'u2': 'ú',
    'u3': 'ǔ',
    'u5': 'ù',
    'u6': 'û',
    'u7': 'ū',
    'u8': 'ú',
    'n1': 'n̄',
    'n2': 'ń',
    'n3': 'ň',
    'n5': 'ǹ',
    'n6': 'n̂',
    'n7': 'n̄',
    'n8': 'ń',
    'm1': 'm̄',
    'm2': 'ḿ',
    'm3': 'm̌',
    'm5': 'm̀',
    'm6': 'm̂',
    'm7': 'm̄',
    'm8': 'ḿ',
}

def get_BP_un_bu(idx):
    return df_un_bu["BP"][idx]

def get_BP_siann_bu(idx):
    return df_siann_bu["BP"][idx]

def get_BP_tiau_remap(tiau_ho):
    return BP_tiau_remap_dict[int(tiau_ho)]

def get_BP_tiau_hu(goan_im, BP_tiau):
    goan_im_idx = f"{goan_im}{BP_tiau}"
    return BP_tiau_dict[goan_im_idx]

def get_BP_chu_im_simple(siann_idx, un_idx, tiau):
    un = get_BP_un_bu(un_idx)
    siann = get_BP_siann_bu(siann_idx)
    # 將「傳統八聲調」轉換成閩拼使用的調號
    BP_tiau = get_BP_tiau_remap(tiau)

    BP_chu_im = f"{siann}{un}{BP_tiau}"

    return BP_chu_im

def get_BP_chu_im(siann_idx, un_idx, tiau):
    un = get_BP_un_bu(un_idx)
    siann = get_BP_siann_bu(siann_idx)
    # 將「傳統八聲調」轉換成閩拼使用的調號
    BP_tiau = get_BP_tiau_remap(int(tiau))

    BP_chu_im = f"{siann}{un}"

    # pattern = r"[a|oo|ere|(iu|ui)|(e|o)|(i|u)|ng|m]"
    searchObj = re.search(pattern, BP_chu_im, re.M | re.I)
    if searchObj:
        found = searchObj.group(1)
        if found == "iu":
            BP_chu_im = BP_chu_im.replace("u", get_BP_tiau_hu(found, BP_tiau))
        elif found == "ui":
            BP_chu_im = BP_chu_im.replace("i", get_BP_tiau_hu(found, BP_tiau))
        elif found == "oo":
            tiau_hu = get_BP_tiau_hu("o", BP_tiau)
            to_be_replaced = f"o{tiau_hu}"
            BP_chu_im = BP_chu_im.replace(found, to_be_replaced)
        elif found == "ere":
            tiau_hu = get_BP_tiau_hu("e", BP_tiau)
            to_be_replaced = f"er{tiau_hu}"
            BP_chu_im = BP_chu_im.replace(found, to_be_replaced)
        elif found == "ng":
            tiau_hu = get_BP_tiau_hu("n", BP_tiau)
            to_be_replaced = f"{tiau_hu}g"
            BP_chu_im = BP_chu_im.replace(found, to_be_replaced)
        else:
            BP_chu_im = BP_chu_im.replace(found, get_BP_tiau_hu(found, BP_tiau))

    return BP_chu_im


# %%
"""
羅馬拼音（TL）
順序：《o＞e＞a＞u＞i＞ng＞m》；而 ng 標示在字母 n 上。
"""
pattern = r"(o|e|a|u|i|ng|m)"

TL_tiau_dict = {
    'a1': 'a',
    'a2': 'á',
    'a3': 'à',
    'a4': 'a',
    'a5': 'â',
    'a7': 'ā',
    'a8': 'a̍',
    'e1': 'e',
    'e2': 'é',
    'e3': 'è',
    'e4': 'e',
    'e5': 'ê',
    'e7': 'ē',
    'e8': 'e̍',
    'i1': 'i',
    'i2': 'í',
    'i3': 'ì',
    'i4': 'i',
    'i5': 'î',
    'i7': 'ī',
    'i8': 'i̍',
    'o1': 'o',
    'o2': 'ó',
    'o3': 'ò',
    'o4': 'o',
    'o5': 'ô',
    'o7': 'ō',
    'o8': 'o̍',
    'u1': 'u',
    'u2': 'ú',
    'u3': 'ù',
    'u4': 'u',
    'u5': 'û',
    'u7': 'ū',
    'u8': 'u̍',
    'n1': 'u',
    'n2': 'ú',
    'n3': 'ù',
    'n4': 'u',
    'n5': 'û',
    'n7': 'ū',
    'n8': 'u̍',
    'n1': 'u',
    'n2': 'ú',
    'n3': 'ù',
    'n4': 'u',
    'n5': 'û',
    'n7': 'ū',
    'u8': 'u̍',
    'n1': 'n',
    'n2': 'ń',
    'n3': 'ǹ',
    'n4': 'n',
    'n5': 'n̂',
    'n7': 'n̄',
    'n8': 'n̍',
    'm1': 'm',
    'm2': 'ḿ',
    'm3': 'm̀',
    'm4': 'm',
    'm5': 'm̌',
    'm7': 'm̄',
    'm8': 'm̍',
}

def get_TL_un_bu(idx):
    return df_un_bu["TL"][idx]

def get_TL_siann_bu(idx):
    return df_siann_bu["TL"][idx]

def get_TL_tiau_ho(goan_im, idx):
    goan_im_idx = f"{goan_im}{idx}"
    return TL_tiau_dict[goan_im_idx]

def get_TL_chu_im(siann_idx, un_idx, tiau):
    un = get_TL_un_bu(un_idx)
    siann = get_TL_siann_bu(siann_idx)

    TL_chu_im = f"{siann}{un}"

    # pattern = r"(o|e|a|u|i|ng|m)"
    searchObj = re.search(pattern, TL_chu_im, re.M | re.I)
    if searchObj:
        goan_im = searchObj.group(1)
        if goan_im != "ng":
            TL_chu_im = TL_chu_im.replace(goan_im,
                                          get_TL_tiau_ho(goan_im, tiau))
        else:
            TL_chu_im = TL_chu_im.replace("n",
                                          get_TL_tiau_ho(goan_im, tiau))
    return TL_chu_im


# %%
# chu_im = "nga2"
# chu_im = "chhian5"
han_ji = "昧"
chu_im = "boenn2"
result = split_chu_im(chu_im)

siann_bu = result[0]    # siann
un_bu = result[1]    # un
tiau_ho = result[2]   # tiau

idx1 = get_siann_idx(siann_bu)
idx2 = get_un_idx(un_bu)
idx3 = get_sip_ngoo_im_idx(idx2)

sni_un = get_sip_ngoo_im_un_bu(idx2)
sni_tiau = get_sip_ngoo_im_tiau_ho(int(tiau_ho))
sni_siann = get_sip_ngoo_im_siann_bu(idx1)
print(f"漢字：{han_ji} ==> 注音碼：{chu_im} ==> 十五音注音：{sni_un}{sni_tiau}{sni_siann}")

TPS_chu_im = get_TPS_chu_im(idx1, idx2, tiau_ho)
print(f"漢字：{han_ji} ==> 注音碼：{chu_im} ==> 卜音注音：{TPS_chu_im}")

# %%
"""
方音符號測試案例
"""
han_ji = "相"
chu_im = "siong1"
result = split_chu_im(chu_im)

siann_bu = result[0]    # siann
un_bu = result[1]    # un
tiau_ho = result[2]   # tiau

siann_idx = get_siann_idx(siann_bu)
un_idx = get_un_idx(un_bu)
sip_ngoo_im_idx = get_sip_ngoo_im_idx(un_idx)

TPS_chu_im = get_TPS_chu_im(siann_idx, un_idx, tiau_ho)
print(f"漢字：{han_ji} ==> 注音碼：{chu_im} ==> 方音注音：{TPS_chu_im}")

# %%
"""
白話字測試案例
"""
han_ji = "南"
chu_im = "lam5"
result = split_chu_im(chu_im)

siann_bu = result[0]    # siann
un_bu = result[1]    # un
tiau_ho = result[2]   # tiau

siann_idx = get_siann_idx(siann_bu)
un_idx = get_un_idx(un_bu)
sip_ngoo_im_idx = get_sip_ngoo_im_idx(un_idx)

POJ_chu_im = get_POJ_chu_im(siann_idx, un_idx, tiau_ho)
print(f"漢字：{han_ji} ==> 注音碼：{chu_im} ==> 白話字拼音：{POJ_chu_im}")

# %%
"""
羅馬拼音測試案例
"""
han_ji_dict = {
    "鏢": "pio1",
    "語": "gi2",
    "欠": "khiam3",
    "德": "tek4",
    "元": "goan5",
    "字": "ji7",
    "俗": "siok8",
}

for han_ji in han_ji_dict:
    chu_im = han_ji_dict[han_ji]
    result = split_chu_im(chu_im)

    siann_bu = result[0]    # siann
    un_bu = result[1]    # un
    tiau_ho = result[2]   # tiau

    siann_idx = get_siann_idx(siann_bu)
    un_idx = get_un_idx(un_bu)
    sip_ngoo_im_idx = get_sip_ngoo_im_idx(un_idx)

    TL_chu_im = get_TL_chu_im(siann_idx, un_idx, tiau_ho)
    print(f"漢字：{han_ji} ==> 注音碼：{chu_im} ==> 羅馬拼音：{TL_chu_im}")

# %%
"""
閩拼測試案例
"""
han_ji_dict = {
    "鏢": "pio1",
    "語": "gi2",
    "欠": "khiam3",
    "德": "tek4",
    "元": "goan5",
    "字": "ji7",
    "俗": "siok8",
    "聲": "siann1",
    "生": "chhinn1"
}

for han_ji in han_ji_dict:
    chu_im = han_ji_dict[han_ji]
    result = split_chu_im(chu_im)

    siann_bu = result[0]    # siann
    un_bu = result[1]    # un
    tiau_ho = result[2]   # tiau

    siann_idx = get_siann_idx(siann_bu)
    un_idx = get_un_idx(un_bu)

    # BP_chu_im = get_BP_chu_im_simple(siann_idx, un_idx, tiau_ho)
    BP_chu_im = get_BP_chu_im(siann_idx, un_idx, tiau_ho)
    print(f"漢字：{han_ji} ==> 注音碼：{chu_im} ==> 閩拼：{BP_chu_im}")
