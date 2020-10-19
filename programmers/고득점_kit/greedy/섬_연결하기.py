def solution(n, costs):
	answer = 0
	costs.sort(key=lambda x: x[2])
	routes = set([costs[0][0]])
	while len(routes) != n:
		for i, cost in enumerate(costs):
			s, e, c = cost
			if s in routes or e in routes:
				if s in routes and e in routes:
					continue
				else:
					routes.update([s,e])
					answer += c
					costs[i] = [-1,-1,-1]
					break
	return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
