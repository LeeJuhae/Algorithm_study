def solution(s):
    answer = list()
    for ch in s:
        if len(answer) != 0 and answer[-1] == ch:
            answer.pop()
        else:
            answer.append(ch)
    return 1 if len(answer) == 0 else 0
