# user_input = input()
# n, m = user_input.split(' ')
# user_input = input()
# r, c, d = user_input.split(' ')
# user_input = input()

# # print(n, m, r, c, d)
# print(user_input)

def solution(n, m, r, c, d, room):
	cnt = 0
	rot = {0:[0,-1], 1:[-1,0], 2:[0,1], 3:[1,0]}
	back = {0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
	loc = [r, c]
	visited = [0] * 4
	while True:
		print(loc, d)
		cnt += 1
		next_loc = [x+y for x, y in zip(loc, rot[d])]
		visited[d] = 1
		if room[next_loc[0]][next_loc[1]] == 0:
			room[loc[0]][loc[1]] = 1
			loc = next_loc
			d = (d+3) % 4
			cnt += 1
		else:
			if visited.count(1) >= 4:
				back_loc = [x+y for x, y in zip(loc, back[d])]
				if room[back_loc[0]][back_loc[1]] == 0:
					loc = back_loc
				else:
					break
			else:
				d = (d+3) % 4
	print(cnt)
# solution(11, 10, 7, 4, 0, [[1,1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,1,1,1,1,0,1],[1,0,0,1,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,1,0,1],[]])

# s = "1 0 0 0 0 0 0 1 0 1".replace(' ',',')

solution(11,10,7,4,0,[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 1, 1, 1, 1, 0, 1],[1, 0, 0, 1, 1, 0, 0, 0, 0, 1],[1, 0, 1, 1, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
