# https://www.acmicpc.net/problem/17208

def sell(d, burger, fries):
    if d == N:
        return 0

    if dp[d][burger][fries]:
        return dp[d][burger][fries]

    ret = 0
    if burger - order[d][0] >= 0 and fries - order[d][1] >= 0:
        ret = sell(d+1, burger - order[d][0], fries - order[d][1]) + 1
    ret = max(sell(d+1, burger, fries), ret)
    dp[d][burger][fries] = ret
    return ret


N, M, K = map(int, input().split())
order = [list(map(int, input().split())) for _ in range(N)]
dp = [[[None for _ in range(K+1)]for _ in range(M+1)]for _ in range(N)]
print(sell(0, M, K))
