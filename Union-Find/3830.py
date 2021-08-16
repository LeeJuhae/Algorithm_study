# https://www.acmicpc.net/problem/3830

import sys
sys.setrecursionlimit(10**6)

def find(a):
	if a == p[a]:
		return a
	x = find(p[a])
	''' 가장 부모인 노드와의 무게 차이를 저장 '''
	weights[a] += weights[p[a]]
	p[a] = x
	return p[a]

def union(a, b, w):
	x = find(a)
	y = find(b)
	p[x] = y
	'''
	(부모) <- (자식)일 때,
	x <-- (+weights[a]) -- a			x <- a
						   ↓ (+w)	=> 	↓	 ↓ (+w)	와 같이 병합될 때
	y <-- (+weights[b]) -- b			y <- b

	weights[x] = -weights[a] + w + weights[b]
	(화살표의 방향에 유의해서 따라가면 식이 쉽게 이해됨)
	'''
	weights[x] = weights[b] + w - weights[a]

ft_input = sys.stdin.readline
while True:
	n, m = map(int, ft_input().split())
	if n == 0 and m == 0:
		break
	p = [i for i in range(n + 1)]
	weights = [0 for i in range(n + 1)]
	for _ in range(m):
		works = list(ft_input().split())
		if works[0] == '!':
			a, b, w = map(int, works[1:])
			if find(a) != find(b):
				union(a, b, w)
		else:
			a, b = map(int, works[1:])
			if find(a) != find (b):
				print('UNKNOWN')
			else:
				print(weights[a] - weights[b])
