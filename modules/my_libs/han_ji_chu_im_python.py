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
    'un_code': ['un', 'ut', 'ian', 'iat', 'im', 'ip', 'ui', 'uih', 'ee', 'eeh', 'an', 'at', 'ong', 'ok', 'oai', 'oaih', 'eng', 'ek', 'oan', 'oat', 'oo', 'ooh', 'iau', 'iauh', 'ei', 'eih', 'iong', 'iok', 'o', 'oh', 'ai', 'aih', 'in', 'it', 'iang', 'iak', 'am', 'ap', 'oa', 'oah', 'ang', 'ak', 'iam', 'iap', 'au', 'auh', 'ia', 'iah', 'oe', 'oeh', 'ann', 'ahnn', 'u', 'uh', 'a', 'ah', 'i', 'ih', 'iu', 'iuh', 'enn', 'ehnn', 'uinn', 'uinnh', 'io', 'ioh', 'inn', 'ihnn', 'ionn', 'ionnh', 'iann', 'iannh', 'oann', 'oannh', 'ng', 'ngh', 'e', 'eh', 'ainn', 'ainnh', 'onn', 'onnh', 'm', 'mh', 'oang', 'oak', 'oainn', 'oaihnn', 'oenn', 'oennh', 'iaunn', 'iauhnn', 'om', 'op', 'aunn', 'aunnh', 'onn', 'ohnn', 'iunn', 'iunnh'],
    'IPA': ['un', 'ut̚', 'ian', 'iat̚', 'im', 'ip̚', 'ui', 'ui?', 'ɛ', 'ɛ?', 'an', 'at̚', 'ɔŋ', 'ɔk̚', 'uai', 'uai?', 'ɪŋ', 'ik̚', 'uan', 'uat̚', 'ɔ', 'ɔu?', 'iaʊ', 'iau?', 'ei', 'ei?', 'iɔŋ', 'iɔk̚', 'o', 'ə?', 'ai', 'ai?', 'in', 'it̚', 'iaŋ', 'iak̚', 'am', 'ap̚', 'ua', 'ua?', 'aŋ', 'ak̚', 'iam', 'iap̚', 'aʊ', 'au?', 'ia', 'ia?', 'ue', 'ue?', 'ã', 'ã?', 'u', 'u?', 'a', 'a?', 'i', 'i?', 'iu', 'iu?', 'ẽ', 'ẽ?', 'ũĩ', 'ũĩ?', 'io', 'iə?', 'ĩ', 'ĩ?', 'ĩɔ̃', 'ĩɔ̃?', 'ĩã', 'iãh', 'ũã', 'ũã?', 'ŋ̍', 'ŋ̍h', 'e', 'e?', 'ãĩ', 'ãĩ?', 'ɔ̃', 'ɔ̃?', 'm̩', 'm̩h', 'uaŋ', 'uak̚', 'ũãĩ', 'uãĩ?', 'ũẽ', 'ũẽ?', 'ĩãũ', 'ĩãũ?', 'ɔm', 'ɔp̚', 'ãũ', 'ãũ?', 'õ', 'õh', 'ĩũ', 'iũh'],
    'sip_ngoo_im': ['君', '君', '堅', '堅', '金', '金', '規', '規', '嘉', '嘉', '干', '干', '公', '公', '乖', '乖', '經', '經', '觀', '觀', '沽', '沽', '嬌', '嬌', '稽', '稽', '恭', '恭', '高', '高', '皆', '皆', '巾', '巾', '姜', '姜', '甘', '甘', '瓜', '瓜', '江', '江', '兼', '兼', '交', '交', '迦', '迦', '檜', '檜', '監', '監', '艍', '艍', '膠', '膠', '居', '居', '丩', '丩', '更', '更', '褌', '褌', '茄', '茄', '梔', '梔', '薑', '薑', '驚', '驚', '官', '官', '鋼', '鋼', '伽', '伽', '閒', '閒', '姑', '姑', '姆', '姆', '光', '光', '閂', '閂', '糜', '糜', '嘄', '嘄', '箴', '箴', '爻', '爻', '扛', '扛', '牛', '牛'],
    'POJ': ['un', 'ut', 'ian', 'iat', 'im', 'ip', 'ui', 'uih', 'ee', 'eeh', 'an', 'at', 'ong', 'ok', 'oai', 'oaih', 'eng', 'ek', 'oan', 'oat', 'o͘', 'o͘h', 'iau', 'iauh', 'ei', 'eih', 'iong', 'iok', 'o', 'oh', 'ai', 'aih', 'in', 'it', 'iang', 'iak', 'am', 'ap', 'oa', 'oah', 'ang', 'ak', 'iam', 'iap', 'au', 'auh', 'ia', 'iah', 'oe', 'oeh', 'aⁿ', 'ahⁿ', 'u', 'uh', 'a', 'ah', 'i', 'ih', 'iu', 'iuh', 'eⁿ', 'ehⁿ', 'uiⁿ', 'uihⁿ', 'io', 'ioh', 'iⁿ', 'iⁿh', 'ioⁿ', 'iohⁿ', 'iaⁿ', 'iahⁿ', 'oaⁿ', 'oahⁿ', 'ng', 'ngh', 'e', 'eh', 'aiⁿ', 'aihⁿ', 'oⁿ', 'ohⁿ', 'm', 'mh', 'oang', 'oak', 'oaiⁿ', 'oaiⁿh', 'oeⁿ', 'oehⁿ', 'iauⁿ', 'iauⁿh', 'om', 'op', 'auⁿ', 'auhⁿ', 'oⁿ', 'ohⁿ', 'iuⁿ', 'iuhⁿ'],
    'TL': ['un', 'ut', 'ian', 'iat', 'im', 'ip', 'ui', 'uih', 'ee', 'eh', 'an', 'ap', 'ong', 'ok', 'uai', 'uaih', 'ing', 'ik', 'uan', 'uat', 'oo', 'ooh', 'iau', 'iauh', 'e', 'eh', 'iong', 'iok', 'o', 'oh', 'ai', 'aih', 'in', 'it', 'iang', 'iak', 'am', 'ap', 'ua', 'uah', 'ang', 'ak', 'iam', 'iap', 'au', 'auh', 'ia', 'iah', 'ue', 'ueh', 'ann', 'annh', 'u', 'uh', 'a', 'ah', 'i', 'ih', 'iu', 'iuh', 'enn', 'ennh', 'uinn', 'uinnh', 'io', 'ioh', 'inn', 'innh', 'ionn', 'ionnh', 'iann', 'iannh', 'uann', 'uannh', 'ng', 'ngh', 'e', 'eh', 'ainn', 'ainnh', 'onn', 'onnh', 'm', 'mh', 'uang', 'uak', 'uainn', 'uainnh', 'uenn', 'uennh', 'iaunn', 'iaunnh', 'om', 'op', 'aunn', 'aunnh', 'onn', 'onnh', 'iunn', 'iunnh'],
    'BP': ['un', 'ut', 'ian', 'iat', 'im', 'ip', 'ui', 'uih', 'e', 'eh', 'an', 'at', 'ong', 'ok', 'uai', 'uaih', 'ing', 'ik', 'uan', 'uat', 'oo', 'ooh', 'iao', 'iaoh', 'e', 'eh', 'iong', 'iok', 'o', 'oh', 'ai', 'aih', 'in', 'it', 'iang', 'iak', 'am', 'ap', 'ua', 'uah', 'ang', 'ak', 'iam', 'iap', 'ao', 'aoh', 'ia', 'iah', 'ue', 'ueh', 'na', 'nah', 'u', 'uh', 'a', 'ah', 'i', 'ih', 'iu', 'iuh', 'ne', 'neh', 'nui', 'nuih', 'io', 'ioh', 'ni', 'nih', 'nioo', 'niooh', 'nia', 'niah', 'nua', 'nuah', 'ng', 'ngh', 'e', 'eh', 'nai', 'naih', 'noo', 'nooh', 'm', 'mh', 'uang', 'uak', 'nuai', 'nuaih', 'nue', 'nueh', 'niao', 'niaoh', 'om', 'op', 'nao', 'naoh', 'no', 'noh', 'niu', 'niuh'],
    'TPS': ['ㄨㄣ', 'ㄨㆵ', 'ㄧㄢ', 'ㄧㄚㆵ', 'ㄧㆬ', 'ㄧㆴ', 'ㄨㄧ', 'ㄨㄧㆷ', 'ㄝ', 'ㄝㆷ', 'ㄢ', 'ㄚㆵ', 'ㆲ', 'ㆦㆻ', 'ㄨㄞ', 'ㄨㄞㆷ', 'ㄧㄥ', 'ㄧㆻ', 'ㄨㄢ', 'ㄨㄚㆵ', 'ㆦ', 'ㆦㆷ', 'ㄧㄠ', 'ㄧㄠㆷ', 'ㄟ', 'ㄟㆷ', 'ㄧㆲ', 'ㄧㆦㆻ', 'ㄜ', 'ㄜㆷ', 'ㄞ', 'ㄞㆷ', 'ㄧㄣ', 'ㄧㆵ', 'ㄧㄤ', 'ㄧㄚㆻ', 'ㆰ', 'ㄚㆴ', 'ㄨㄚ', 'ㄨㄚㆷ', 'ㄤ', 'ㄚㆻ', 'ㄧㆰ', 'ㄧㄚㆴ', 'ㄠ', 'ㄠㆷ', 'ㄧㄚ', 'ㄧㄚㆷ', 'ㄨㆤ', 'ㄨㆤㆷ', 'ㆩ', 'ㆩㆷ', 'ㄨ', 'ㄨㆷ', 'ㄚ', 'ㄚㆷ', 'ㄧ', 'ㄧㆷ', 'ㄧㄨ', 'ㄧㄨㆷ', 'ㆥ', 'ㆥㆷ', 'ㄨㆪ', 'ㄨㆪㆷ', 'ㄧㄜ', 'ㄧㄜㆷ', 'ㆪ', 'ㆪ', 'ㄧㆧ', 'ㄧㆧㆷ', 'ㄧㆩ', 'ㄧㆩㆷ', 'ㄨㆩ', 'ㄨㆩㆷ', 'ㆭ', 'ㆭㆷ', 'ㆤ', 'ㆤㆷ', 'ㆮ', 'ㆮㆷ', 'ㆧ', 'ㆧㆷ', 'ㆬ', 'ㆬㆷ', 'ㄨㄤ', 'ㄨㄚㆻ', 'ㄨㆮ', 'ㄨㆮㆷ', 'ㄨㆥ', 'ㄨㆥㆷ', 'ㄧㆯ', 'ㄧㆯㆷ', 'ㆱ', 'ㆦㆴ', 'ㆯ', 'ㆯㆷ', 'ㆧ', 'ㆧㆷ', 'ㄧㆫ', 'ㄧㆫㆷ'],
    'sip_ngoo_im_id': ['1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8', '9', '9', '10', '10', '11', '11', '12', '12', '13', '13', '14', '14', '15', '15', '16', '16', '17', '17', '18', '18', '19', '19', '20', '20', '21', '21', '22', '22', '23', '23', '24', '24', '25', '25', '26', '26', '27', '27', '28', '28', '29', '29', '30', '30', '31', '31', '32', '32', '33', '33', '34', '34', '35', '35', '36', '36', '37', '37', '38', '38', '39', '39', '40', '40', '41', '41', '42', '42', '43', '43', '44', '44', '45', '45', '46', '46', '47', '47', '48', '48', '49', '49', '50', '50'],
}
df_un_bu = pd.DataFrame(un_mu_dict)

