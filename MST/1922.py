# https://www.acmicpc.net/problem/1922

'''
프림 알고리즘 사용
'''

import sys
from collections import defaultdict
from heapq import heappush, heappop

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
m = int(ft_input().rstrip())
adj = defaultdict(list)
for _ in range(m):
	a, b, c = map(int, ft_input().split())
	adj[a].append((c, b))
	adj[b].append((c, a))

q = [(0, 1)]
visit = [False for _ in range(n + 1)]
cnt, min_cost = 0, 0
while q:
	if cnt == n:
		break
	cost, node = heappop(q)
	if not visit[node]:
		visit[node] = True
		cnt += 1
		min_cost += cost
		for nxt in adj[node]:
			heappush(q, nxt)
print(min_cost)
