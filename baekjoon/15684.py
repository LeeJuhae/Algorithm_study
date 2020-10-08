import sys

def isAnswer():
	for j in range(N):
		r = j
		for i in range(H):
			if ladder[i][r] == 1:
				r += 1
			elif r-1 >= 0 and ladder[i][r-1] == 1:
				r -= 1
		if r != j:
			return False
	return True

def dfs(h, depth, min_depth):
	if depth < 4:
		if isAnswer():
			min_depth = min(min_depth, depth)
		else:
			for i in range(h, H):
				for j in range(N-1):
					if ladder[i][j] == 1 or (j-1 >= 0 and ladder[i][j-1] == 1) or (j+1 < N and ladder[i][j+1] == 1):
						continue
					ladder[i][j] = 1
					min_depth = dfs(i, depth+1, min_depth)
					ladder[i][j] = 0
	return min_depth
N, M, H = map(int, sys.stdin.readline().split())
ladder = [[0 for _ in range(N)] for _ in range(H)]
for _ in range(M):
	a, b = map(int, sys.stdin.readline().split())
	ladder[a-1][b-1] = 1
ret = dfs(0, 0, float('inf'))
print(-1 if ret == float('inf') else ret)
