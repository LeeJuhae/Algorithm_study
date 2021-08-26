# https://www.acmicpc.net/problem/1854

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop

ft_input = sys.stdin.readline
n, m, k = map(int, ft_input().split())
paths = defaultdict(lambda: defaultdict(lambda: float('inf')))
for _ in range(m):
	a, b, c = map(int, ft_input().split())
	paths[a][b] = c
visit = [[] for _ in range(n + 1)]
queue = [(0, 1)]
visit[1].append(0)
while queue:
	cost, node = heappop(queue)
	for next_node, next_cost in paths[node].items():
		next_cost += cost
		if len(visit[next_node]) < k:
			heappush(visit[next_node], -next_cost)
			heappush(queue, (next_cost, next_node))
		elif -visit[next_node][0] > next_cost:
			heappop(visit[next_node])
			heappush(visit[next_node], -next_cost)
			heappush(queue, (next_cost, next_node))
for i in range(1, n + 1):
	print(-1 if len(visit[i]) < k else -visit[i][0])
