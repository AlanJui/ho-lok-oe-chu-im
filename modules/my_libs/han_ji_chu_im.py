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
    'un_code': ['a', 'ann', 'ah', 'ahnn', 'ai', 'ainn', 'ak', 'am', 'an', 'ang', 'ap', 'at', 'au', 'auh', 'e', 'enn', 'eh', 'ehnn', 'ek', 'eng', 'i', 'inn', 'ia', 'iann', 'iah', 'iannh', 'iak', 'iam', 'ian', 'iang', 'iap', 'iat', 'iau', 'iaunn', 'iauh', 'ih', 'im', 'in', 'io', 'ioh', 'iok', 'iong', 'ip', 'it', 'iu', 'iunn', 'iunnh', 'm', 'mh', 'ng', 'ngh', 'o', 'onn', 'oo', 'oa', 'oann', 'oah', 'oai', 'oainn', 'oan', 'oang', 'oat', 'oe', 'oeh', 'oh', 'onnh', 'ok', 'om', 'ong', 'u', 'uh', 'ui', 'un', 'ut'],
    'IPA': ['a', 'ã', 'a?', 'ã?', 'ai', 'ãĩ', 'ak̚', 'am', 'an', 'aŋ', 'ap̚', 'at̚', 'aʊ', 'au?', 'e', 'ẽ', 'e?', 'ẽ?', 'ik̚', 'ɪŋ', 'i', 'ĩ', 'ia', 'ĩã', 'ia?', 'iãh', 'iak̚', 'iam', 'ian', 'iaŋ', 'iap̚', 'iat̚', 'iaʊ', 'ĩãũ', 'iau?', 'i?', 'im', 'in', 'io', 'iə?', 'iɔk̚', 'iɔŋ', 'ip̚', 'it̚', 'iu', 'ĩũ', 'iũh', 'm̩', 'm̩h', 'ŋ̍', 'ŋ̍h', 'o', 'ɔ̃', 'ɔ', 'ua', 'ũã', 'ua?', 'uai', 'ũãĩ', 'uan', 'uaŋ', 'uat̚', 'ue', 'ue?', 'ə?', 'ɔ̃?', 'ɔk̚', 'ɔm', 'ɔŋ', 'u', 'u?', 'ui', 'un', 'ut̚'],
    'sip_ngoo_im': ['膠', '監', '膠', '監', '皆', '閒', '江', '甘', '干', '江', '甘', '干', '交', '交', '伽', '更', '伽', '更', '經', '經', '居', '梔', '迦', '驚', '迦', '驚', '姜', '兼', '堅', '姜', '兼', '堅', '嬌', '嘄', '嬌', '居', '金', '巾', '茄', '茄', '恭', '恭', '金', '巾', '丩', '牛', '牛', '姆', '姆', '鋼', '鋼', '高', '姑', '沽', '瓜', '官', '瓜', '乖', '閂', '觀', '光', '觀', '檜', '檜', '高', '姑', '公', '箴', '公', '艍', '艍', '規', '君', '君'],
    'POJ': ['a', 'aⁿ', 'ah', 'ahⁿ', 'ai', 'aiⁿ', 'ak', 'am', 'an', 'ang', 'ap', 'at', 'au', 'auh', 'e', 'eⁿ', 'eh', 'ehⁿ', 'ek', 'eng', 'i', 'iⁿ', 'ia', 'iaⁿ', 'iah', 'iahⁿ', 'iak', 'iam', 'ian', 'iang', 'iap', 'iat', 'iau', 'iauⁿ', 'iauh', 'ih', 'im', 'in', 'io', 'ioh', 'iok', 'iong', 'ip', 'it', 'iu', 'iuⁿ', 'iuhⁿ', 'm', 'mh', 'ng', 'ngh', 'o', 'oⁿ', 'o͘', 'oa', 'oaⁿ', 'oah', 'oai', 'oaiⁿ', 'oan', 'oang', 'oat', 'oe', 'oeh', 'oh', 'ohⁿ', 'ok', 'om', 'ong', 'u', 'uh', 'ui', 'un', 'ut'],
    'TL': ['a', 'ann', 'ah', 'annh', 'ai', 'ainn', 'ak', 'am', 'an', 'ang', 'ap', 'ap', 'au', 'auh', 'e', 'enn', 'eh', 'ennh', 'ik', 'ing', 'i', 'inn', 'ia', 'iann', 'iah', 'iannh', 'iak', 'iam', 'ian', 'iang', 'iap', 'iat', 'iau', 'iaunn', 'iauh', 'ih', 'im', 'in', 'io', 'ioh', 'iok', 'iong', 'ip', 'it', 'iu', 'iunn', 'iunnh', 'm', 'mh', 'ng', 'ngh', 'o', 'onn', 'oo', 'ua', 'uann', 'uah', 'uai', 'uainn', 'uan', 'uang', 'uat', 'ue', 'ueh', 'oh', 'onnh', 'ok', 'om', 'ong', 'u', 'uh', 'ui', 'un', 'ut'],
    'BP': ['a', 'na', 'ah', 'nah', 'ai', 'nai', 'ak', 'am', 'an', 'ang', 'ap', 'at', 'ao', 'aoh', 'e', 'ne', 'eh', 'neh', 'ik', 'ing', 'i', 'ni', 'ia', 'nia', 'iah', 'niah', 'iak', 'iam', 'ian', 'iang', 'iap', 'iat', 'iao', 'niao', 'iaoh', 'ih', 'im', 'in', 'io', 'ioh', 'iok', 'iong', 'ip', 'it', 'iu', 'niu', 'niuh', 'm', 'mh', 'ng', 'ngh', 'o', 'noo', 'oo', 'ua', 'nua', 'uah', 'uai', 'nuai', 'uan', 'uang', 'uat', 'ue', 'ueh', 'oh', 'nooh', 'ok', 'om', 'ong', 'u', 'uh', 'ui', 'un', 'ut'],
    'TPS': ['ㄚ', 'ㆩ', 'ㄚㆷ', 'ㆩㆷ', 'ㄞ', 'ㆮ', 'ㄚㆻ', 'ㆰ', 'ㄢ', 'ㄤ', 'ㄚㆴ', 'ㄚㆵ', 'ㄠ', 'ㄠㆷ', 'ㆤ', 'ㆥ', 'ㆤㆷ', 'ㆥㆷ', 'ㄧㆻ', 'ㄧㄥ', 'ㄧ', 'ㆪ', 'ㄧㄚ', 'ㄧㆩ', 'ㄧㄚㆷ', 'ㄧㆩㆷ', 'ㄧㄚㆻ', 'ㄧㆰ', 'ㄧㄢ', 'ㄧㄤ', 'ㄧㄚㆴ', 'ㄧㄚㆵ', 'ㄧㄠ', 'ㄧㆯ', 'ㄧㄠㆷ', 'ㄧㆷ', 'ㄧㆬ', 'ㄧㄣ', 'ㄧㄜ', 'ㄧㄜㆷ', 'ㄧㆦㆻ', 'ㄧㆲ', 'ㄧㆴ', 'ㄧㆵ', 'ㄧㄨ', 'ㄧㆫ', 'ㄧㆫㆷ', 'ㆬ', 'ㆬㆷ', 'ㆭ', 'ㆭㆷ', 'ㄜ', 'ㆧ', 'ㆦ', 'ㄨㄚ', 'ㄨㆩ', 'ㄨㄚㆷ', 'ㄨㄞ', 'ㄨㆮ', 'ㄨㄢ', 'ㄨㄤ', 'ㄨㄚㆵ', 'ㄨㆤ', 'ㄨㆤㆷ', 'ㄜㆷ', 'ㆧㆷ', 'ㆦㆻ', 'ㆱ', 'ㆲ', 'ㄨ', 'ㄨㆷ', 'ㄨㄧ', 'ㄨㄣ', 'ㄨㆵ'],
}
df_un_bu = pd.DataFrame(un_mu_dict)

