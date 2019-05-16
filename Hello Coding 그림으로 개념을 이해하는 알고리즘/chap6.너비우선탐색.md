## Chap6. 너비 우선 탐색 (BFS)

### 02 그래프의 소개

그래프란 연결의 집합을 모형화한 것으로, 정점(node)과 간선(edge)로 이루어진다.

### 03 너비 우선 탐색(BFS)

너비 우선 탐색은 다음 두 가지 질문에 대해 대답할 수 있다.

질문 1 : 정점 A에서 정점 B로 가는 경로가 존재하는가?

질문 2 : 정점 A에서 정점 B로 가는 최단 경로는 무엇인가?

즉, 임의의 노드에서 시작하여 인접한 노드를 먼저 탐색하는 방법을 찾는 알고리즘이다. 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법으로 깊게 탐색하기 전 넓게 탐색하는 것이다.

그래프 탐색의 경우 어떤 노드를 방문했었는지 여부를 반드시 검사해야 한다. 그렇지 않으면 무한루프에 빠질 위험이 있다. 

너비 우선 탐색 구현시 방문할 노드들을 차례로 저장한 후 꺼낼 수 있는 자료 구조인 큐를 일반적으로 사용한다. 

### 05 알고리즘의 구현

```python
from collections import deque

def bfs(name):
  search_queue = deque()
  search_queue += graph[name]
  searched = []
  while search_queue:
    person = search_queue.popleft()
    if not person in searched:
      if person_is_seller(person):
        return True
      else:
        search_queue += graph[person]
        searched.append(person)
 return False

def person_is_seller(name):
  return name[-1] == "m"

graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search("you")
```



너비 우선 탐색은 O(정점 수 + 간선 수)가 되고, 보통 O(V+E)라고 표기한다.