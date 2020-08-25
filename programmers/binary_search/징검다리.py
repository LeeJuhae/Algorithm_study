def solution(distance, rocks, n):
	answer = 0
	rocks = sorted(rocks) + [distance]
	left, right = 1, distance
	while left <= right:
		mid = (left + right) // 2
		min_dist = distance
		prev_rock, removed_rocks = 0, 0
		for i in range(len(rocks)):
			if rocks[i] - prev_rock < mid:
				removed_rocks += 1
			else:
				min_dist = min(min_dist, rocks[i]-prev_rock)
				prev_rock = rocks[i]
		if removed_rocks > n:
			right = mid - 1
		else:
			left = mid + 1
			answer = min_dist
	return answer

print(solution(25, [2, 14, 11, 21, 17], 2))
