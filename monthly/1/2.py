def solution(n):
	answer = [[] for _ in range(n)]
	for i in range(1,n+1):
		answer[i-1] = [0 for _ in range(i)]
	num = 1
	direc = [[1,0],[0,1],[-1,-1]]
	d_idx = 0
	loc = [-1, 0]
	for i in range(n, 0, -1):
		for j in range(i):
			loc = [x+y for x, y in zip(loc, direc[d_idx])]
			a, b = loc
			answer[a][b]= num
			num += 1
		d_idx = (d_idx + 1) % 3
	temp = []
	for row in answer:
		for col in row:
			temp.append(col)
	return temp

print(solution(5))
