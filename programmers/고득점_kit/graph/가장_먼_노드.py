from collections import defaultdict, deque
inf = float('inf')

def make_graph(edges):
	graph = defaultdict(list)
	for edge in edges:
		a, b = edge
		graph[a].append(b)
		graph[b].append(a)
	return graph

def count_nodes(graph, weight):
	queue = deque()
	queue.append([1, 0])
	while queue:
		now, cost = queue.popleft()
		for node in graph[now]:
			if weight[node-1] == inf:
				weight[node-1] = cost + 1
				queue.append([node, cost+1])
	return weight.count(max(weight))

def solution(n, edge):
	answer, start = 0, 1
	graph = make_graph(edge)
	weight = [0] + [inf for _ in range(1, n)]
	return count_nodes(graph, weight)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
