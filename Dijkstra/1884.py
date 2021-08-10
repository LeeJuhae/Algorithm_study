# https://www.acmicpc.net/problem/1884

import sys
from collections import defaultdict
from heapq import heappush, heappop

ft_input = sys.stdin.readline
k = int(ft_input().rstrip())
n = int(ft_input().rstrip())
r = int(ft_input().rstrip())
roads = defaultdict(list)
for _ in range(r):
	s, d, l, t = map(int, ft_input().split())
	roads[s].append((l, d, t))

queue = []
heappush(queue, (0, 0, 1))
visit = [[float('inf') for _ in range(k + 1)] for _ in range(n + 1)]

while queue:
	d, cost, node = heappop(queue)
	if visit[node][cost] < d:
		continue

	for next_d, next_node, next_cost in roads[node]:
		if cost + next_cost > k:
			continue
		if visit[next_node][cost + next_cost] <= d + next_d:
			continue
		heappush(queue, (d + next_d, cost + next_cost, next_node))
		visit[next_node][cost + next_cost] = d + next_d
ans = min(visit[n])
print(ans if ans != float('inf') else -1)