# 自 DataFrame 取出，欄標題名為：un_code 的部份，並將之轉換成 list
un_list = df_un_bu["un_code"].values.tolist()
sip_ngoo_im_un_bu_list = df_un_bu["sip_ngoo_im_id"].values.tolist()
sip_ngoo_im_un_bu = df_un_bu["sip_ngoo_im"].values.tolist()

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
        sip_ngoo_im_idx = int(sip_ngoo_im_un_bu_list[un_bu_index])
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
sip_ngoo_im_siann_bu = df_siann_bu["sip_ngoo_im"].values.tolist()

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
"""
十五音注音
"""

sip_ngoo_im_un_bu_2_un_code_dict = {
    '君': ['un', 'ut'],
    '堅': ['ian', 'iat'],
    '金': ['im', 'ip'],
    '規': ['ui', 'uih'],
    '嘉': ['ee', 'eeh'],
    '干': ['an', 'at'],
    '公': ['ong', 'ok'],
    '乖': ['oai', 'oaih'],
    '經': ['eng', 'ek'],
    '觀': ['oan', 'oat'],
    '沽': ['oo', 'ooh'],
    '嬌': ['iau', 'iauh'],
    '稽': ['ei', 'eih'],
    '恭': ['iong', 'iok'],
    '高': ['o', 'oh'],
    '皆': ['ai', 'aih'],
    '巾': ['in', 'it'],
    '姜': ['iang', 'iak'],
    '甘': ['am', 'ap'],
    '瓜': ['oa', 'oah'],
    '江': ['ang', 'ak'],
    '兼': ['iam', 'iap'],
    '交': ['au', 'auh'],
    '迦': ['ia', 'iah'],
    '檜': ['oe', 'oeh'],
    '監': ['ann', 'ahnn'],
    '艍': ['u', 'uh'],
    '膠': ['a', 'ah'],
    '居': ['i', 'ih'],
    '丩': ['iu', 'iuh'],
    '更': ['enn', 'ehnn'],
    '褌': ['uinn', 'uinnh'],
    '茄': ['io', 'ioh'],
    '梔': ['inn', 'ihnn'],
    '薑': ['ionn', 'ionnh'],
    '驚': ['iann', 'iannh'],
    '官': ['oann', 'oannh'],
    '鋼': ['ng', 'ngh'],
    '伽': ['e', 'eh'],
    '閒': ['ainn', 'ainnh'],
    '姑': ['onn', 'onnh'],
    '姆': ['m', 'mh'],
    '光': ['oang', 'oak'],
    '閂': ['oainn', 'oaihnn'],
    '糜': ['oenn', 'oennh'],
    '嘄': ['iaunn', 'iauhnn'],
    '箴': ['om', 'op'],
    '爻': ['aunn', 'aunnh'],
    '扛': ['onn', 'ohnn'],
    '牛': ['iunn', 'iunnh'],
}

sip_ngoo_im_tiau_dict = {
    1: "一",
    2: "二",
    3: "三",
    4: "四",
    5: "五",
    7: "七",
    8: "八",
}

sip_ngoo_im_trandication_tiau_dict = {
    "上平": 1,
    "上上": 2,
    "上去": 3,
    "上入": 4,
    "下平": 5,
    "下上": 6,
    "下去": 7,
    "下入": 8,
}

def get_siann_code_by_siann_bu(sian_bu):
    index = sip_ngoo_im_siann_bu.index(sian_bu)
    return siann_list[index]

def get_un_code_by_un_bu(un_bu, tiau):
    if tiau == 4 or tiau == 8:
        # 韻母為入聲韻
        un_bu_code = sip_ngoo_im_un_bu_2_un_code_dict[un_bu][1]
    else:
        # 韻母為舒聲韻
        un_bu_code = sip_ngoo_im_un_bu_2_un_code_dict[un_bu][0]
    return un_bu_code

def convert_trandication_tiau(tiau):
    return sip_ngoo_im_trandication_tiau_dict[tiau]

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
"""
方音符號(TPS)
"""

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
