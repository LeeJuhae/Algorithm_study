# https://www.acmicpc.net/problem/1194

import sys
from collections import deque

'''
# key point

maze[x][y] = key 일 때, 가지고 있는 key 값을 저장할 때,
k의 복사본 nk를 만들어 nk 값을 바꾸어 주는 것.

'''

n, m = map(int, sys.stdin.readline().split())
maze = []
start_x, start_y = 0, 0
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(1 << 6)]
for i in range(n):
	maze.append(list(sys.stdin.readline().split()[0]))
	if '0' in maze[-1]:
		start_x, start_y = i, maze[-1].index('0')
		visited[0][start_x][start_y] = True
		maze[start_x][start_y] = '.'

q = deque([(start_x, start_y, 0, 0)])
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
keys = ['a', 'b', 'c', 'd', 'e', 'f']
doors = ['A', 'B', 'C', 'D', 'E', 'F']

while q:
	x, y, k, d = q.popleft()
	for dx, dy in directions:
		nx, ny, nd = x + dx, y + dy, d + 1
		if nx not in range(0, n) or ny not in range(0, m) or visited[k][nx][ny]:
			continue
		if maze[nx][ny] == '#':
			continue
		elif maze[nx][ny] == '.':
			q.append((nx, ny, k, nd))
			visited[k][nx][ny] = True
		elif maze[nx][ny] in keys:
			nk = k
			nk |= (1 << ord(maze[nx][ny]) - 97)
			q.append((nx, ny, nk, nd))
			visited[nk][nx][ny] = True
		elif maze[nx][ny] in doors:
			if k & (1 << ord(maze[nx][ny])- 65):
				q.append((nx, ny, k, nd))
				visited[k][nx][ny] = True
		elif maze[nx][ny] == '1':
			print(d + 1)
			sys.exit()
print(-1)
