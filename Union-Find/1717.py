# https://www.acmicpc.net/problem/1717

import sys
sys.setrecursionlimit(10 ** 6)

def union(a, b):
	x = find(a)
	y = find(b)
	if x < y:
		p[y] = x
	else:
		p[x] = y

def find(a):
	if a == p[a]:
		return a
	p[a] = find(p[a])
	return p[a]

ft_input = sys.stdin.readline
n, m = map(int, ft_input().split())
p = [i for i in range(n + 1)]
for _ in range(m):
	cmd, a, b = map(int, ft_input().split())
	if cmd == 0:
		union(a, b)
	else:
		print('YES' if find(a) == find(b) else 'NO')
