import sys
from collections import defaultdict
import heapq

def infect(info, value, start):
	nodes = []
	heapq.heappush(nodes, [value[start], start])
	while nodes:
		distance, start = heapq.heappop(nodes)
		for k, v in info[start].items():
			if value[k] > distance + v:
				value[k] = distance + v
				heapq.heappush(nodes, [value[k],k])
	return value

def set_value(value, node):
	if value.get(node) is None:
		value[node] = max_value
	return value

N = int(sys.stdin.readline())
max_value = float('inf')
for _ in range(N):
	nodes, lines, start = map(int, sys.stdin.readline().split())
	info, value = defaultdict(dict), dict()
	for _ in range(lines):
		a, b, s = map(int, sys.stdin.readline().split())
		value = set_value(value, a)
		value = set_value(value, b)
		info[b][a] = s
	value[start] = 0
	value = infect(info, value, start)
	days = list(filter(lambda x: x != max_value,list(value.values())))
	print(len(days), max(days))

# import sys
# from collections import defaultdict
# from heapq import heappush, heappop

# def infect(info, value, start):
# 	nodes = []
# 	heappush(nodes, info[start])
# 	infected = 1
# 	while nodes:
# 		for _ in range(len(nodes)):
# 			node = heappop(nodes)
# 			for idx, (k, v) in enumerate(node.items()):
# 				if value[k] == max_value:
# 					infected += 1
# 				value[k] = min(value[k], value[start] + v)
# 				if k in info.keys():
# 					nodes.append(info[k])
# 				if idx == 0:
# 					start = k
# 	return infected, value

# def set_value(value, node):
# 	if value.get(node) is None:
# 		value[node] = max_value
# 	return value

# N = int(sys.stdin.readline())
# max_value = float('inf')
# for _ in range(N):
# 	nodes, lines, start = map(int, sys.stdin.readline().split())
# 	info, value = defaultdict(dict), dict()
# 	for _ in range(lines):
# 		a, b, s = map(int, sys.stdin.readline().split())
# 		value = set_value(value, a)
# 		value = set_value(value, b)
# 		info[b][a] = s
# 	value[start] = 0
# 	infected, value = infect(info, value, start)
# 	days = filter(lambda x: x != max_value,list(value.values()))
# 	print(infected, max(days))
