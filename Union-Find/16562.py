# https://www.acmicpc.net/problem/16562

import sys

def find(a):
	if a == p[a]:
		return a
	p[a] = find(p[a])
	return p[a]

def union(a, b):
	x = find(a)
	y = find(b)
	if costs[x] > costs[y]:
		p[x] = y
	else:
		p[y] = x

ft_input = sys.stdin.readline
n, m, k = map(int, ft_input().split())
costs = [0] + list(map(int, ft_input().split()))
p = [i for i in range(n + 1)]
for _ in range(m):
	v, w = map(int, ft_input().split())
	if find(v) != find(w):
		union(v, w)

ans = 0
for i in range(1, n + 1):
	if i == p[i]:
		ans += costs[i]
print(ans if ans <= k else 'Oh no')
