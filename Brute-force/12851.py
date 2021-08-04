# https://www.acmicpc.net/problem/12851

import sys
from collections import deque

n, k = list(map(int, sys.stdin.readline().split()))
max_range = 100000
visit = [-1 for _ in range(max_range + 1)]
visit[n] = 0
directions = (0, 1, -1)
q = deque([(n, 0)])
ans, cnt = float('inf'), 0

if n == k:
	cnt = 1
else:
	while q:
		n_pos, time= q.popleft()
		for d in directions:
			next_n_pos = n_pos + d if d else 2 * n_pos
			next_time = time + 1
			if next_n_pos not in range(0, max_range + 1):
				continue
			if visit[next_n_pos] == -1 or visit[next_n_pos] >= next_time:
				if next_n_pos == k:
					if visit[k] == next_time: cnt += 1
					else: cnt = 1
				q.append((next_n_pos, next_time))
				visit[next_n_pos] = next_time
print(visit[k])
print(cnt)
