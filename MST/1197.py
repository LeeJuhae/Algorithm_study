# https://www.acmicpc.net/problem/1197

import sys
from collections import defaultdict
from heapq import heappush, heappop

ft_input = sys.stdin.readline
v, e = map(int, ft_input().split())
adj = defaultdict(list)
for _ in range(e):
	a, b, c = map(int, ft_input().split())
	adj[a].append((c, b))
	adj[b].append((c, a))

q = [(0, 1)]
visit = [False for _ in range(v + 1)]
cnt, w_sum = 0, 0
while q:
	if cnt == v:
		break
	w, node = heappop(q)
	if not visit[node]:
		visit[node] = True
		w_sum += w
		cnt += 1
		for next_w, next_node in adj[node]:
			heappush(q, (next_w, next_node))
print(w_sum)
