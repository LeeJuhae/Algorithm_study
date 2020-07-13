import math

def get_multi_set(str):
    multi_set = []
    for i in range(len(str)-1):
        if str[i:i+2].isalpha():
            multi_set.append(str[i:i+2])
    return multi_set

def solution(str1, str2):
    answer = 0
    inter_cnt = 0
    union_cnt = 0
    str1 = str1.upper()
    str2 = str2.upper()
    multi_set1 = get_multi_set(str1)
    multi_set2 = get_multi_set(str2)
    if len(multi_set1) == 0 and len(multi_set2) == 0:
        return 1 * 65536
    single_set1 = set(multi_set1)
    single_set2 = set(multi_set2)
    inter_set = single_set1.intersection(single_set2)
    union_set = single_set1.union(single_set2)
    for i in inter_set:
        inter_cnt += min(multi_set1.count(i), multi_set2.count(i))
    for u in union_set:
        union_cnt += max(multi_set1.count(u), multi_set2.count(u))
    return math.floor((inter_cnt / union_cnt) * 65536)
