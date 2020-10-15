import sys
from collections import deque

def find_fish(boards, shark, size, cnt):
	directions = [[-1,0],[0,-1],[0,1],[1,0]]
	queue = deque([[shark, 0, size, cnt]]) # [상어 위치, 소요 시간, 상어 크기, 잡아 먹은 같은 크기의 물고기 수]
	visited = [[0 for _ in range(N)] for _ in range(N)]
	visited[shark[0]][shark[1]] = 1
	min_x, min_y = N, N
	min_time = float('inf')
	now_size = size
	now_cnt = cnt
	while queue:
		loc, time, size, cnt = queue.popleft()
		x, y = loc
		for direc in directions:
			new_x, new_y = [i+j for i, j in zip(loc, direc)]
			if 0 <= new_x < N and 0 <= new_y < N:
				if visited[new_x][new_y] == 0 and size >= boards[new_x][new_y]:
					visited[new_x][new_y] = 1
					if size == boards[new_x][new_y] or boards[new_x][new_y] == 0:
						queue.append([[new_x, new_y], time + 1, size, cnt])
					elif time + 1 <= min_time:
						if new_x < min_x or (new_x == min_x and new_y < min_y):
							min_x, min_y = new_x, new_y
							min_time = time + 1
							now_cnt = cnt + 1
							# 상어 크기 변경
							if cnt + 1 == size:
								now_size += 1
								now_cnt = 0
	fish = [min_x, min_y]
	if fish == [N, N]:
		return None, 0, 0, cnt
	else:
		return fish, min_time, now_size, now_cnt

N = int(sys.stdin.readline())
boards = []
loc = []
for _ in range(N):
	boards.append(list(map(int, sys.stdin.readline().split())))
	if 9 in boards[-1]:
		loc = [len(boards)-1, boards[-1].index(9)]
		boards[loc[0]][loc[1]] = 0
size = 2 # 아기 상어 크기
all_time = 0 # 소요 시간의 합
cnt = 0 # 잡아 먹은 같은 크기의 물고기 수
while True:
	fish, time, size, cnt = find_fish(boards, loc, size, cnt)
	if fish == None:
		break
	else:
		loc = fish
		boards[loc[0]][loc[1]] = 0
		all_time += time
print(all_time)
