from collections import deque, defaultdict

moves = [[-1,0], [0,1], [1,0], [0,-1]]
h_rotates = [[-1,1], [1,1], [-1,-1], [1,-1]] # _
v_rotates = [[1,-1], [1,1], [-1,-1], [-1,1]] # |

def isInside(l, r, N):
	if 0 <= l[0] < N  and 0 <= r[0] < N and 0 <= l[1] < N and 0 <= r[1] < N:
		return True
	return False

def canGo(l, r, board):
	if board[l[0]][l[1]] == 0 and board[r[0]][r[1]] == 0:
		return True
	return False

def canHRotate(idx, l, r, board):
	N = len(board)
	if idx < 2:
		if 0 <= l[1]-1 < N and board[l[0]][l[1]] == 0 and board[l[0]][l[1]-1] == 0:
			return True
	else:
		if 0 <= r[1]+1 < N and board[r[0]][r[1]] == 0 and board[r[0]][r[1]+1] == 0:
			return True
	return False

def canVRotate(idx, l, r, board):
	N = len(board)
	if idx < 2:
		if 0<= l[0]-1 < N and board[l[0]][l[1]] == 0 and board[l[0]-1][l[1]] == 0:
			return True
	else:
		if 0<= r[0]+1 < N and board[r[0]][r[1]] == 0 and board[r[0]+1][r[1]] == 0:
			return True

	return False

def solution(board):
	N = len(board)
	queue = deque()
	loc = ((0,0),(0,1))
	cost = 0
	queue.append([loc, cost])
	visit = defaultdict(dict)
	min_cost = float('inf')
	visit[loc] = cost
	while queue:
		loc, cost = queue.popleft()
		left, right = loc
		shape = 'h' if left[0] == right[0] else 'v'
		for move in moves:
			new_l = [i+j for i, j in zip(left, move)]
			new_r = [i+j for i, j in zip(right, move)]
			if isInside(new_l, new_r, N) and canGo(new_l, new_r, board):
				val = tuple(sorted([tuple(new_l), tuple(new_r)]))
				if new_l == [N-1,N-1] or new_r == [N-1,N-1]:
					min_cost = min(min_cost, cost + 1)
				elif visit.get(val) is None or visit.get(val) > cost + 1:
					visit[val] = cost + 1
					queue.append([val, cost + 1])
		if shape == 'h':
			for idx, rotate in enumerate(h_rotates):
				if idx < 2:
					new_l = [i+j for i, j in zip(left, rotate)]
					if isInside(new_l, right, N) and canHRotate(idx, new_l, right, board):
						val = tuple(sorted([tuple(new_l), tuple(right)]))
						if new_l == [N-1,N-1] or right == [N-1,N-1]:
							min_cost = min(min_cost, cost + 1)
						elif visit.get(val) is None or visit.get(val) > cost + 1:
							visit[val] = cost + 1
							queue.append([val, cost + 1])
				else:
					new_r = [i+j for i, j in zip(right, rotate)]
					if isInside(left, new_r, N) and canHRotate(idx, left, new_r, board):
						val = tuple(sorted([tuple(left), tuple(new_r)]))
						if left == [N-1,N-1] or  new_r == [N-1,N-1]:
							min_cost = min(min_cost, cost + 1)
						elif visit.get(val) is None or visit.get(val) > cost + 1:
							visit[val] = cost + 1
							queue.append([val, cost + 1])
		else:
			for idx, rotate in enumerate(v_rotates):
				if idx < 2:
					new_l = [i+j for i, j in zip(left, rotate)]
					if isInside(new_l, right, N) and canVRotate(idx, new_l, right, board):
						val = tuple(sorted([tuple(new_l), tuple(right)]))
						if new_l == [N-1,N-1] or right == [N-1,N-1]:
							min_cost = min(min_cost, cost + 1)
						elif visit.get(val) is None or visit.get(val) > cost + 1:
							visit[val] = cost + 1
							queue.append([val, cost + 1])
				else:
					new_r = [i+j for i, j in zip(right, rotate)]
					if isInside(left, new_r, N) and canVRotate(idx, left, new_r, board):
						val = tuple(sorted([tuple(left), tuple(new_r)]))
						if left == [N-1,N-1] or new_r == [N-1,N-1]:
							min_cost = min(min_cost, cost + 1)
						elif visit.get(val) is None or visit.get(val) > cost + 1:
							visit[val] = cost + 1
							queue.append([val, cost + 1])
	return min_cost


# print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]))
