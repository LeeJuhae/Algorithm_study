# https://www.acmicpc.net/problem/11000

import sys
import heapq

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
timeline = []
for _ in range(n):
	timeline.append(list(map(int, ft_input().split())))
timeline.sort() # 시작 시간 기준 정렬
room = []
heapq.heappush(room, timeline[0][1]) # 종료 시간 기준 우선순위 큐

for time in timeline[1:]:
	if time[0] < room[0]:
		heapq.heappush(room, time[1])
	else:
		heapq.heappop(room)
		heapq.heappush(room, time[1])
print(len(room))
