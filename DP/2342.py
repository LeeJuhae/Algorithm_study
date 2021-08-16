# https://www.acmicpc.net/problem/2342

import sys
sys.setrecursionlimit(10**6)

def getCost(foot, direction):
	if foot:
		if foot == direction:
			return 1
		elif abs(foot - direction) == 2:
			return 4
		else:
			return 3
	else:
		return 2

def game(idx, left, right):
	if idx == n:
		return 0
	if dp[idx][left][right] != -1:
		return dp[idx][left][right]

	ret = float('inf')
	dp[idx][left][right] = \
		min(game(idx+1, left, arr[idx]) + getCost(right, arr[idx]), \
			game(idx+1, arr[idx], right) + getCost(left, arr[idx]))
	return dp[idx][left][right]

arr = list(map(int,sys.stdin.readline().split()))
n = len(arr) - 1
dp = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(100000)]
print(game(0, 0, 0))
