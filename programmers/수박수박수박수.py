def solution(n):
    answer = '수박' * int(n/2)
    if n % 2 == 1:
        answer = answer + '수'
    return answer
