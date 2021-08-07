# https://www.acmicpc.net/problem/2665

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
rooms = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
# visit[x][y] = (x, y) 까지 가는데 검은 방을 흰 방으로 바꾼 횟수
visit = [[-1 for _ in range(n)] for _ in range(n)]
visit[0][0] = 0
q = deque([(0, 0)])
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

while q:
	x, y = q.popleft()

	if x == n - 1 and y == n - 1:
		print(visit[x][y])
		break

	for d_x, d_y in directions:
		next_x, next_y = x + d_x, y + d_y
		if next_x not in range(n) or next_y not in range(n) or \
			visit[next_x][next_y] != -1:
			continue
		if rooms[next_x][next_y] == '1':
			visit[next_x][next_y] = visit[x][y]
			q.appendleft((next_x, next_y))
		else:
			visit[next_x][next_y] = visit[x][y] + 1
			q.append((next_x, next_y))
