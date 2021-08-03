# https://www.acmicpc.net/problem/2559

import sys

n, k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
arr = [0]
for num in numbers:
	arr.append(arr[-1] + num)

s, e = 0, 0 + k
ret = -float('inf')
while e < len(arr):
	ret = max(ret, arr[e] - arr[s])
	s += 1
	e = s + k
print(ret)
