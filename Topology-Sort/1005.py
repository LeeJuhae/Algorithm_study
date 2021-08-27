# https://www.acmicpc.net/problem/1005

import sys
from collections import defaultdict, deque

ft_input = sys.stdin.readline
t = int(ft_input().rstrip())
for _ in range(t):
	n, k = map(int, ft_input().split())
	times = [0] + list(map(int, ft_input().split()))
	preworks = [times[i] for i in range(n + 1)]
	graphs = defaultdict(list)
	indegrees = [0 for _ in range(n + 1)]
	for _ in range(k):
		x, y = map(int, ft_input().split())
		graphs[x].append(y)
		indegrees[y] += 1
	w = int(ft_input().rstrip())
	queue = deque([])
	for i in range(1, n + 1):
		if indegrees[i] == 0:
			queue.append((i))
	while queue:
		node = queue.popleft()
		for next_node in graphs[node]:
			indegrees[next_node] -= 1
			preworks[next_node] = max(preworks[node] + times[next_node], preworks[next_node])
			if indegrees[next_node] == 0:
				queue.append((next_node))
	print(preworks[w])
