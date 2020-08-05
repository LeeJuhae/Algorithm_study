def isAllCleaned(loc, room):
	# print(loc, room)
	directions = [[0,-1],[-1,0],[0,1],[1,0]]
	for direction in directions:
		check_loc = [x+y for x, y in zip(loc,direction)]
		# print(room[check_loc[0]][check_loc[1]], check_loc[0], check_loc[1])
		if room[check_loc[0]][check_loc[1]] == 0:
			return False
	return True

# def print_room(room):
# 	for row in room:
# 		print(row)

def solution(n, m, r, c, d, room):
	cnt = 0
	rot = {0:[0,-1], 1:[-1,0], 2:[0,1], 3:[1,0]}
	back = {0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
	loc = [r, c]
	# a = 0
	while True:
		room[loc[0]][loc[1]] = 2
		# print("room:")
		# print_room(room)
		cnt += 1
		while True:
			next_loc = [x+y for x, y in zip(loc, rot[d])]
			# print(loc, d, cnt)
			# print(next_loc)

			if room[next_loc[0]][next_loc[1]] == 0:
				# room[loc[0]][loc[1]] = 1
				d = (d+3) % 4
				loc = next_loc
				break
				# cnt += 1
			else:
				if isAllCleaned(loc, room):
					back_loc = [x+y for x, y in zip(loc, back[d])]
					# print(loc)
					if room[back_loc[0]][back_loc[1]] != 1:
						loc = back_loc
					else:
						print(cnt)
						return
						# return (cnt)
				else:
					d = (d+3) % 4
			# print_room(room)
			# a += 1
			# if a > 10:
			# 	return
		# break
	# print(cnt)
# solution(3,3,1,1,0,[[1,1,1],[1,0,1],[1,1,1]])
# solution(11,10,7,4,0,[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 1, 1, 1, 1, 0, 1],[1, 0, 0, 1, 1, 0, 0, 0, 0, 1],[1, 0, 1, 1, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],[1, 0, 0, 0, 0, 0, 1, 1, 0, 1],[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

user_input = input()
print(user_input)
# n, m =
# user_input = input()
# r, c, d = user_input.split(' ')
# # user_input = input()
# print(n, m, r, c, d)
