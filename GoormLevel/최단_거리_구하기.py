# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

def dfs(loc, visited, dist, min_dist):
	if loc == [N-1,N-1]:
		min_dist = min(min_dist, dist)
	else:
		for way in ways:
			x, y = [i+j for i, j in zip(loc, way)]
			if x in range(0, N) and y in range(0, N) and not visited[x][y] and roads[x][y]:
				visited[x][y] = 1
				min_dist = dfs([x,y], visited, dist + 1, min_dist)
				visited[x][y] = 0
	return min_dist
	
if __name__ == "__main__":
	N = int(sys.stdin.readline())
	roads, visited = [], []
	ways = [[-1,0],[0,1],[1,0],[0,-1]]
	for _ in range(N):
		roads.append(list(map(int,sys.stdin.readline().split())))
		visited.append([0]*N)
	visited[0][0] = 1
	print(dfs([0,0], visited, 0, 100)+1)
	
# 6
# 1 1 1 1 1 1
# 0 0 1 0 0 1
# 1 1 1 0 1 1
# 1 0 0 0 1 0
# 1 1 1 0 1 0
# 0 0 1 1 1 1
