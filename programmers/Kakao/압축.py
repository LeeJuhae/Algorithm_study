def solution(msg):
    answer = []
    lzw_dict = {}
    idx = 1
    for _ in range(1, 27):
        lzw_dict[chr(ord('A') + idx - 1)] = idx
        idx += 1

    i = 0
    while i < len(msg):
        for j in range(len(msg),i,-1):
            if msg[i:j] in lzw_dict.keys():
                answer.append(lzw_dict[msg[i:j]])
                lzw_dict[msg[i:j+1]] = idx
                idx += 1
                i = j
                break
    return answer
