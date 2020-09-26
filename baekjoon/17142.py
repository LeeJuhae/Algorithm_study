import sys
from itertools import combinations
import copy
from collections import deque

def spread(boards, now_virus):
	directions = [[-1,0],[0,1],[1,0],[0,-1]]
	time = 0
	queue = deque(now_virus)
	visited = [[0 for _ in range(N)] for _ in range(N)]
	for virus in now_virus:
		visited[virus[0]][virus[1]] = 1
	while queue:
		x, y, t = queue.popleft()
		for d in directions:
			new_x, new_y = d[0] + x, d[1] + y
			if 0 <= new_x < N and 0 <= new_y < N:
				if boards[new_x][new_y] != 1 and visited[new_x][new_y] == 0:
					if boards[new_x][new_y] != 2:
						time = t + 1
					boards[new_x][new_y] = 2
					visited[new_x][new_y] = 1
					queue.append([new_x, new_y, t + 1])
	for row in boards:
		if 0 in row:
			return -1
	return time

def select_virus(N, M, boards, candi_virus):
	comb_inactive_virus = list(combinations(candi_virus, M))
	time = float('inf')
	for selected_virus in comb_inactive_virus:
		new_boards = copy.deepcopy(boards)
		time = min(time, spread(new_boards, selected_virus))
		if time != -1:
			min_time = time
	return min_time if min_time != float('inf') else -1

N, M = map(int, sys.stdin.readline().split())
boards = []
candi_virus = []
for row in range(N):
	boards.append(list(map(int ,sys.stdin.readline().split())))
	for col in range(N):
		if boards[row][col] == 2:
			candi_virus.append([row, col, 0])
print(select_virus(N, M, boards, candi_virus))
