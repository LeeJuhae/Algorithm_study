# https://www.acmicpc.net/problem/10815

import sys

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
cards = sorted(list(map(int, ft_input().split())))
m = int(ft_input().rstrip())
numbers = list(map(int, ft_input().split()))

def upper_bound(number):
	left, right = 0, n - 1
	while left <= right:
		mid = (left + right) // 2
		if number > cards[mid]:
			left = mid + 1
		elif number == cards[mid]:
			return 1
		else:
			right = mid - 1
	return 0

for number in numbers:
	print(upper_bound(number), end=' ')
