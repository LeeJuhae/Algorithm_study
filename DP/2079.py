# https://www.acmicpc.net/problem/2079

import sys
from collections import defaultdict
from heapq import heappush, heappop

word = sys.stdin.readline().rstrip()
n = len(word)
''' dp[i][j] = True -> word[i:j+1]가 팰린드롬 '''
dp = [[False for _ in range(n)] for _ in range(n)]
adj = defaultdict(list)

def isPalindrome(start, end):
	if start >= end:
		return True

	''' 이미 word[strart:end+1]이 팰린드롬임을 알았을 때 바로 리턴 '''
	if dp[start][end]:
		return dp[start][end]

	if word[start] == word[end]:
		ret = isPalindrome(start + 1, end - 1)
	else:
		ret = False

	dp[start][end] = ret
	return ret

'''
adj에 넣어줄 때, i + 1을 하는 이유는
아래 while문에서 next_cur의 의미에 부합하기 위함.

adj: {0: [1, 3], 1: [2, 6], 2: [3, 5], 3: [4], 4: [5], 5: [6]}
->  본 문제의 조건: 여러 개의 팰린드롬 문자열로만 word를 나눠야함.
	문자열의 처음부터 시작해서 key값까지 왔을 때,
	조건을 충족하기 위해서 갈 수 있는 문자열의 index들이 value에 담겨있음.
	즉, key와 value들이 여러 개의 팰린드롬 문자열을 구분하는 경계임.
'''
for i in range(n):
	dp[i][i] = True
	adj[i].append(i + 1)
	for j in range(i + 1, n):
		if isPalindrome(i, j):
			adj[i].append(j + 1)

q = [(0, 0)]
visit = [float('inf') for _ in range(n + 1)]

''' 문자열 끝에 도달하기 위한 최소 비용(최소의 팰린드롬 개수) 구하기. '''
while q:
	cost, cur = heappop(q)

	if visit[cur] < cost:
		continue

	for next_cur in adj[cur]:
		next_cost = cost + 1
		if next_cost < visit[next_cur]:
			visit[next_cur] = next_cost
			heappush(q, (next_cost, next_cur))
print(visit[n])
