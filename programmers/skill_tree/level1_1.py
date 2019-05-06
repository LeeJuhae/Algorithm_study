def solution(n):
    answer = []
    while(True):
        if n < 10:
            answer.append(n)
            break
        answer.append(n%10)
        n = (n - n%10)/10
    return answer
