import math
def solution(n):
    answer = -1
    if math.sqrt(n) == math.ceil(math.sqrt(n)):
        answer = (int(math.sqrt(n))+1)**2
    return answer
