# https://www.acmicpc.net/problem/1509

import sys
from collections import defaultdict
from heapq import heappush, heappop

word = sys.stdin.readline().rstrip()
n = len(word)
dp = [[None for _ in range(n)] for _ in range(n)]
adj = defaultdict(list)

def isPalindrome(start, end):
	if start >= end:
		return True

	if dp[start][end] != None:
		return dp[start][end]

	if word[start] == word[end]:
		ret = isPalindrome(start + 1, end - 1)
	else:
		ret = False

	dp[start][end] = ret
	return ret

for i in range(n):
	dp[i][i] = True
	adj[i].append(i + 1)
	for j in range(i + 1, n):
		if isPalindrome(i, j):
			adj[i].append(j + 1)

q = [(0, 0)]
visit = [float('inf') for _ in range(n + 1)]
visit[0] = 0

while q:
	cost, cur = heappop(q)

	if visit[cur] < cost:
		continue

	for next_cur in adj[cur]:
		next_cost = cost + 1
		''' 부등호에 등호 안붙여서 시간초과 발생함 (!다음부터 조심하기!)'''
		if visit[next_cur] <= next_cost:
			continue
		visit[next_cur] = next_cost
		heappush(q, (next_cost, next_cur))

print(visit[n])
