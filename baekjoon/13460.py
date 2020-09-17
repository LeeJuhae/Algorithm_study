import sys

def dfs(boards, blue, red, hole, cnt, min_cnt):
	directions = [[-1,0],[0,1],[1,0],[0,-1]]
	if cnt < 10:
		for d in directions:
			# print(blue, red, d)
			b_x, b_y = blue
			r_x, r_y = red
			d_x, d_y = d
			b_done, r_done = False, False
			b_fall, r_fall = False, False
			# print(blue, red, d, cnt)
			if d_x == 0 and b_x == r_x:
				if (d_y == -1 and b_y < r_y) or (d_y == 1 and r_y < b_y):
					while not b_done:
						# print(b_x ,b_y, d_x, d_y)
						if boards[b_x + d_x][b_y + d_y] == 'O':
							b_x += d_x
							b_y += d_y
							b_fall = True
							break
						elif boards[b_x+d_x][b_y + d_y] == '.':
							b_x += d_x
							b_y += d_y
						else:
							# b_x -= d_x
							# b_y -= d_y
							b_done = True
					while not r_done:
						if boards[r_x+d_x][r_y + d_y] == 'O':
							r_fall = True
							break
						elif [r_x + d_x, r_y + d_y] == [b_x, b_y]:
							break
						elif boards[r_x+d_x][r_y + d_y] == '.':
							r_x += d_x
							r_y += d_y
						else:
							# r_x -= d_x
							# r_y -= d_y
							r_done = True
				else:
					while not r_done:
						if boards[r_x+d_x][r_y + d_y] == 'O':
							r_x += d_x
							r_y += d_y
							r_fall = True
							break
						elif boards[r_x+d_x][r_y + d_y] == '.':
							r_x += d_x
							r_y += d_y
							# print("here")
						else:
							# r_x -= d_x
							# r_y -= d_y
							r_done = True
					while not b_done:
						if boards[b_x + d_x][b_y + d_y] == 'O':
							b_fall = True
							break
						elif [b_x+d_x, b_y+d_y] == [r_x, r_y]:
							break
						elif boards[b_x+d_x][b_y + d_y] == '.':
							b_x += d_x
							b_y += d_y
						else:
							# b_x -= d_x
							# b_y -= d_y
							b_done = True
			elif d_y == 0 and b_y == r_y:
				# print("?")
				if (d_x == -1 and b_x < r_x) or (d_x == 1 and r_x < b_x):
					while not b_done:
						if boards[b_x + d_x][b_y + d_y] == 'O':
							b_x += d_x
							b_y += d_y
							b_fall = True
							break
						elif boards[b_x+d_x][b_y + d_y] == '.':
							b_x += d_x
							b_y += d_y
						else:
							# b_x -= d_x
							# b_y -= d_y
							b_done = True
					while not r_done:
						if boards[r_x+d_x][r_y + d_y] == 'O':
							r_x += d_x
							r_y += d_y
							r_fall = True
							break
						elif [r_x + d_x, r_y + d_y] == [b_x, b_y]:
							break
						elif boards[r_x+d_x][r_y + d_y] == '.':
							r_x += d_x
							r_y += d_y
						else:
							# r_x -= d_x
							# r_y -= d_y
							r_done = True
				else:
					# print("here")
					while not r_done:
						if boards[r_x+d_x][r_y + d_y] == 'O':
							r_x += d_x
							r_y += d_y
							r_fall = True
							break
						elif boards[r_x+d_x][r_y + d_y] == '.':
							r_x += d_x
							r_y += d_y
						else:
							# r_x -= d_x
							# r_y -= d_y
							r_done = True
					while not b_done:
						# print(blue, red, d)
						if boards[b_x + d_x][b_y + d_y] == 'O':
							b_fall = True
							break
						elif [b_x+d_x, b_y+d_y] == [r_x, r_y]:
							break
						elif boards[b_x+d_x][b_y + d_y] == '.':
							b_x += d_x
							b_y += d_y
						else:
							# b_x -= d_x
							# b_y -= d_y
							b_done = True
			else:
				while True:
					if boards[b_x+d_x][b_y+d_y] == 'O':
						b_x += d_x
						b_y += d_y
						b_fall = True
						break
					elif boards[b_x+d_x][b_y+d_y] == '.':
						b_x += d_x
						b_y += d_y
					else:
						# b_x -= d_x
						# b_y -= d_y
						b_done = True
					if boards[r_x + d_x][r_y + d_y] == 'O':
						r_fall = True
						r_x += d_x
						r_y += d_y
						break
					elif [r_x+d_x, r_y+d_y] == [b_x,b_y]:
						break
					elif boards[r_x+d_x][r_y+d_y] == '.':
						r_x += d_x
						r_y += d_y
					else:
						r_done = True
					if r_done and b_done:
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
