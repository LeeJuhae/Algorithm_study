def solution(m, n, puddles):
	inf = float('inf')
	road = [[inf for _ in range(m)] for _ in range(n)]
	wasPuddles = False
	for i in range(n):
		for j in range(m):
			if [j+1, i+1] in puddles:
				if j == 0:
					wasPuddles = True
				road[i][j] = 0
			elif i == 0:
				road[i][j] = 1 if road[i].count(0) == 0 else 0
			elif j == 0:
				road[i][j] = 1 if not wasPuddles else 0
	for i in range(1, n):
		for j in range(1, m):
			if road[i][j] != 0:
				if road[i][j-1] != 0 and road[i-1][j] != 0:
					road[i][j] = road[i][j-1] + road[i-1][j]
				elif road[i][j-1] == 0 or road[i-1][j] == 0:
					road[i][j] = max(road[i][j-1], road[i-1][j])
	return road[-1][-1] % 1000000007

print(solution(4,3,[[2,1],[2,2]]))
