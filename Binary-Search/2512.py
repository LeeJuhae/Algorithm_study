# https://www.acmicpc.net/problem/2512

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
budget = int(sys.stdin.readline().rstrip())

left, right = 1, max(arr)
ret = 0
while left <= right:
	mid = (left + right) // 2
	sum_b = 0
	for ele in arr:
		sum_b += min(ele, mid)
	if sum_b <= budget:
		left = mid + 1
		ret = mid
	else:
		right = mid - 1
print(ret)
