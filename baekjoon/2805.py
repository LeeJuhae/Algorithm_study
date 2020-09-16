'''
	Baekjoon - 2805. 나무 자르기
	삼성 SW 역량 테스트 기출 문제
	언어 : Python
	메모리 : 247,652kb
	실행시간 : 580ms
	코드길이 : 350b
'''
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
left, right = 0, max(trees)
tree_sum = 0
while left <= right:
	mid = (left + right) // 2
	tree_sum = 0
	for tree in trees:
		if tree > mid:
			tree_sum += tree - mid
	if tree_sum >= M:
		left = mid + 1
	else:
		right = mid - 1
print(right)
