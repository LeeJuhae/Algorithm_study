def check_two_layer_block(board, r, c, cols):
	ele = board[r][c]
	N = len(board)
	if r < N - 1:
		if c > 0 and c < N - 1:
			if board[r+1][c-1:c+2] == [ele, ele, ele]:
				if board[r][c-1] == 0 and board[r][c+1] == 0:
					if c-1 not in cols and c+1 not in cols:
						board[r][c] = 0
						board[r+1][c-1], board[r+1][c], board[r+1][c+1] = 0, 0, 0
						return board, 1
		if c < N - 2:
			if board[r+1][c:c+3] == [ele, ele, ele]:
				if board[r][c+1] == 0 and board[r][c+2] == 0:
					if c+1 not in cols and c+2 not in cols:
						board[r][c] = 0
						board[r+1][c], board[r+1][c+1], board[r+1][c+2] = 0, 0, 0
						return board, 1
		if c >= 2:
			if board[r+1][c-2:c+1] == [ele, ele, ele]:
				if board[r][c-2] == 0 and board[r][c-1] == 0:
					if c-2 not in cols and c-1 not in cols:
						board[r][c] = 0
						board[r+1][c-2], board[r+1][c-1], board[r+1][c] = 0, 0, 0
						return board, 1
	return board, 0

def check_three_layer_block(board, r, c, cols):
	ele = board[r][c]
	N = len(board)
	if r < N - 2:
		if c < N - 1:
			if board[r+1][c] == ele and board[r+2][c] == ele and board[r+2][c+1] == ele:
				if board[r][c+1] == 0 and board[r+1][c+1] == 0:
					if c+1 not in cols:
						board[r][c] = 0
						board[r+1][c], board[r+2][c], board[r+2][c+1] = 0, 0, 0
						return board, 1
		if c > 0:
			if board[r+1][c] == ele and board[r+2][c] == ele and board[r+2][c-1] == ele:
				if board[r][c-1] == 0 and board[r+1][c-1] == 0:
					if c-1 not in cols:
						board[r][c] = 0
						board[r+1][c], board[r+2][c], board[r+2][c-1] = 0, 0, 0
						return board, 1
	return board, 0

def solution(board):
	cnt, pre_cnt = 0, 0
	while True:
		cols = set()
		move_cnt = 0
		for r, row in enumerate(board):
			for c, ele in enumerate(row):
				if ele != 0:
					board, move_cnt = check_two_layer_block(board, r, c, cols)
					if move_cnt == 0:
						board, move_cnt = check_three_layer_block(board, r, c, cols)
					if move_cnt == 0:
						cols.add(c)
					cnt += move_cnt
		if pre_cnt == cnt:
			break
		pre_cnt = cnt
	return cnt

# print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))
