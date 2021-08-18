import sys

'''
시간 초과났던 이유: 출력 포맷을 맞추기 위해 리스트를 문자열로 만들었기 때문
수정 전 출력 코드:
	return = []
	return.append(upper_bound() - lower_bound())
	print(' '.join(str(ele) for ele in return))
'''

# return: number 이상의 값이 시작되는 idx
def lower_bound(number):
	left, right = 0, len(cards) - 1
	while left <= right:
		mid = int((left + right) / 2)
		if number <= cards[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return left

# return: number 초과의 값이 시작되는 idx
def upper_bound(number):
	left, right = 0, len(cards) - 1
	while left <= right:
		mid = int((left + right) / 2)
		if number >= cards[mid]:
			left = mid + 1
		else:
			right = mid - 1
	return left

n = sys.stdin.readline().rstrip()
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = sys.stdin.readline().rstrip()
numbers = list(map(int, sys.stdin.readline().split()))

for idx, number in enumerate(numbers):
	if idx == len(numbers) - 1:
		print(upper_bound(number) - lower_bound(number), end='')
	else:
		print(upper_bound(number) - lower_bound(number), end=' ')