# 自 DataFrame 取出，欄標題名為：un_code 的部份，並將之轉換成 list
un_list = df_un_bu["un_code"].values.tolist()

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

# un_bu = "oenn"
# idx2 = get_un_idx(un_bu)
# print(f'idx2 = {idx2}')


# %%

# ==========================================================
# 聲母處理
# ==========================================================
siann_bu_dict = {
    'siann_code': ['b', 'ch', 'chh', 'g', 'h', 'j', 'k', 'kh', 'l', 'm', 'n', 'ng', 'p', 'ph', 's', 't', 'th'],
    'IPA': ['b', 'ʦ', 'ʦʰ', 'ɡ', 'h', 'ʣ', 'k', 'kʰ', 'l', 'm', 'n', 'ŋ', 'p', 'pʰ', 's', 't', 'tʰ'],
    'sip_ngoo_im': ['門', '曾', '出', '語', '喜', '入', '求', '去', '柳', '毛', '耐', '雅', '邊', '頗', '時', '地', '他'],
    'POJ': ['b', 'ch', 'chh', 'g', 'h', 'j', 'k', 'kh', 'l', 'm', 'n', 'ng', 'p', 'ph', 's', 't', ' '],
    'TL': ['b', 'ts', 'tsh', 'g', 'h', 'j', 'k', 'kh', 'l', 'm', 'n', 'ng', 'p', 'ph', 's', 't', 'th'],
    'BP': ['bb', 'z', 'c', 'gg', 'h', 'zz', 'g', 'k', 'l', 'bbn', 'ln', 'ggn', 'b', 'p', 's', 'd', 't'],
    'TPS': ['ㆠ', 'ㄗ', 'ㄘ', 'ㆣ', 'ㄏ', 'ㆡ', 'ㄍ', 'ㄎ', 'ㄌ', 'ㄇ', 'ㄋ', 'ㄫ', 'ㄅ', 'ㄆ', 'ㄙ', 'ㄉ', 'ㄊ'],
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
# chu_im = "nga2"
# chu_im = "chhian5"
chu_im = "boenn2"
result = split_chu_im(chu_im)

siann_bu = result[0]    # siann
un_bu = result[1]    # un
tiau_ho = result[2]   # tiau

idx1 = get_siann_idx(siann_bu)
idx2 = get_un_idx(un_bu)
