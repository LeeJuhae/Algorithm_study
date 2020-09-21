import sys
import copy

def plus(boards, not_zero, r, c):
	if boards[r][c] != 0:
		if not_zero == [-1, -1]:
			not_zero = [r, c]
		elif boards[r][c] == boards[not_zero[0]][not_zero[1]]:
			boards[not_zero[0]][not_zero[1]] *= 2
			boards[r][c] = 0
			not_zero = [-1, -1]
		else:
			not_zero = [r, c]
	return boards, not_zero

def move(boards, d):
	if d % 2 == 0:
		if d == 0:
			r, c = 0, 0
			while c < N:
				not_zero = [-1, -1]
				while r < N:
					boards, not_zero = plus(boards, not_zero, r, c)
					r += 1
				c += 1
				r = 0
		elif d == 2:
			r, c = N-1, 0
			while c < N:
				not_zero = [-1, -1]
				while r >= 0:
					boards, not_zero = plus(boards, not_zero, r, c)
					r -= 1
				c += 1
				r = N-1
		new_boards = []
		for i in range(N):
			new_boards.append([row[i] for row in boards if row[i] != 0])
			if d == 0:
				new_boards[-1] += [0 for _ in range(N-len(new_boards[-1]))]
			else:
				new_boards[-1] = [0 for _ in range(N-len(new_boards[-1]))] + new_boards[-1]
		boards = [[] for _ in range(N)]
		for i in range(N):
			for j in range(N):
				boards[j % N].append(new_boards[i][j])
	elif d == 1:
		r, c = 0, 0
		while r < N:
			not_zero = [-1, -1]
			while c < N:
				boards, not_zero = plus(boards, not_zero, r, c)
				c += 1
			r += 1
			c = 0
		for r in range(N):
			boards[r] = list(filter(lambda x: x != 0, boards[r]))
			boards[r] += [0 for _ in range(N-len(boards[r]))]
	elif d == 3:
		r, c = 0, N-1
		while r < N:
			not_zero = [-1, -1]
			while c >= 0:
				boards, not_zero = plus(boards, not_zero, r, c)
				c -=1
			r += 1
			c = N-1
		for r in range(N):
			boards[r] = list(filter(lambda x: x != 0, boards[r]))
			boards[r] = [0 for _ in range(N-len(boards[r]))] + boards[r]
	return boards

def play(boards, rot_cnt, max_value):
	if rot_cnt >= 5:
		now_max = 0
		for row in boards:
			now_max = max(now_max, max(row))
		max_value = max(now_max, max_value)
	else:
		direcitions = [[-1,0],[0,1],[1,0],[0,-1]]
		for d_idx in range(4):
			temp = copy.deepcopy(boards)
			temp = move(temp, d_idx)
			max_value = play(temp, rot_cnt + 1, max_value)
	return max_value

N = int(sys.stdin.readline())
boards = []
for _ in range(N):
	boards.append(list(map(int, sys.stdin.readline().split())))
print(play(boards, 0, 0))
