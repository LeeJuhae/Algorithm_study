# https://www.acmicpc.net/problem/2504

'''
# 놓쳤던 부분

괄호가 올바르지 않은 경우를 생각하지 못했다.
(코드 상에서 for문의 첫번째 elif 부분)
'''
import sys

inputs = sys.stdin.readline().rstrip()
b_val = {')' : 2, ']': 3}
stack = []
res = 0

for ele in inputs:
	if ele in ['(', '[']:
		stack.append([ele, 0])
	elif not stack or (stack[-1][0] == '(' and ele == ']') \
		or (stack[-1][0] == '[' and ele == ')'):
		print(0)
		sys.exit()
	elif stack :
		if (stack[-1][0] == '(' and ele == ')') or \
			(stack[-1][0] == '[' and ele == ']'):
			e, s = stack.pop()
			if stack:
				stack[-1][1] += b_val[ele] * (s if s != 0 else 1)
			else:
				res += b_val[ele] * (s if s != 0 else 1)
print(res)
