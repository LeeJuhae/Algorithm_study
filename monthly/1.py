def solution(numbers):
	answer = set()
	for i in range(len(numbers)):
		for j in range(i+1, len(numbers)):
			answer.add(numbers[i]+numbers[j])
	return sorted(list(answer))
print(solution([2,1,3,4,1]))
# print(solution([2]))