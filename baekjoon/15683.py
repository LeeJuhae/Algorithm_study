from itertools import product
import copy

def get_directions(room):
	directions = []
	for r, row in enumerate(room):
		for c in range(len(row)):
			if room[r][c] == 2:
				directions.append([0,1])
			elif room[r][c] in [1,3,4]:
				directions.append([0,1,2,3])
	return directions

def watch(room, r, c, idx):
	if idx == 0:
		for i in range(c-1, -1, -1):
			if room[r][i] == 0 :
				room[r][i] = '#'
			# elif room[r][i] == 6:
			elif room[r][i] != '#':
				break
	elif idx == 1:
		for i in range(r-1, -1, -1):
			if room[i][c] == 0:
				room[i][c] = '#'
			# elif room[r][i] == 6:
			elif room[r][i] != '#':
				break
	elif idx == 2:
		for i in range(c+1,M):
			if room[r][i] == 0:
				room[r][i] = '#'
			# elif room[r][i] == 6:
			elif room[r][i] != '#':
				break
	elif idx == 3:
		for i in range(r+1, N):
			if room[i][c] == 0:
				room[i][c] = '#'
			# elif room[r][i] == 6:
			elif room[r][i] != '#':
				break
	return room

def watch_two(room, r ,c, idx):
	for i in range(idx, 4, 2):
		room = watch(room, r, c, i)
	return room

def watch_three(room, r, c, idx):
	for i in range(2):
		room = watch(room, r, c, (idx + i) % 4)
	return room

def watch_four(room, r, c, idx):
	for i in range(4):
		if i != idx:
			room = watch(room, r, c, i)
	return room

def watch_five(room):
	for r, row in enumerate(room):
		for c in range(len(row)):
			if room[r][c] == 5:
				for i in range(4):
					room = watch(room, r, c, i)
	return room

def get_blind_spot(room):
	cnt = 0
	for row in room:
		cnt += row.count(0)
	return cnt

def solution(room):
	room = watch_five(room)
	blind_spot = N * M
	directions = get_directions(room)
	product_items = list(product(*directions))

	for item in product_items:
		idx = 0
		copy_room = copy.deepcopy(room)
		for r, row in enumerate(copy_room):
			for c in range(len(row)):
				if copy_room[r][c] != '#' and copy_room[r][c] >= 1 and copy_room[r][c] <= 4:
					if copy_room[r][c] == 1:
						copy_room = watch(copy_room, r, c, item[idx])
					elif copy_room[r][c] == 2:
						copy_room = watch_two(copy_room, r, c, item[idx])
					elif copy_room[r][c] == 3:
						copy_room = watch_three(copy_room, r, c, item[idx])
					elif copy_room[r][c] == 4:
						copy_room = watch_four(copy_room, r, c, item[idx])
					idx += 1
		blind_spot = min(blind_spot, get_blind_spot(copy_room))
	return blind_spot

N, M = list(map(int, input().split()))
room = []
for _ in range(N):
	room.append(list(map(int, input().split())))
print(solution(room))
