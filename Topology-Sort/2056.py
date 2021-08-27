# https://www.acmicpc.net/problem/2056

import sys
from collections import defaultdict, deque

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
graphs = defaultdict(list)
indegrees = [0 for _ in range(n + 1)]
times = [0 for _ in range(n + 1)]
preworks = [0]
for i in range(n):
	work = list(map(int, ft_input().split()))
	times[i + 1] = work[0]
	preworks.append(work[0])
	indegrees[i + 1] += work[1]
	for j in range(work[1]):
		graphs[work[2 + j]].append(i + 1)
queue = deque([])
ans = 0
for i in range(1, n + 1):
	if indegrees[i] == 0:
		queue.append((i))
		if not len(graphs[i]):
			ans = max(ans, times[i])
while queue:
	node = queue.popleft()
	for next_node in graphs[node]:
		indegrees[next_node] -= 1
		preworks[next_node] = max(preworks[node] + times[next_node], preworks[next_node])
		if indegrees[next_node] == 0:
			queue.append((next_node))
print(max(max(preworks), ans))
