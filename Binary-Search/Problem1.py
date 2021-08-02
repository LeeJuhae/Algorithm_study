# https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
	rocks = sorted(rocks + [distance])
	left, right = 0, distance
	ret = 0
	while left <= right:
		mid = (left + right) // 2
		prev = 0
		removed = 0
		for rock in rocks:
			if rock - prev < mid: removed += 1
			else: prev = rock
		if removed <= n:
			left = mid + 1
			ret = mid
		else:
			right = mid - 1
	return ret

print(solution(34, [5, 19, 28], 2)) // 15
# print(solution(1234, [1, 2, 3], 3)) // 1234
# print(solution(25, [2, 14, 11, 21, 17], 2)) // 4


'''
예전에 작성했던 코드
: min_dist를 구하는 부분 불필요 함
'''
# def solution(distance, rocks, n):
# 	answer = 0
# 	rocks = sorted(rocks) + [distance]
# 	left, right = 1, distance
# 	while left <= right:
# 		mid = (left + right) // 2
# 		min_dist = distance
# 		prev_rock, removed_rocks = 0, 0
# 		for i in range(len(rocks)):
# 			if rocks[i] - prev_rock < mid:
# 				removed_rocks += 1
# 			else:
# 				min_dist = min(min_dist, rocks[i]-prev_rock)
# 				prev_rock = rocks[i]
# 		if removed_rocks > n:
# 			right = mid - 1
# 		else:
# 			left = mid + 1
# 			answer = min_dist
# 	return answer
