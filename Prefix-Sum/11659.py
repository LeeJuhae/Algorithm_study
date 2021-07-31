# https://www.acmicpc.net/problem/11659

import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

sum_arr = [0]
for num in numbers:
	sum_arr.append(sum_arr[-1] + num)

for _ in range(m):
	s, e = map(int, sys.stdin.readline().split())
	print(sum_arr[e] - sum_arr[s-1])
