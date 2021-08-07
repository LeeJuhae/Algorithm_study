# https://www.acmicpc.net/problem/1162

'''
# key point

시간 초과 발생 -> heapq에 넣을 때 가중치(w)가 첫번째 원소가 되도록 넣어야 함
'''

from heapq import heappush, heappop
from math import inf

n, m, k = map(int, input().split())
roads = [[] for _ in range(n + 1)]
for _ in range(m):
	a, b, c = map(int, input().split())
	roads[a].append([b, c])
	roads[b].append([a, c])
dp = [[inf for _ in range(k + 1)] for _ in range(n + 1)]
dp[1] = [0 for _ in range(k + 1)]
q = []
heappush(q, (0, 1, 0))

while q:
	print(q)
	w, v, cnt = heappop(q)
	if w > dp[v][cnt]:
		continue
	for next_v, next_w in roads[v]:
		cost = w + next_w
		if dp[next_v][cnt] > cost:
			heappush(q, (cost, next_v, cnt))
			dp[next_v][cnt] = cost
		if cnt < k:
			if dp[next_v][cnt + 1] > w:
				heappush(q, (w, next_v, cnt + 1))
				dp[next_v][cnt + 1] = w
print(min(dp[n]))
