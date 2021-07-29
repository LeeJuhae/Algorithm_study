# https://www.acmicpc.net/problem/17071

'''
# key point
- n이 갈 수 있는 위치 => direction (0, 1, -1)로 표현
- visit[time % 2]
    : n이 n+1, n-1로 이동하며 갔던 위치에 또 가게 됨
    ex. time: 0 -> 4
        time: 1 -> 5 3 8
        time: 2 -> 4 6 10   2 4 6   7 9 16
        ...
    홀수 time에 갔던 곳은 홀수 time에 또다시 가게되고,
    짝수 time에 갔던 곳은 짝수 time에 또다시 가게 됨
'''

import sys
from collections import deque

n, k = list(map(int, sys.stdin.readline().split()))
max_range = 500000
visit = [[-1 for _ in range(max_range + 1)] for _ in range(2)]
directions = (0, 1, -1)
q = deque()
q.append((n, 0, k))
ret = -1
visit[0][n] = 0

while q:
    n_pos, time, k_pos = q.popleft()

    if visit[time % 2][k_pos] != -1 and visit[time % 2][k_pos] <= time:
        ret = time
        break

    for direction in directions:
        next_n_pos = n_pos + direction if direction else 2 * n_pos
        next_time = time + 1
        next_k_pos = k_pos + next_time

        if next_n_pos < 0 or next_n_pos > max_range or next_k_pos > max_range or visit[next_time % 2][next_n_pos] != -1:
            continue
        q.append((next_n_pos, next_time, next_k_pos))
        visit[next_time % 2][next_n_pos] = next_time
print(ret)
