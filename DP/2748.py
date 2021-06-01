# https://www.acmicpc.net/problem/2748

def go(n):
    if n < 2:
        return n

    if dp[n]:
        return dp[n]

    ret = go(n-1) + go(n-2)
    dp[n] = ret
    return ret


n = int(input())
dp = [None for _ in range(n+1)]
print(go(n))
