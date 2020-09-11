# Not Solved
def solution(a):
	answer = -1
	one_col = []
	for idx in range(len(a[0])):
		one_col.append(list(zip(*a))[idx].count(1))
	print(one_col)
	return answer

print(solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]]))
