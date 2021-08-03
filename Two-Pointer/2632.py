import sys

def get_input(size):
	temp = []
	for _ in range(size):
		temp.append(int(sys.stdin.readline().rstrip()))
	return temp

size = int(sys.stdin.readline().rstrip())
m, n = map(int, sys.stdin.readline().split())
pizzas = [get_input(m), get_input(n)]


