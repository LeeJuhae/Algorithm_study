# https://www.acmicpc.net/problem/1613

import sys

ft_input = sys.stdin.readline
n, k = map(int, ft_input().split())
h = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(k):
	before, after = map(int, ft_input().split())
	h[before][after] = -1
	h[after][before] = 1

for k in range(1, n + 1):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if h[i][k] * h[k][j] > 0 and h[i][j] == 0:
				h[i][j] = h[i][k]
				h[j][i] = -1 * h[i][k]

s = int(ft_input().rstrip())
for _ in range(s):
	a, b = map(int, ft_input().split())
	print(h[a][b])
