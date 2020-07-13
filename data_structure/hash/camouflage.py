def solution(clothes):
    answer = 1
    clothes_dict = dict()
    for cloth in clothes:
        if cloth[1] not in clothes_dict.keys():
            clothes_dict[cloth[1]] = 1
        else:
            clothes_dict[cloth[1]] += 1
    for value in clothes_dict.values():
        answer *= (value + 1)
    return answer - 1
