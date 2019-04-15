import math
def solution(n):
    prime = []
    num = 0
    for i in range(2, n+1):
        prime.append(i)
    
    for i in range(2,math.ceil(math.sqrt(n))):
        if prime[i-2] == -1:
            continue
        for j in range(i-1,len(prime)):
            if prime[j] % i == 0:
                prime[j]=-1
                
    for i in range(len(prime)):
        if prime[i] != -1:
            num += 1
            
    return num
