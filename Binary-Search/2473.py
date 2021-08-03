# https://www.acmicpc.net/problem/2473

import sys

n = int(sys.stdin.readline().rstrip())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

ans = [float('inf'), float('inf'), float('inf')]
for i in range(n-2):
	left, right = i + 1, n - 1
	temp_ans = [numbers[i], numbers[left], numbers[right]]
	min_abs = sum(temp_ans)
	while left < right:
		temp_sum = numbers[i] + numbers[left] + numbers[right]
		if abs(min_abs) > abs(temp_sum):
			temp_ans = [numbers[i], numbers[left], numbers[right]]
			min_abs = temp_sum
			if min_abs == 0:
				break
		if temp_sum < 0: left += 1
		else: right -= 1
	if abs(sum(ans)) > abs(min_abs):
		ans = temp_ans
		if abs(sum(ans)) == 0:
			break
print(ans[0], ans[1], ans[2])
