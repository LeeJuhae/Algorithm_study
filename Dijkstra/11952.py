# https://www.acmicpc.net/problem/11952

import sys
from collections import defaultdict
from heapq import heappush, heappop

ft_input = sys.stdin.readline
n, m, k, s = map(int, ft_input().split())
p, q = map(int, ft_input().split())
queue = []
occupied = []
z_dist = [float('inf') for _ in range(n + 1)]

for _ in range(k):
	city = int(ft_input().rstrip())
	occupied.append(city)
	heappush(queue, (0,city))
	z_dist[city] = 0

paths = defaultdict(list)
for _ in range(m):
	u, v = map(int, ft_input().split())
	paths[u].append(v)
	paths[v].append(u)

while queue:
	d, node = heappop(queue)
	if z_dist[node] < d:
		continue
	for next_node in paths[node]:
		if z_dist[next_node] <= d + 1:
			continue
		heappush(queue, (d + 1, next_node))
		z_dist[next_node] = d + 1

queue = []
heappush(queue, (0, 1))
visit = [float('inf') for _ in range(n + 1)]
visit[1] = 0

while queue:
	cost, node = heappop(queue)
	if visit[node] < cost:
		continue
	for next_node in paths[node]:
		if next_node in occupied:
			continue
		if next_node == n:
			next_cost = cost
		else:
			next_cost = cost + (p if z_dist[next_node] > s else q)
		if visit[next_node] <= next_cost:
			continue
		heappush(queue, (next_cost, next_node))
		visit[next_node] = next_cost
print(visit[n])
