# https://www.acmicpc.net/problem/7579
# https://claude-u.tistory.com/445

import sys

ft_input = sys.stdin.readline
n, m = map(int, ft_input().split())
memories = [0] + list(map(int, ft_input().split()))
costs = [0] + list(map(int, ft_input().split()))
dp = [[0 for _ in range(sum(costs)+ 1)] for _ in range(n + 1)]
ans = float('inf')
for i in range(1, n + 1):
	memory, cost = memories[i], costs[i]
	for j in range(sum(costs) + 1):
		if j < cost:
			dp[i][j] = dp[i - 1][j]
		else:
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + memory)
		if dp[i][j] >= m:
			ans = min(ans, j)
print(ans if ans != float('inf') else 0)
