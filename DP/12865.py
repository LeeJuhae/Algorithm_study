# https://www.acmicpc.net/problem/12865

import sys

ft_input = sys.stdin.readline
n, k = map(int, ft_input().split())
things = [(0, 0)]
for _ in range(n):
	w, v = map(int, ft_input().split())
	things.append((w, v))

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
	for j in range(1, k + 1):
		w, v = things[i]
		if j < w:
			dp[i][j] = dp[i - 1][j]
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[n][k])
