# https://www.acmicpc.net/problem/4811

import sys


def take(day, w, h):
    if day == 2 * n:
        return 1
    if dp[day][w][h] != -1:
        return dp[day][w][h]
    ret = 0
    if w + 1 <= n:
        ret += take(day + 1, w + 1, h)
    if h + 1 <= w:
        ret += take(day + 1, w, h + 1)
    dp[day][w][h] = ret
    return ret


N = list(map(int, sys.stdin.read().split()))[:-1]
for n in N:
    dp = [[[-1 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(2 * n + 1)]
    print(take(0, 0, 0))
