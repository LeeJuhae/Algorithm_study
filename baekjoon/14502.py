'''
백준 - 14502 : 연구소
삼성 SW 역량 테스트 기출 문제
'''

from itertools import combinations
import copy

def set_walls(lab_map, walls):
	for wall in walls:
		lab_map[wall[0]][wall[1]] = 1
	return lab_map

def spread(lab_map):
	while True:
		conta = 0
		for r in range(len(lab_map)):
			for c in range(len(lab_map[r])):
				if lab_map[r][c] == 2:
					if r != 0 and lab_map[r-1][c] == 0:
						lab_map[r-1][c] = 2
						conta += 1
					if r != len(lab_map) - 1 and lab_map[r+1][c] == 0:
						lab_map[r+1][c] = 2
						conta += 1
					if c != 0 and lab_map[r][c-1] == 0:
						lab_map[r][c-1] = 2
						conta += 1
					if c != len(lab_map[r]) - 1 and lab_map[r][c+1] == 0:
						lab_map[r][c+1] = 2
						conta += 1
		if conta == 0:
			break
	return lab_map

def get_safe_zone(conta_map):
	safe_zone = 0
	for row in conta_map:
		safe_zone += row.count(0)
	return safe_zone

def solution(n, m, lab_map):
	wall_locs = []
	max_safe_zone = 0
	for r,row in enumerate(lab_map):
		for c,ele in enumerate(row):
			if ele == 0:
				wall_locs.append([r,c])
	walls_comb = list(combinations(wall_locs, 3))

	for walls in walls_comb:
		temp_map = copy.deepcopy(lab_map)
		walls_in_map = set_walls(temp_map, walls)
		conta_map = spread(walls_in_map)
		safe_zone = get_safe_zone(conta_map)
		max_safe_zone = max(max_safe_zone, safe_zone)
	return(max_safe_zone)

n, m = map(int, input().split(' '))
lab_map = []
for i in range(n):
	lab_map.append(list(map(int, input().split(' '))))

print(solution(n, m, lab_map))

'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

result : 27
-----------

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

result : 9
-----------

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

result : 3
-----------
'''
