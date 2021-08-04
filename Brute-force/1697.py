# https://www.acmicpc.net/problem/1697

import sys
from collections import deque

n, k = list(map(int, sys.stdin.readline().split()))
max_range = 100000
visit = [[-1 for _ in range(max_range + 1)] for _ in range(2)]
directions = (0, 1, -1)
q = deque()
q.append((n, 0, k))
ret = -1
visit[0][n] = 0

while q:
	n_pos, time, k_pos = q.popleft()

	if visit[time % 2][k_pos] != -1 and visit[time % 2][k_pos] <= time:
		ret = time
		break

	for direction in directions:
		next_n_pos = n_pos + direction if direction else 2 * n_pos
		next_time = time + 1

		if next_n_pos not in range(0, max_range + 1) or visit[next_time % 2][next_n_pos] != -1:
			continue

		q.append((next_n_pos, next_time, k_pos))
		visit[next_time % 2][next_n_pos] = next_time
print(ret)
