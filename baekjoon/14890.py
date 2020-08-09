'''
	Baekjoon - 14890. 경사로
	삼성 SW 역량 테스트 기출 문제
	언어 : Python
	메모리 : 29,380kb
	실행시간 : 68ms
	코드길이 : 965b
'''
def can_go(road, N):
	i = 1
	height = road[0]
	queue = [height]
	while i < N:
		if len(queue) > L:
			queue.pop(0)
		if height - road[i] == 1:
			if len(road[i:i+L]) != L or len(set(road[i:i+L])) != 1:
				return False
			i += L
			if i < N:
				height = road[i-1]
				del queue[:]
		elif road[i] - height == 1:
			if len(queue) != L or len(set(queue)) != 1:
				return False
			i += 1
			if i < N:
				height = road[i-1]
				del queue[:]
				queue.append(height)
		elif road[i] == height:
			i += 1
			queue.append(height)
		else:
			return False
	return True

def solution(input_map, N, L):
	answer = 2*N
	i = 0
	while i < N:
		row_road = input_map[i]
		col_road = [x[i] for x in input_map]
		answer -= 1 if not can_go(row_road, N) else 0
		answer -= 1 if not can_go(col_road, N) else 0
		i += 1
	return answer

N, L = map(int, input().split())
input_map = []
for i in range(N):
	input_map.append(list(map(int, input().split())))
print(solution(input_map, N, L))
