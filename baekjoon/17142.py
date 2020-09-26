import sys
from itertools import combinations
import copy
from collections import deque

def spread(boards, now_virus, min_time):
	directions = [[-1,0],[0,1],[1,0],[0,-1]]
	time = 0
	queue = deque(now_virus)
	visited = [[0 for _ in range(N)] for _ in range(N)]
	for virus in now_virus:
		visited[virus[0]][virus[1]] = 1
	while queue:
		x, y, t = queue.popleft()
		if time >= min_time:
			return min_time
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
	min_time = float('inf')
	for selected_virus in comb_inactive_virus:
		new_boards = copy.deepcopy(boards)
		time = spread(new_boards, selected_virus, min_time)
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


# import sys
# from itertools import combinations
# import copy

# def spread(boards):
# 	directions = [[-1,0],[0,1],[1,0],[0,-1]]
# 	time = 0
# 	while True:
# 		cnt = 0
# 		new_boards = copy.deepcopy(boards)
# 		for x in range(N):
# 			for y in range(N):
# 				if boards[x][y] == 2:
# 					for d in directions:
# 						new_x, new_y = [i+j for i,j in zip(d,[x,y])]
# 						if 0 <= new_x < N and 0 <= new_y < N and boards[new_x][new_y] == 0:
# 							new_boards[new_x][new_y] = 2
# 							cnt += 1
# 		if cnt == 0:
# 			for row in boards:
# 				if row.count(0) > 0:
# 					time = -1
# 					break
# 			break
# 		time += 1
# 		boards = new_boards
# 	return time

# def select_virus(N, M, boards, candi_virus):
# 	comb_inactive_virus = list(combinations(candi_virus, len(candi_virus)-M))
# 	min_time = float('inf')
# 	for selected_virus in comb_inactive_virus:
# 		new_boards = copy.deepcopy(boards)
# 		for inacitve_virus in selected_virus:
# 			new_boards[inacitve_virus[0]][inacitve_virus[1]] = '*'
# 		time = spread(new_boards)
# 		if time != -1:
# 			min_time = min(min_time, time)
# 	if min_time == float('inf'):
# 		min_time = -1
# 	return min_time

# N, M = map(int, sys.stdin.readline().split())
# boards = []
# candi_virus = []
# for row in range(N):
# 	boards.append(list(map(int ,sys.stdin.readline().split())))
# 	for col in range(N):
# 		if boards[row][col] == 2:
# 			candi_virus.append([row, col])
# 		elif boards[row][col] == 1:
# 			boards[row][col] = '-'
# print(select_virus(N, M, boards, candi_virus))
