# https://www.acmicpc.net/problem/10942

import sys

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
numbers = list(map(int, ft_input().split()))
m = int(ft_input().rstrip())
dp = [[None for _ in range(n)] for _ in range(n)]

def isPalindrome(start, end):
	if start >= end:
		return 1

	if dp[start][end] != None:
		return dp[start][end]

	if numbers[start] == numbers[end]:
		ret = isPalindrome(start + 1, end - 1)
	else:
		ret = 0
	dp[start][end] = ret
	return ret

for i in range(n):
	dp[i][i] = 1
	for j in range(i + 1, n):
		isPalindrome(i, j)

for _ in range(m):
	s, e = map(int,ft_input().split())
	print(dp[s-1][e-1])
