def solution(n):
    divisor = []
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            divisor.append(i)
    for i in range(len(divisor)):
        answer += divisor[i]
    return answer


#참고 code
#def sumDivisor(num):
#num / 2 의 수들만 검사하면 성능 약 2배 향상
#    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
