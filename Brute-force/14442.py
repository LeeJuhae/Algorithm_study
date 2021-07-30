# https://www.acmicpc.net/problem/14442

'''
# key point

visited: [부순 벽의 수][x][y]
'''
import sys
from collections import deque

n, m, k = list(map(int, sys.stdin.readline().split()))
maps = [list(sys.stdin.readline().split()[0]) for _ in range(n)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
q = deque([(0, 0, 1, 0)])
visited[0][0][0] = True

while q:
	x, y, cnt, wall = q.popleft()
	if (x, y) == (n-1, m-1):
		print(cnt)
		sys.exit()

	for dx, dy in directions:
		nxt_x, nxt_y = x + dx, y + dy

		if nxt_x not in range(0, n) or nxt_y not in range(0, m) or visited[wall][nxt_x][nxt_y]:
			continue

		if maps[nxt_x][nxt_y] == '0':
			q.append((nxt_x, nxt_y, cnt + 1, wall))
			visited[wall][nxt_x][nxt_y] = 1
		elif maps[nxt_x][nxt_y] == '1' and wall < k and not visited[wall+1][nxt_x][nxt_y]:
			q.append((nxt_x, nxt_y, cnt + 1, wall + 1))
			visited[wall+1][nxt_x][nxt_y] = 1
print(-1)

