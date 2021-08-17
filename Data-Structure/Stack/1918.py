# https://www.acmicpc.net/problem/1918

import sys

infix = sys.stdin.readline().rstrip()
stack = []
res = ''
for ch in infix:
	if ch.isalpha():
		res += ch
	elif ch == '(':
		stack.append(ch)
	elif ch == '*' or ch == '/':
		while stack and (stack[-1] == '*' or stack[-1] =='/'):
			res += stack.pop()
		stack.append(ch)
	elif ch == '+' or ch == '-':
		while stack and stack[-1] != '(':
			res += stack.pop()
		stack.append(ch)
	elif ch == ')':
		while stack and stack[-1] != '(':
			res += stack.pop()
		stack.pop()

while stack :
	res += stack.pop()
print(res)
