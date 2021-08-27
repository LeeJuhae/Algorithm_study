# https://www.acmicpc.net/problem/17845

import sys

ft_input = sys.stdin.readline
n, k = map(int, ft_input().split())
subjects = [(0, 0)]
for _ in range(k):
	subjects.append(tuple(map(int, ft_input().split())))
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
for i in range(1, k + 1):
	for j in range(1, n + 1):
		imp, t = subjects[i]
		if j < t:
			dp[i][j] = dp[i - 1][j]
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - t] + imp)
print(dp[k][n])
