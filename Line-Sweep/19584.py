# https://www.acmicpc.net/problem/19584

import sys
from collections import defaultdict

ft_input = sys.stdin.readline
n, m = map(int, ft_input().split())
locations = []
costs = defaultdict(int)
for _ in range(n):
	locations.append(list(map(int, ft_input().split())))
for _ in range(m):
	s, e, c = map(int, ft_input().split())
	s, e = locations[s - 1][1], locations[e - 1][1]
	s, e = min(s, e), max(s, e)
	'''
	s부터는 +c이고,
	e를 넘어선 좌표 즉, e + 1부터는 -c를 뺌.
	'''
	costs[s] += c
	costs[e + 1] -= c
ans = 0
temp = 0
for ele in sorted(costs.items()):
	temp += ele[1]
	ans = max(ans, temp)
print(ans)

