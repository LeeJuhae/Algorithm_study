# https://www.acmicpc.net/problem/14621

import sys
from collections import defaultdict
from heapq import heappush, heappop

ft_input = sys.stdin.readline
n, m = map(int, ft_input().split())
schools = [0] + ft_input().split()
adj = defaultdict(list)

for _ in range(m):
	u, v, d = map(int, ft_input().split())
	if schools[u] != schools[v]:
		adj[u].append((d, v))
		adj[v].append((d, u))

visit = [False for _ in range(n + 1)]
q = [(0, 1)]
min_cost, cnt = 0, 0
while q:
	if cnt == n:
		break
	cost, node = heappop(q)
	if not visit[node]:
		visit[node] = True
		min_cost += cost
		cnt += 1
		for next_cost, next_node in adj[node]:
			heappush(q, (next_cost, next_node))
print(min_cost if cnt == n else -1)
