'''
	Baekjoon - 7576. 토마토
	언어 : Python
	메모리 : 106,272kb
	실행시간 : 3656ms
	코드길이 : 823b
'''
import sys
from collections import deque

def keep_in_storage(tomatoes, ripe_tomatoes):
	days = -1
	while ripe_tomatoes:
		days += 1
		for _ in range(len(ripe_tomatoes)):
			ripe_tomato = ripe_tomatoes.popleft()
			for direction in directions:
				x, y = [i+j for i, j in zip(ripe_tomato, direction)]
				if 0 <= x < M and 0 <= y < N and tomatoes[x][y] == 0:
					tomatoes[x][y] = 1
					ripe_tomatoes.append([x,y])
	for tomato in tomatoes:
		if 0 in tomato:
			return -1
	return days

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ripe_tomatoes = deque()
tomatoes = []
N, M = map(int,sys.stdin.readline().split())
for i in range(M):
	tomatoes.append(list(map(int, sys.stdin.readline().split())))
	for j in range(N):
		if tomatoes[i][j] == 1:
			ripe_tomatoes.append([i,j])
print(keep_in_storage(tomatoes, ripe_tomatoes))
