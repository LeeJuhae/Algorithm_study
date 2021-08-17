import sys

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
stack = []
for _ in range(n):
	cmd = ft_input().split()
	if cmd[0] ==  'push':
		stack.append(cmd[1])
	elif cmd[0] == 'pop':
		if len(stack) == 0: print(-1)
		else: print(stack.pop())
	elif cmd[0] == 'size':
		print(len(stack))
	elif cmd[0] == 'empty':
		if len(stack) == 0: print(1)
		else: print(0)
	elif cmd[0] == 'top':
		if len(stack) == 0: print(-1)
		else: print(stack[-1])
