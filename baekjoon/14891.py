'''
	Baekjoon - 14891. 톱니바퀴
	삼성 SW 역량 테스트 기출 문제
	언어 : Python
	메모리 : 29,380kb
	실행시간 : 64ms
	코드길이 : 1285b
'''
def get_ctrl_gear(status):
	for i in range(4):
		if status[i] == 1 or status[i] == -1:
			return i
	return -1

def set_status(gears, status, ctrl_gear):
	if ctrl_gear - 1 >= 0 and status[ctrl_gear-1] != 2:
		if gears[ctrl_gear - 1][2] != gears[ctrl_gear][6]:
			status[ctrl_gear-1] = status[ctrl_gear] * -1
		else:
			status[ctrl_gear-1] = 2
	if ctrl_gear + 1 < 4 and status[ctrl_gear+1] != 2:
		if gears[ctrl_gear + 1][6] != gears[ctrl_gear][2]:
			status[ctrl_gear+1] = status[ctrl_gear] * -1
		else:
			status[ctrl_gear+1] = 2
	return status

def rotate(gears, direction, ctrl_gear):
	if direction == -1:
		gears[ctrl_gear].append(gears[ctrl_gear].pop(0))
	else:
		gears[ctrl_gear].insert(0,gears[ctrl_gear].pop(7))
	return gears

def solution(gears, N, turns):
	answer = 0
	for i in range(N):
		gear = turns[i][0] - 1
		direction = turns[i][1]
		status = [direction if j == gear else 0 for j in range(4)]
		while status.count(1) != 0 or status.count(-1) != 0:
			ctrl_gear = get_ctrl_gear(status)
			status = set_status(gears, status, ctrl_gear)
			gears = rotate(gears, status[ctrl_gear], ctrl_gear)
			status[ctrl_gear] = 2
	for i in range(4):
		if gears[i][0] == '1':
			answer += (2 ** (i))
	return answer

gears = []
turns = []
for i in range(4):
	gears.append([x for x in input()])
N = int(input())
for i in range(N):
	turns.append(list(map(int, input().split())))
print(solution(gears, N, turns))
