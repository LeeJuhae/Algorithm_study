# https://www.acmicpc.net/problem/2493

'''
# test case

5
6 9 5 7 4
result: [0, 0, 2, 2, 4]

7
3 1 1 2 7 6 3
result: [0, 1, 2, 1, 0, 5, 6]
'''
import sys

n = int(sys.stdin.readline().rstrip())
tops = list(map(int, sys.stdin.readline().split()))
tops.reverse()
stack = []
ans = [0] * n

for i, top in enumerate(tops):
	while stack and stack[-1][1] <= top:
		idx, h = stack.pop()
		ans[n - idx - 1] = n - i
	stack.append((i, top))

for ele in ans:
	print(ele, end=' ')
