# https://www.acmicpc.net/problem/14728

import sys

ft_input = sys.stdin.readline
n, t = map(int, ft_input().split())
sections = [(0, 0)]
for _ in range(n):
	sections.append(tuple(map(int, ft_input().split())))
dp = [[0 for _ in range(t + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
	for j in range(1, t + 1):
		k, s = sections[i]
		if j < k:
			dp[i][j] = dp[i - 1][j]
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - k] + s)
print(dp[n][t])
