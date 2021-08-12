# https://www.acmicpc.net/problem/10159

import sys
from collections import defaultdict

ft_input = sys.stdin.readline
n = int(ft_input().rstrip())
m = int(ft_input().rstrip())
w = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
	heavy, light = map(int,ft_input().split())
	'''
	부등호 관계를 저장할 때, 하나의 관계(> 또는 <)만으로 w 배열을 채워야 함.
	< 와 > 관계 모두를 하나의 리스트에 저장할 경우 각각의 값을 다르게 설정해야 함.
	ex. w[heavy][light] = 1
		w[light][heavy] = 2
		위 값에 따라 아래의 코드도 일부 수정됨.
	'''
	w[heavy][light] = 1 # 부등호가 '>'인 관계를 배열에 저장함.
	# w[light][heavy] = 1

for k in range(1, n + 1): # 거쳐가는 지점
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if w[i][k] and w[k][j]: #i, j 모두 k와 대소 비교가 가능하면
				w[i][j] = 1 # i와 j의 대소 비교도 가능함

for i in range(1, n + 1):
	cnt = 0
	for j in range(1, n + 1):
		if i == j:
			continue
		if w[i][j] == 0 and w[j][i] == 0:
			cnt += 1
	print(cnt)
