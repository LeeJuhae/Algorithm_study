'''
	Baekjoon - 1717. 집합의 표현 (Union-Find)
	언어 : Python
	메모리 : 111,816kb
	실행시간 : 544ms
	코드길이 : 641b
'''
import sys
input = sys.stdin.readline

def get_parent(me):
	if parents[me] == me:
		return me
	parent = get_parent(parents[me])
	parents[me] = parent
	return parent

def union(a, b):
	a_parent = get_parent(a)
	b_parent = get_parent(b)
	if a_parent != b_parent:
		parents[b_parent] = a_parent

def find_parent(me):
	if parents[me] == me:
		return me
	return find_parent(parents[me])

if __name__ == "__main__":
	N, M = map(int, input().split())
	parents = dict()
	for i in range(N+1):
		parents[i] = i
	for _ in range(M):
		cmd, a, b = map(int, input().split())
		if cmd == 0:
			union(a, b)
		else:
			if find_parent(a) == find_parent(b):
				print('YES')
			else:
				print('NO')
