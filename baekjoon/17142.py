import sys
from itertools import combinations
import copy
from collections import deque

def spread(boards, now_virus, min_time):
	directions = [[-1,0],[0,1],[1,0],[0,-1]]
	time = -1
	queue = deque(now_virus)
	visited = copy.deepcopy(boards)
	while queue:
		x, y, t = queue.popleft()
		if t >= min_time:
			return min_time
		visited[x][y] = 1
		for d in directions:
			new_x, new_y = [i+j for i,j in zip(d,[x,y])]
			if 0 <= new_x < N and 0 <= new_y < N and boards[new_x][new_y] == 0:
				boards[new_x][new_y] = 2
				queue.append([new_x, new_y, t + 1])
		time = t
	for row in visited:
		if row.count(0) > 0:
			return -1
	return time

def select_virus(N, M, boards, candi_virus):
	comb_inactive_virus = list(combinations(candi_virus, len(candi_virus)-M))
	min_time = float('inf')
	for selected_virus in comb_inactive_virus:
		new_boards = copy.deepcopy(boards)
		now_virus = []
		for virus in candi_virus:
			if virus not in selected_virus:
				now_virus.append(virus + [0])
			else:
				new_boards[virus[0]][virus[1]] = '*'
		time = spread(new_boards, now_virus, min_time)
		if time != -1:
			min_time = time
	if min_time == float('inf'):
		min_time = -1
	return min_time

N, M = map(int, sys.stdin.readline().split())
boards = []
candi_virus = []
for row in range(N):
	boards.append(list(map(int ,sys.stdin.readline().split())))
	for col in range(N):
		if boards[row][col] == 2:
			candi_virus.append([row, col])
		elif boards[row][col] == 1:
			boards[row][col] = '-'
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
