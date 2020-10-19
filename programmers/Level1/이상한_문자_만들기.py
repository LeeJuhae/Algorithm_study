def solution(s):
    ind = 0
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            ind = 0
            answer += s[i]
            continue
        if ind % 2 == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        ind += 1
    return answer
