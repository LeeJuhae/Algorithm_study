import sys
from collections import deque

def get_cnt(pieces, board):
	cnt = 0
	for piece in pieces:
		if piece in board:
			cnt += 1
	return cnt

def isDuplicate(pieces):
	boards = [[[10, 4], [20, 3], [30, 4]], [[10, 5], [20, 4], [30, 5]], [[10, 6], [20, 5], [30, 6]], [[0, 20], [10, 7], [20, 6], [30, 7]]]
	for board in boards:
		if get_cnt(pieces, board) > 1:
			return True
	return False

def play(dice, pieces):
	way = \
	{ 0 : [i*2 for i in range(21)],
	 10 : [10, 13, 16, 19, 25, 30, 35, 40],
	 20 : [20, 22, 24, 25, 30, 35, 40],
	 30 : [30, 28, 27, 26, 25, 30, 35, 40]
	}
	queue = deque([[pieces, 0, 0]])
	d_idx = 0
	all_sum = 0
	while queue:
		piece, d_idx, temp_sum = queue.popleft()
		if d_idx < 10:
			for i in range(4):
				key, value = piece[i]
				# 도착지점에 도착한 말일 경우
				if key == -1:
					continue
				# 2씩 증가하다 10, 20, 30에 도착한 경우
					# key를 10, 20, 30으로 바꿔주고 value를 0으로 초기화
				if key == 0 and value + dice[d_idx] in [5, 10, 15]:
					key = 2 * (value + dice[d_idx])
					value = 0
				# 도착지점을 지날 경우 key, value = -1, -1
				elif len(way[piece[i][0]]) <= piece[i][1] + dice[d_idx]:
					key = -1
					value = -1
				else:
					key = piece[i][0]
					value = piece[i][1] + dice[d_idx]
				# 바뀐 말의 위치가 적용된 말들의 위치 리스트
				temp = piece[:i] + [[key, value]] + piece[i+1:]
				# 25, 30, 35, 40에 위치한 말이 2개 이상일 경우 pass
				if isDuplicate(temp):
					continue
				# 말이 갈 곳에 다른 말이 없을 경우
				if [key, value] != [-1, -1] and [key, value] not in piece:
					all_sum = max(all_sum, temp_sum + way[key][value])
					queue.append([temp, d_idx + 1, temp_sum + way[key][value]])
				# 말이 도착 지점을 지난 경우 -> 지금까지 말들의 위치의 합에 변함이 없음
				elif [key, value] == [-1, -1]:
					queue.append([temp, d_idx + 1, temp_sum])
	return all_sum

dice = list(map(int, sys.stdin.readline().split()))
# pieces의 원소 하나 하나는 [way의 key, way의 value index]를 의미함
pieces = [[0,0],[0,0],[0,0],[0,0]]
print(play(dice, pieces))
