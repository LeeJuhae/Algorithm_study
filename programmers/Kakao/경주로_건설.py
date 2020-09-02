def solution(board):
	N = len(board)
	movings = [[-1,0],[0,1],[1,0],[0,-1]]
	queue = [(0,0,-1,0)]
	visit = {(0,0,0):0, (0,0,1):0, (0,0,2):0, (0,0,3):0}
	min_cost = float('inf')
	while len(queue) != 0:
		x, y, direc, cost = queue.pop(0)
		for idx, moving in enumerate(movings):
			new_x, new_y = [i+j for i, j in list(zip([x, y], moving))]
			new_direc = idx
			if 0 <= new_x < N and 0 <= new_y < N and not board[new_x][new_y]:
				if direc == -1 or abs(direc-new_direc) % 2 == 0:
					new_cost = cost + 100
				else:
					new_cost = cost + 600
				if new_x == N-1 and new_y == N-1:
					min_cost = min(min_cost, new_cost)
				elif visit.get((new_x, new_y, new_direc)) is None or visit.get((new_x, new_y, new_direc)) > new_cost:
					visit[(new_x, new_y, new_direc)] = new_cost
					queue.append((new_x, new_y, new_direc, new_cost))
	return min_cost

# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
