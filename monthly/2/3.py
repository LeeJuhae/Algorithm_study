from collections import defaultdict, deque
from itertools import combinations

def get_info(tree_info, i, n):
	queue = []
	for idx in tree_info[i].items():
		queue.append([idx, 1])
	queue = deque(queue)
	while queue:
		ele, cnt = queue.popleft()
		if cnt > n:
			break
		for temp in tree_info[ele[0]].items():
			if temp[0] != i:
				if temp[0] in tree_info[i]:
					tree_info[i][temp[0]] = min(tree_info[i][temp[0]],temp[1] + cnt)
					tree_info[temp[0]][i] = min(tree_info[i][temp[0]],temp[1] + cnt)
				else:
					tree_info[i][temp[0]] = temp[1] + cnt
					tree_info[temp[0]][i] = temp[1] + cnt
					if cnt == n:
						return tree_info
					queue.append([temp, cnt + 1])
	return tree_info

def solution(n, edges):
	tree_info = defaultdict(defaultdict)
	for edge in edges:
		a, b = edge
		tree_info[a][b] = 1
		tree_info[b][a] = 1
	for i in range(1,n+1 // 2):
		tree_info = get_info(tree_info, i, n)
	comb = list(combinations(list(range(1, n+1)), 3))
	max_median = 0
	for ele in comb:
		a, b, c = ele
		temp = sorted([tree_info[a][b], tree_info[a][c], tree_info[b][c]])
		max_median = max(max_median, temp[1])
	return max_median

print(solution(4, [[1,2],[2,3],[3,4]]))
