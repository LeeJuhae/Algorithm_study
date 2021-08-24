# https://www.acmicpc.net/problem/1931

import sys

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
timeline = []
for _ in range(n):
	timeline.append(list(map(int, ft_input().split())))
# 일찍 시작하고 일찍 끝나는 순서로 정렬
timeline = sorted(timeline, key=lambda x: (x[1], x[0]))
cnt = 0
start = 0
for time in timeline:
	if time[0] >= start:
		cnt += 1
		start = time[1]
print(cnt)

'''
- 정렬 방법에 따른 결과 차이

ex.
timeline = [[2, 4], [2, 3], [1, 3], [1, 4], [1, 2]]

# 정답
1.
timeline = sorted(timeline, key=lambda x: (x[1], x[0]))
1, 2 -> 1, 3 -> 2, 3 -> 1, 4 -> 2, 4

2.
timeline = sorted(timeline, key=lambda x: x[0])
timeline = sorted(timeline, key=lambda x: x[1])
1, 3 -> 1, 4 -> 1, 2 -> 2, 4 -> 2, 3
1, 2 -> 1, 3 -> 2, 3 -> 1, 4 -> 2, 4

# 오답
3.
timeline = sorted(timeline, key=lambda x: (x[0], x[1]))
1, 2 -> 1, 3 -> 1, 4 -> 2, 3 -> 2, 4

4.
timeline = sorted(timeline, key=lambda x: x[1])
timeline = sorted(timeline, key=lambda x: x[0])
1, 2 -> 2, 3 -> 1, 3 -> 2, 4 -> 1, 4
1, 2 -> 1, 3 -> 1, 4 -> 2, 3 -> 2, 4
'''
