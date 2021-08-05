# https://www.acmicpc.net/problem/1937

'''
# key point

sys.setrecursionlimit(2000)
: 재귀의 깊이를 최대 2000으로 정해줌. (n <= 500)
'''
import sys
from collections import deque
sys.setrecursionlimit(2000)

def dfs(x, y):
	if dp[x][y] != -1:
		return dp[x][y]
	ret = 1
	for d_x, d_y in directions:
		next_x, next_y = x + d_x, y + d_y
		if next_x not in range(n) or next_y not in range(n):
			continue
		if arr[next_x][next_y] > arr[x][y]:
			ret = max(ret, dfs(next_x, next_y) + 1)
	dp[x][y] = ret
	return ret

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
max_val = 0
for start_x in range(n):
	for start_y in range(n):
		max_val = max(max_val, dfs(start_x, start_y))
print(max_val)
