def solution(people, limit):
	answer = 0
	start, end = 0, len(people)-1
	people.sort(reverse=True)
	while start <= end:
		if people[start] + people[end] <= limit:
			end -= 1
		answer +=1
		start += 1
	return answer

# print(solution(	[70, 50, 80, 50], 100))
