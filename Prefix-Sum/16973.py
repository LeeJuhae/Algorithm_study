# https://www.acmicpc.net/problem/16973
# https://giiro.tistory.com/entry/BOJ-16973-%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95-%ED%83%88%EC%B6%9C

import sys
from collections import deque

ft_input = sys.stdin.readline
n, m = map(int, ft_input().split())
boards = [list(map(int, ft_input().split())) for _ in range(n)]
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
	for j in range(1, m + 1):
		dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + boards[i-1][j-1]
h, w, s_r, s_c, f_r, f_c = map(int, ft_input().split())
direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
queue = deque()
queue.append((s_r, s_c, 0))
visit = [[False for _ in range(m + 1)] for _ in range(n + 1)]
visit[s_r][s_c] = True

while queue:
	x, y, depth = queue.popleft()
	for d_x, d_y in direction:
		n_x, n_y, n_d = x + d_x, y + d_y, depth + 1
		a, b, c, d = n_x, n_y, n_x + h - 1, n_y + w - 1
		if a < 1 or b < 1 or c > n or d > m or visit[n_x][n_y]:
			continue
		if not (dp[c][d] - dp[c][b - 1] - dp[a - 1][d] + dp[a - 1][b - 1]):
			if n_x == f_r and n_y == f_c:
				print(n_d)
				sys.exit()
			queue.append((n_x, n_y, n_d))
			visit[n_x][n_y] = True
print(-1)
