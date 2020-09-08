import sys
import copy
from collections import deque
sys.setrecursionlimit(10**6)

def isDivided(N, M, iceberg):
	check = [[0 for _ in range(M)] for _ in range(N)]
	queue = deque()
	directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
	i, j, flag = 0, 0, 1
	while flag < 3 and i < N and j < M:
		if iceberg[i][j] != 0 and check[i][j] == 0:
			queue.append([i,j])
			while queue:
				x, y = queue.popleft()
				check[x][y] = flag
				for direction in directions:
					new_x, new_y = [a+b for a, b in zip([x,y],direction)]
					if 0 <= new_x < N and 0 <= new_y < M and iceberg[new_x][new_y] != 0 and check[new_x][new_y] == 0:
						queue.append([new_x, new_y])
			flag += 1
		if j == M-1:
			i += 1
			j = 0
		else:
			j += 1
	del check
	return True if flag >= 3 else False

def isAllMelted(iceberg):
	for row in iceberg:
		if max(row) != 0:
			return False
	return True

def canNotMelt(iceberg):
	for row in iceberg:
		if row.count(0) > 0:
			return False
	return True

def melt(N, M, iceberg):
	year = 0
	directions = [[-1,0], [0, 1], [1, 0], [0, -1]]
	queue = deque()
	while True:
		if isAllMelted(iceberg) or canNotMelt(iceberg):
			return 0
		year += 1
		for i in range(N):
			for j in range(M):
				if iceberg[i][j] != 0:
					melting_cnt = 0
					for direction in directions:
						r, c = i + direction[0], j + direction[1]
						if 0 <= r < N and 0 <= c < M and iceberg[r][c] == 0 and iceberg[i][j] >= melting_cnt :
							melting_cnt += 1
					if melting_cnt != 0:
						queue.append([i,j,melting_cnt])
		while queue:
			i, j, cnt = queue.popleft()
			iceberg[i][j] -= cnt
		if isDivided(N, M, iceberg):
			break
	return year

if __name__ == "__main__":
	N, M = map(int, sys.stdin.readline().split())
	iceberg = []
	for _ in range(N):
		iceberg.append(list(map(int, sys.stdin.readline().split())))
	print(melt(N, M, iceberg))
