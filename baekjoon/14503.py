def cant_go(loc, room):
	directions = [[0,-1],[-1,0],[0,1],[1,0]]
	for direction in directions:
		check_loc = [x+y for x, y in zip(loc,direction)]
		if room[check_loc[0]][check_loc[1]] == 0:
			return False
	return True

def solution(n, m, r, c, d, room):
	cnt = 0
	rot = {0:[0,-1], 1:[-1,0], 2:[0,1], 3:[1,0]}
	back = {0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
	loc = [r, c]

	while True:
		room[loc[0]][loc[1]] = 2
		cnt += 1
		while True:
			next_loc = [x+y for x, y in zip(loc, rot[d])]
			if room[next_loc[0]][next_loc[1]] == 0:
				d = (d+3) % 4
				loc = next_loc
				break
			else:
				if cant_go(loc, room):
					back_loc = [x+y for x, y in zip(loc, back[d])]
					if room[back_loc[0]][back_loc[1]] != 1:
						loc = back_loc
					else:
						print(cnt)
						return
				else:
					d = (d+3) % 4

n, m = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))
room = []
for i in range(n):
	room.append(list(map(int, input().split())))
solution(n, m, r, c, d, room)
