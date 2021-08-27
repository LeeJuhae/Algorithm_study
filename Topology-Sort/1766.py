# https://www.acmicpc.net/problem/1766

import sys
from collections import defaultdict
from heapq import heappush, heappop

ft_input = sys.stdin.readline
n, m = map(int, ft_input().split())
graphs = defaultdict(list)
indegrees = [0 for _ in range(n + 1)]
for _ in range(m):
	a, b = map(int, ft_input().split())
	graphs[a].append(b)
	indegrees[b] += 1
queue = []
ans = []
for i in range(1, n + 1):
	if indegrees[i] == 0:
		heappush(queue, i)
while queue:
	node = heappop(queue)
	ans.append(node)
	for next_node in graphs[node]:
		indegrees[next_node] -= 1
		if indegrees[next_node] == 0:
			heappush(queue, next_node)
print(*ans)
