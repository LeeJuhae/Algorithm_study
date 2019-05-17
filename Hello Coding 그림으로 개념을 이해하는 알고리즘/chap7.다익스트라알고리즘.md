## Chap7. 다익스트라 알고리즘

### 02 다익스트라 알고리즘

다익스트라 알고리즘은 하나의 정점에서 다른 모든 정점들의 최단 경로를 구하는 알고리즘이다. 또한 방향성 비순환 그래프(Directed Acyclic Graph)에만 적용된다.

다음 4단계로 이루어진다.

1. 가중치가 가장 작은 정점을 찾는다.
2. 이 정점의 이웃 정점에 대해 현재의 가중치보다 더 작은 경로가 존재하는지 확인하고, 있다면 가중치를 수정한다.
3. 그래프 상의 모든 정점에 대해 반복한다.
4. 최종 경로를 계산한다.

``` python
def find_lowest_cost_node(costs):
  lowest_cost = float("inf")
  lowest_cost_node = None
  for node in costs:
    if cost < lowest_code and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  return lowest_cost_node

#그래프
graph = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

#각 정점까지의 가중치 합을 기록하기 위한 dict
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#부모 정점을 기록하기 위한 dict
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None 

processed = []
node = find_lowest_cost_node(costs)
while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  for n in neighbors.keys():
    new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
      costs[n] = new_cost
      parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
```

다익스트라 알고리즘은 가중치가 모두 양수일 때만 정상적으로 동작한다. 만약 가중치가 음수이면 벨만-포드 알고리즘을 사용한다.