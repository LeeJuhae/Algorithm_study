def solution(s):
    answer = []
    info_dict = {}
    temp = []
    str_num = ''
    for ch in s[1:-1]:
        if ch == '{':
            comma_cnt = 1
        elif ch == '}':
            temp.append(int(str_num))
            info_dict[comma_cnt] = temp
            temp = []
            str_num = ''
        elif ch == ',':
            if len(str_num) != 0:
                temp.append(int(str_num))
                str_num = ''
                comma_cnt += 1
        else:
            str_num += ch
    info_dict = sorted(info_dict.items())
    for k, set_v in info_dict:
        for v in set_v:
            if v not in answer:
                answer.append(v)
                break
    return answer
