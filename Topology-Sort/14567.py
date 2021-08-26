# https://www.acmicpc.net/problem/14567

import sys
from collections import defaultdict, deque

ft_input = sys.stdin.readline
n, m = map(int, ft_input().split())
paths = defaultdict(list)
indegrees = [0 for _ in range(n + 1)]
semesters = [0 for _ in range(n + 1)]
queue = deque([])

for _ in range(m):
	a, b = map(int, ft_input().split())
	paths[a].append(b)
	indegrees[b] += 1

for i in range(1, n + 1):
	if indegrees[i] == 0:
		queue.append((i, 1))

while queue:
	node, semester = queue.popleft()
	semesters[node] = semester
	for next_node in paths[node]:
		indegrees[next_node] -= 1
		if indegrees[next_node] == 0:
			queue.append((next_node, semester + 1))
print(*semesters[1:])
