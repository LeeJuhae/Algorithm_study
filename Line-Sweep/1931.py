# https://www.acmicpc.net/problem/1931

import sys

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
timeline = []
for _ in range(n):
	timeline.append(list(map(int, ft_input().split())))
timeline = sorted(timeline, key=lambda x: x[0])
timeline = sorted(timeline, key=lambda x: x[1])

cnt = 0
start = 0
for time in timeline:
	if time[0] >= start:
		cnt += 1
		start = time[1]
print(cnt)
