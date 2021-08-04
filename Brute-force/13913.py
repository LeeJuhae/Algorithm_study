# https://www.acmicpc.net/problem/13913

import sys
from collections import deque

n, k = list(map(int, sys.stdin.readline().split()))
max_range = 100000
visit = [-1 for _ in range(max_range + 1)]
directions = (0, -1, 1)
q = deque([n])
visit[n] = n
path = []

while q:
	n_pos = q.popleft()
	if n_pos == k:
		path.append(n_pos)
		while n_pos != n:
			path.append(visit[n_pos])
			n_pos = visit[n_pos]
		break
	for d in directions:
		next_n_pos = n_pos + d if d else 2 * n_pos
		if next_n_pos not in range(0, max_range + 1) or visit[next_n_pos] != -1:
			continue
		q.append(next_n_pos)
		visit[next_n_pos] = n_pos

print(len(path) -1)
print(*path[::-1])
