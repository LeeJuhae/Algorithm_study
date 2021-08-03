# https://www.acmicpc.net/problem/11660

import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sum_arr = []
for i in range(n):
	temp = [0]
	for ele in arr[i]:
		temp.append(temp[-1] + ele)
	sum_arr.append(temp)

for _ in range(m):
	x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
	x = x2 - x1
	ans = 0
	for i in range(x + 1):
		ans += sum_arr[x1 + i - 1][y2] - sum_arr[x1 + i - 1][y1 - 1]
	print(ans)
