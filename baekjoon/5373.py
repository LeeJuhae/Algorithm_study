'''
	Baekjoon - 5373. 큐빙
	삼성 SW 역량 테스트 기출 문제
	언어 : Python
	메모리 : 29,380kb
	실행시간 : 392ms
	코드길이 : 2899b
'''
def get_sides():
	sides = {}
	for side, color in side_info.items():
		sides[side] = []
		for r in range(3):
			temp = []
			for c in range(3):
				temp.append(color)
			sides[side].append(temp)
	return sides

def get_rot_ways():
	ways = dict()
	ways['U+'] =[['F',0,'r',0],['L',0,'r',0],['B',0,'r',0],['R',0,'r',0]]
	ways['U-'] =[['F',0,'r',0],['R',0,'r',0],['B',0,'r',0],['L',0,'r',0]]
	ways['D+'] =[['F',2,'r',0],['R',2,'r',0],['B',2,'r',0],['L',2,'r',0]]
	ways['D-'] =[['F',2,'r',0],['L',2,'r',0],['B',2,'r',0],['R',2,'r',0]]
	ways['L+'] =[['U',0,'c',-1],['F',0,'c',0],['D',0,'c',0],['B',2,'c',-1]]
	ways['L-'] =[['U',0,'c',0],['B',2,'c',-1],['D',0,'c',-1],['F',0,'c',0]]
	ways['R+'] =[['U',2,'c',0],['B',0,'c',-1],['D',2,'c',-1],['F',2,'c',0]]
	ways['R-'] =[['U',2,'c',-1],['F',2,'c',0],['D',2,'c',0],['B',0,'c',-1]]
	ways['F+'] =[['U',2,'r',-1],['R',0,'c',0],['D',0,'r',-1],['L',2,'c',0]]
	ways['F-'] =[['U',2,'r',0],['L',2,'c',-1],['D',0,'r',0],['R',0,'c',-1]]
	ways['B+'] =[['U',0,'r',0],['L',0,'c',-1],['D',2,'r',0],['R',2,'c',-1]]
	ways['B-'] =[['U',0,'r',-1],['R',2,'c',0],['D',2,'r',-1],['L',0,'c',0]]
	return ways

def rotate_target(side, direction):
	new_side = []
	if direction == '+':
		for c in range(3):
			row = []
			for r in range(2,-1,-1):
				row.append(side[r][c])
			new_side.append(row)
	elif direction == '-':
		for c in range(2,-1,-1):
			row = []
			for r in range(3):
				row.append(side[r][c])
			new_side.append(row)
	return new_side

def rotate_touch_side(sides, target, rotating_way):
	pre_cube = []
	for side_idx in range(4):
		now = rotating_way[side_idx]
		now_target, now_idx, now_type, direction = now
		if len(pre_cube) == 0:
			pre = rotating_way[(side_idx+3)%4]
			pre_target, pre_idx, pre_type = pre[:-1]
			if pre_type == 'r':
				pre_cube = sides[pre_target][pre_idx]
			elif pre_type == 'c':
				pre_cube = [row[pre_idx] for row in sides[pre_target]]
		if direction == -1:
			pre_cube.reverse()
		if now_type == 'r':
			now_cube = sides[now_target][now_idx]
			sides[now_target][now_idx] = pre_cube
		elif now_type == 'c':
			now_cube = [row[now_idx] for row in sides[now_target]]
			for idx in range(3):
				sides[now_target][idx][now_idx] = pre_cube[idx]
		pre_cube = now_cube
	return sides

def rotate(sides, testcases, rotating_ways):
	for testcase in testcases:
		target = testcase[0]
		direction = testcase[1]
		sides[target] = rotate_target(sides[target], direction)
		sides = rotate_touch_side(sides, target, rotating_ways[target+direction])
	return sides

def print_up_side(up_side):
	for row in up_side:
		print(''.join(row))

if __name__ == '__main__':
	N = int(input())
	side_info = {'U':'w','D':'y','F':'r','B':'o','L':'g','R':'b'}
	rotating_ways = get_rot_ways()
	for _ in range(N):
		sides = get_sides()
		M = int(input())
		testcases = list(input().split(' '))
		sides = rotate(sides, testcases, rotating_ways)
		print_up_side(sides['U'])
