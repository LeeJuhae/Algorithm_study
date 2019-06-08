def solution(n, m):
    answer = [n*m]
    while m!=0:
        r = n % m
        n = m
        m = r
    answer.insert(0,n)
    answer[1] = answer[1] / answer[0]
    return answer
