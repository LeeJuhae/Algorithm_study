# https://programmers.co.kr/learn/courses/30/lessons/64062

def cross(stones, mid, k):
	cnt = 1
	for idx, stone in enumerate(stones):
		if stone - mid < 0:
			cnt += 1
		else:
			if cnt > k:
				return False
			cnt = 1
	if cnt > k:
		return False
	return True

def solution(stones, k):
	left, right = min(stones), max(stones)
	ret = 0
	while left <= right:
		mid = (left + right) // 2
		if cross(stones, mid, k):
			left = mid + 1
			ret = mid
		else:
			right = mid - 1
	return ret

# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # 3
# print(solution(	[1, 3, 3, 1, 3, 2], 2)) # 3

# 이전 코드

# def can_go(stones, k, stone_cnt, friend):
#     dist = 1
#     stones = [stone-friend if stone - friend > 0 else 0 for stone in stones]
#     idx = stones.index(0)
#     while idx < stone_cnt and dist <= k:
#         if stones[idx] == 0:
#             dist += 1
#         else:
#             dist = 1
#         idx += 1
#     if dist > k:
#         return False
#     return True

# def solution(stones, k):
#     friend = min(stones)
#     max_friend = max(stones)
#     stone_cnt = len(stones)
#     while friend <= max_friend:
#         mid = (friend + max_friend) // 2
#         if can_go(stones, k, stone_cnt, mid):
#             friend = mid + 1
#         else:
#             max_friend = mid - 1
#     return friend
