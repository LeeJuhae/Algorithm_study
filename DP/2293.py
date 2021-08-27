# https://www.acmicpc.net/problem/2293
# https://jshong1125.tistory.com/44

import sys

ft_input = sys.stdin.readline
n, k = map(int, ft_input().split())
coins = []
for _ in range(n):
	coins.append(int(ft_input().rstrip()))
dp = [0 for _ in range(k + 1)]
dp[0] = 1
for coin in coins:
	for j in range(coin, k + 1):
		dp[j] = dp[j] + dp[j - coin]
print(dp[k])
