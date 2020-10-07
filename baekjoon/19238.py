import sys
from collections import deque, defaultdict

def find_passenger(taxi, passengers, roads, fuel):
	directions = [[-1,0],[0,-1],[0,1],[1,0]]
	visited = [[0 for _ in range(N)] for _ in range(N)]
	visited[taxi[0]][taxi[1]] = 1
	queue = deque()
	queue.append([taxi, 0])
	min_x, min_y = N, N
	min_dist = float('inf')
	while queue:
		loc, cnt = queue.popleft()
		x, y = loc
		if cnt > min_dist:
			break
		if (x, y) in passengers.keys() and (x < min_x or (x == min_x and y < min_y)):
			min_dist = cnt
			min_x, min_y = x, y
		for direct in directions:
			new_x, new_y = [i+j for i, j in zip(loc, direct)]
			if 0 <= new_x < N and 0 <= new_y < N:
				if roads[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
					visited[new_x][new_y] = 1
					queue.append([(new_x, new_y), cnt+1])
	return (min_x, min_y), min_dist

def move(taxi, destination, roads, fuel):
	directions = [[-1,0],[0,1],[1,0],[0,-1]]
	queue = deque()
	visited = [[0 for _ in range(N)] for _ in range(N)]
	visited[taxi[0]][taxi[1]] = 1
	queue.append([taxi, 0])
	while queue:
		loc, cnt = queue.popleft()
		if loc == destination:
			return cnt
		for direc in directions:
			new_x, new_y = [i+j for i, j in zip(loc, direc)]
			if 0 <= new_x < N and 0 <= new_y < N:
				if roads[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
					visited[new_x][new_y] = 1
					queue.append([(new_x, new_y), cnt +1])
		if cnt > fuel:
			break
	return -1

def work(taxi, fuel, passengers, roads):
	while passengers:
		passenger, cnt = find_passenger(taxi, passengers, roads, fuel)
		if passenger == (N, N):
			return -1
		fuel -= cnt
		if fuel < 0:
			return -1
		destination = passengers[passenger]
		consumed_fuel = move(passenger, destination, roads, fuel)
		if consumed_fuel == -1 or fuel < consumed_fuel:
			return -1
		taxi = passengers[passenger]
		del passengers[passenger]
		fuel += consumed_fuel
	return fuel

N, M, fuel = map(int, sys.stdin.readline().split())
roads = []
for _ in range(N):
	roads.append(list(map(int, sys.stdin.readline().split())))
taxi = list(map(int, sys.stdin.readline().split()))
taxi = tuple([i+j for i, j in zip(taxi, [-1,-1])])
passengers = defaultdict()
for _ in range(M):
	s_x, s_y, e_x, e_y = list(map(int, sys.stdin.readline().split()))
	passengers[(s_x-1, s_y-1)] = (e_x-1, e_y-1)
print(work(taxi, fuel, passengers, roads))
