# https://www.acmicpc.net/problem/16724

import sys

def find(a):
	if a == p[a]:
		return a
	p[a] = find(p[a])
	return p[a]

def union(a, b):
	x = find(a)
	y = find(b)
	if x < y:
		p[y] = x
	else:
		p[x] = y

ft_input = sys.stdin.readline
n, m = map(int, ft_input().split())
maps = [list(ft_input().rstrip()) for _ in range(n)]
directions = {'U': -1 * m, 'D': m, 'L': -1, 'R': 1}
p = [i for i in range(n * m)]
for r in range(n):
	for c in range(m):
		d = directions[maps[r][c]]
		now = r * m + c
		if find(now) != find(now + d):
			union(now, now + d)
'''
아래 과정 없이 바로
print(len(set(p))) 로 답을 출력할 경우 오답.

ex.
3 4
DRDL
UDUD
URUL
 => p = [0, 1, 1, 1, 0, 1, 1, 1, 0, 5, 1, 7]
'''
visit = set()
for i in range(n * m):
	visit.add(find(i))
print(len(visit))
