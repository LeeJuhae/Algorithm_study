'''
	Baekjoon - 14888. 연산자 끼워넣기
	삼성 SW 역량 테스트 기출 문제
	언어 : Python
	메모리 : 33,480kb
	실행시간 : 624ms
	코드길이 : 1028b
'''
import sys
from itertools import permutations

def sum(a, b):
	return a + b

def sub(a, b):
	return a - b

def mul(a, b):
	return a * b

def div(a, b):
	if a < 0:
		a *= -1
		res = a // b
		res *= -1
	else:
		res = a // b
	return res

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
sign_cnt = list(map(int, sys.stdin.readline().split()))
sign = ['+', '-', '*', '/']
sign_list = []

for idx, operator in enumerate(sign_cnt):
	if sign_cnt[idx] > 0:
		sign_list += [sign[idx] for _ in range(sign_cnt[idx])]
comb_sign = set(permutations(sign_list, len(sign_list)))
min_num = float('inf')
max_num = float('-inf')
for comb in comb_sign:
	num = numbers[0]
	for idx, operator in enumerate(comb):
		if operator == '+':
			num = sum(num, numbers[idx+1])
		elif operator == '-':
			num = sub(num, numbers[idx+1])
		elif operator == '*':
			num = mul(num, numbers[idx+1])
		else:
			num = div(num, numbers[idx+1])
	min_num = min(min_num, num)
	max_num = max(max_num, num)
print(max_num)
print(min_num)
