import sys

def dfs(boards, blue, red, hole, cnt, min_cnt):
	directions = [[-1,0],[0,1],[1,0],[0,-1]]
	if cnt >= 10:
		if min_cnt == float('inf'):
			min_cnt = -1
	else:
		for d in directions:
			b_x, b_y = blue
			r_x, r_y = red
			d_x, d_y = d
			b_fall, r_fall = False, False
			while True:
				isMove = False
				while not b_fall:
					if boards[b_x][b_y] == 'O':
						b_fall = True
						break
					elif boards[b_x + d_x][b_y + d_y] != '#' and (r_fall or  [b_x +d_x,b_y + d_y] != [r_x, r_y]):
						b_x += d_x
						b_y += d_y
						isMove = True
					else:
						break
				if b_fall:
					break
				while not r_fall:
					if boards[r_x][r_y] == 'O':
						r_fall = True
						break
					elif boards[r_x + d_x][r_y + d_y] != '#' and [r_x+d_x, r_y+d_y] != [b_x, b_y]:
						r_x += d_x
						r_y += d_y
						isMove = True
					else:
						break
				if not isMove:
					break
			if not b_fall:
				if r_fall:
					if min_cnt != -1:
						min_cnt = min(min_cnt, cnt + 1)
					else:
						min_cnt = cnt + 1
				else:
					min_cnt = dfs(boards, [b_x, b_y], [r_x, r_y], hole, cnt + 1, min_cnt)
			else:
				if min_cnt == float('inf'):
					min_cnt = -1
	return min_cnt

N, M = map(int, sys.stdin.readline().split())
boards, blue, red, hole = [], [], [], []
for _ in range(N):
	boards.append(list(sys.stdin.readline().rstrip()))
for i in range(N):
	for j in range(M):
		if boards[i][j] == 'B':
			blue = [i, j]
			boards[i][j] = '.'
		elif boards[i][j] == 'R':
			red = [i, j]
			boards[i][j] = '.'
		elif boards[i][j] == 'O':
			hole = [i, j]
print(dfs(boards, blue, red, hole, 0, float('inf')))
