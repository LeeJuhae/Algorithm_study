# https://www.acmicpc.net/problem/2573

import sys
from  collections import deque

ft_input = sys.stdin.readline
n, m = map(int, ft_input().split())
maps = [list(map(int, ft_input().split())) for _ in range(n)]
year = 0

def melt(x, y, visit):
	directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
	queue = deque([[x, y]])
	melting_q = deque([])
	while queue:
		x, y = queue.popleft();
		melting_cnt = 0
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if nx not in range(n) or ny not in range(m) or visit[nx][ny]:
				continue
			if maps[nx][ny] != 0:
				visit[nx][ny] = True
				queue.append([nx, ny])
			else:
				melting_cnt += 1
		if melting_cnt:
			melting_q.append([x, y, melting_cnt])
	return melting_q

while True:
	cnt = 0
	visit = [[False for _ in range(m)] for _ in range(n)]
	for x in range(n):
		for y in range(m):
			if maps[x][y] != 0 and not visit[x][y]:
				cnt += 1
				visit[x][y] = True
				melting = melt(x, y, visit)
				while melting:
					mx, my, m_cnt = melting.popleft()
					maps[mx][my] = max(0, maps[mx][my] - m_cnt)
	if cnt == 0:
		year = 0
		break
	if cnt >= 2:
		break
	year += 1
print(year)
