# https://www.acmicpc.net/problem/2467

import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))

left, right = 0, n - 1
ret = [numbers[left], numbers[right]]
while left < right:
	sum_val = numbers[left] + numbers[right]
	if abs(sum_val) < abs(sum(ret)):
		ret = [numbers[left], numbers[right]]
		if abs(sum_val) == 0:
			break
	if sum_val < 0: left += 1
	else: right -= 1
print(ret[0], ret[1])


