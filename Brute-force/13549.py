# https://www.acmicpc.net/problem/13549

'''
# key point

directions의 순서에 따라 정답이 달라짐
'''
import sys
from collections import deque

n, k = list(map(int, sys.stdin.readline().split()))
max_range = 100000
visit = [-1 for _ in range(max_range + 1)]
directions = (0, -1, 1)
q = deque([n])
visit[n] = 0

while q:
	n_pos = q.popleft()
	if n_pos == k:
		break
	for d in directions:
		next_n_pos = n_pos + d if d else 2 * n_pos
		if next_n_pos not in range(0, max_range + 1) or visit[next_n_pos] != -1:
			continue
		if d:
			q.append(next_n_pos)
			visit[next_n_pos] = visit[n_pos] + 1
		else:
			q.appendleft(next_n_pos)
			visit[next_n_pos] = visit[n_pos]
print(visit[k])
