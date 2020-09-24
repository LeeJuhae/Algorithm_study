import sys
import copy
from collections import defaultdict
from itertools import combinations

def get_h_lines(ladder):
	h_lines = []
	for b in range(1, N):
		for a in range(1, H+1):
			if a not in ladder[b].keys() and a not in ladder[b+1].keys():
				h_lines.append((a, b))
	return h_lines

def isAnswer(ladder, h_lines):
	for line in h_lines:
		a, b = line
		ladder[b][a] = b + 1
		ladder[b+1][a] = b
	i = 1
	while i < N+1:
		r, c = i, 1
		trace = []
		temp = copy.deepcopy(ladder)
		while c <= H:
			trace.append((r, c))
			if c in temp[r]:
				new_r = temp[r].pop(c)
				if (new_r, c) not in trace:
					r = new_r
				else:
					c += 1
			else:
				c += 1
			if len(temp[r].keys()) == 0:
				break
		if i != r:
			return False
		i += 1
	return True

def comb_test(ladder, h_lines, cnt):
	comb_lines = list(combinations(h_lines, cnt))
	for h_line in comb_lines:
		isPossible = True
		for line in h_line:
			a, b = line
			if (a, b+1) in h_line:
				isPossible = False
				break
		temp = copy.deepcopy(ladder)
		if isPossible and isAnswer(temp, h_line):
			return cnt
	return -1

def bfs(ladder, h_lines):
	temp = copy.deepcopy(ladder)
	if isAnswer(temp, []):
		return 0
	if comb_test(temp, h_lines, 1) != -1:
		return 1
	if comb_test(temp, h_lines, 2) != -1:
		return 2
	if comb_test(temp, h_lines, 3) != -1:
		return 3
	return -1

N, M, H = map(int, sys.stdin.readline().split())
ladder = [[0 for _ in range(N)] for _ in range(H)]
# print(ladder)
for _ in range(M):
	a, b = map(int, sys.stdin.readline().split())
	print(a, b)
	ladder[b-1][a-1] = 1
	ladder[b][a-1] = 1
	# ladder[b][a] = b + 1
	# ladder[b+1][a] = b
for row in ladder:
	print(row)
# print(bfs(ladder, get_h_lines(ladder)))

# import sys
# import copy
# from collections import defaultdict
# from itertools import combinations

# def get_h_lines(ladder):
# 	h_lines = []
# 	for b in range(1, N):
# 		for a in range(1, H+1):
# 			if a not in ladder[b].keys() and a not in ladder[b+1].keys():
# 				h_lines.append((a, b))
# 	return h_lines

# def isAnswer(ladder, h_lines):
# 	for line in h_lines:
# 		a, b = line
# 		ladder[b][a] = b + 1
# 		ladder[b+1][a] = b
# 	i = 1
# 	while i < N+1:
# 		r, c = i, 1
# 		trace = []
# 		temp = copy.deepcopy(ladder)
# 		while c <= H:
# 			trace.append((r, c))
# 			if c in temp[r]:
# 				new_r = temp[r].pop(c)
# 				if (new_r, c) not in trace:
# 					r = new_r
# 				else:
# 					c += 1
# 			else:
# 				c += 1
# 			if len(temp[r].keys()) == 0:
# 				break
# 		if i != r:
# 			return False
# 		i += 1
# 	return True

# def comb_test(ladder, h_lines, cnt):
# 	comb_lines = list(combinations(h_lines, cnt))
# 	for h_line in comb_lines:
# 		isPossible = True
# 		for line in h_line:
# 			a, b = line
# 			if (a, b+1) in h_line:
# 				isPossible = False
# 				break
# 		temp = copy.deepcopy(ladder)
# 		if isPossible and isAnswer(temp, h_line):
# 			return cnt
# 	return -1

# def bfs(ladder, h_lines):
# 	temp = copy.deepcopy(ladder)
# 	if isAnswer(temp, []):
# 		return 0
# 	if comb_test(temp, h_lines, 1) != -1:
# 		return 1
# 	if comb_test(temp, h_lines, 2) != -1:
# 		return 2
# 	if comb_test(temp, h_lines, 3) != -1:
# 		return 3
# 	return -1

# N, M, H = map(int, sys.stdin.readline().split())
# ladder = defaultdict(defaultdict)
# for _ in range(M):
# 	a, b = map(int, sys.stdin.readline().split())
# 	ladder[b][a] = b + 1
# 	ladder[b+1][a] = b
# print(bfs(ladder, get_h_lines(ladder)))
