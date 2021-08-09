# https://www.acmicpc.net/problem/16681

import sys
from collections import defaultdict
from heapq import heappush, heappop

ft_input = sys.stdin.readline
n, m, d, e = list(map(int, ft_input().split()))
heights = list(map(int, ft_input().split()))
paths = defaultdict(list)
for _ in range(m):
	u, v, w = list(map(int, ft_input().split()))
	if heights[u-1] < heights[v-1]:
		paths[u].append((v, w))
	elif heights[u-1] > heights[v-1]:
		paths[v].append((u, w))

def dijkstra(asc=True):
	q = []
	start = 1 if asc else n
	heappush(q, (0, start))
	visit = [float('inf') for _ in range(n + 1)]
	visit[start] = 0

	while q:
		cost, node = heappop(q)
		if visit[node] < cost:
			continue
		for next_node, next_cost  in paths[node]:
			if visit[next_node] > cost + next_cost:
				visit[next_node] = cost + next_cost
				heappush(q, (cost + next_cost, next_node))
	return visit

ascend = dijkstra()[1:]
descend = dijkstra(False)[1:]
dist = list(map(sum, zip(ascend, descend)))
ans = -float('inf')
for i in range(n):
	achievement = heights[i] * e
	consumption = dist[i] * d
	if achievement == float('inf') or consumption == float('inf'):
		continue
	ans = max(ans, achievement - consumption)
print(ans if ans != -float('inf') else 'Impossible')

