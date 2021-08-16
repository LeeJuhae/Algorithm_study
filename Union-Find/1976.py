# https://www.acmicpc.net/problem/1976

import sys
from collections import defaultdict

def find(a):
	if a == parents[a]:
		return a
	parents[a] = find(parents[a])
	return parents[a]

def union(a, b):
	a_parent = find(a)
	b_parent = find(b)
	if a_parent < b_parent:
		parents[b_parent] = a_parent
	else:
		parents[a_parent] = b_parent

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
m = int(ft_input().rstrip())
parents = [i for i in range(n)]

for i in range(n):
	row = list(map(int, ft_input().split()))
	for j in range(n):
		if row[j]:
			if find(i) != find(j):
				union(i, j)

plans = list(map(int, ft_input().split()))
p = parents[plans[0] - 1]
ans = 'YES'
for plan in plans[1:]:
	if p != find(plan - 1):
		ans = 'NO'
		break
print(ans)
