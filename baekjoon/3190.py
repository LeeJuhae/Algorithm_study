'''
	Baekjoon - 3190. 뱀
	삼성 SW 역량 테스트 기출 문제
	언어 : PyPy3
	메모리 : 123,548kb
	실행시간 : 192ms
	코드길이 : 1049b
	list -> deque
		: 메모리 : 8kb 감소
		: 시간 : 8ms 감소
'''

import sys
from collections import deque

def play(boards, moves):
	directions = [[-1,0],[0,1],[1,0],[0,-1]]
	d_idx, time = 1, 0
	loc = [0, 0]
	move = moves.popleft()
	body = deque()
	body.append(loc)
	while True:
		boards[loc[0]][loc[1]] = 2
		if move != None and time == int(move[0]):
			d_idx = (d_idx + 3) % 4 if move[1] == 'L' else (d_idx + 1) % 4
			move = moves.popleft() if moves else None
		x, y = [i+j for i, j in zip(loc, directions[d_idx])]
		if not (0 <= x < N) or not (0 <= y < N) or boards[x][y] == 2:
			break
		elif boards[x][y] == 0:
			r_x, r_y = body.popleft()
			boards[r_x][r_y] = 0
		body.append([x,y])
		time += 1
		loc = [x, y]
	return time + 1

if __name__ == '__main__':
	N = int(sys.stdin.readline())
	K = int(sys.stdin.readline())
	boards = [[0 for _ in range(N)] for _ in range(N)]
	for _ in range(K):
		i, j = map(int, sys.stdin.readline().split())
		boards[i-1][j-1] = 1
	L = int(sys.stdin.readline())
	moves = deque()
	for _ in range(L):
		moves.append(list(sys.stdin.readline().split()))
	print(play(boards, moves))
