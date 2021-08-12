# https://www.acmicpc.net/problem/14588

import sys

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
lines = [list(map(int, ft_input().split())) for _ in range(n)]
q = int(ft_input().rstrip())
d = [[float('inf') for _ in range(n )] for _ in range(n)]
for i in range(n):
	for j in range(i + 1, n):
		if lines[j][0] in range(lines[i][0], lines[i][1] + 1) \
			or lines[j][1] in range(lines[i][0], lines[i][1] + 1) \
			or lines[i][0] in range(lines[j][0], lines[j][1] + 1):
			d[i][j] = 1
			d[j][i] = 1

for k in range(n):
	for i in range(n):
		for j in range(n):
			if d[i][k] != 0 and d[k][j] != 0:
				d[i][j] = min(d[i][j], d[i][k] + d[k][j])

for _ in range(q):
	a, b = map(int, ft_input().split())
	print(d[a-1][b-1] if d[a-1][b-1] != float('inf') else -1)
