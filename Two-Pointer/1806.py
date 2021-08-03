# https://www.acmicpc.net/problem/1806

import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
s, e = 0, 1
sum_val, len_val = numbers[s] + numbers[e], float('inf')
while s <= e:
	if sum_val < m:
		e += 1
		if e == n: break
		sum_val += numbers[e]
	else:
		len_val = min(len_val, e-s+1)
		sum_val -= numbers[s]
		s += 1
print(0 if len_val == float('inf') else len_val)
