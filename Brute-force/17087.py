# https://www.acmicpc.net/problem/17087

import sys
from collections import deque

def gcd(x, y):
	if not y: return x
	return gcd(y, x % y)

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = abs (arr[0] - s)

for ele in arr[1:]:
	ans = gcd(ans, abs(ele - s))
print(ans)
