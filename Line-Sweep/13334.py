# https://www.acmicpc.net/problem/13334

'''
line을 종료 지점을 기준으로 sort하고 heapq(우선순위 큐)에 시작 지점을 넣는 것과
line을 종료 지점, 시작 지점을 기준으로 미리 sort하는 것의 차이점은?
'''

import sys
from heapq import heappush, heappop

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
lines = []
for _ in range(n):
	lines.append(sorted(list(map(int, ft_input().split()))))
d = int(ft_input().rstrip())
lines = sorted(list(filter(lambda x: x[1] - x[0] <= d, lines)), key=lambda x: x[1])
max_cnt = 0
if len(lines) > 0:
	queue = []
	for line in lines:
		heappush(queue, line[0])
		while queue and line[1] - queue[0] > d:
			heappop(queue)
		max_cnt = max(max_cnt, len(queue))
print(max_cnt)
