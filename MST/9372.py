# https://www.acmicpc.net/problem/9372

import sys

ft_input = sys.stdin.readline
t = int(ft_input().rstrip())
for _ in range(t):
	n, m = map(int, ft_input().split())
	for _ in range(m):
		ft_input().split()
	print(n-1)
