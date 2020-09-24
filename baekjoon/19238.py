import sys
from collections import deque, defaultdict

def find_passenger(taxi, passengers, roads, fuel):
	directions = [[-1,0],[0,-1],[0,1],[1,0]]
	visited = [[0 for _ in range(N)] for _ in range(N)]
	visited[taxi[0]][taxi[1]] = 1
	queue = deque()
	queue.append([taxi, 0])
	candi_passengers = []
	min_x, min_y = N+1, N+1
	min_dist = float('inf')
	while queue:
		loc, cnt = queue.popleft()
		if cnt > min_dist:
			continue
		if loc in passengers.keys() and (loc[0] < min_x or (loc[0] == min_x and loc[1] < min_y)):
			min_dist = min(min_dist, cnt)
			candi_passengers.append((loc, cnt))
		else:
			for direc in directions:
				new_x, new_y = [i+j for i, j in zip(loc, direc)]
				if 0 <= new_x < N and 0 <= new_y < N:
					if roads[new_x][new_y] == 0 and visited[new_x][new_y] == 0:
						visited[new_x][new_y] = 1
						queue.append([(new_x, new_y), cnt +1])
	# 	if cnt > min_dist:
	# 		break
	if len(candi_passengers) == 0:
		return None
	return candi_passengers[0]

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
		# if cnt > fuel:
		# 	break
	return -1

def work(taxi, fuel, passengers, roads):
	while passengers:
		passenger = find_passenger(taxi, passengers, roads, fuel)
		if passenger == None:
			return -1
		fuel -= passenger[1]
		if fuel < 0:
			return -1
		destination = passengers[passenger[0]]
		consumed_fuel = move(passenger[0], destination, roads, fuel)
		if consumed_fuel == -1 or fuel < consumed_fuel:
			return -1
		taxi = passengers[passenger[0]]
		del passengers[passenger[0]]
		fuel += consumed_fuel
	return fuel

N, M, fuel = map(int, sys.stdin.readline().split())
roads = []
for _ in range(N):
	roads.append(list(map(int, sys.stdin.readline().split())))
taxi = list(map(int, sys.stdin.readline().split()))
taxi[0] -= 1
taxi[1] -= 1
taxi = tuple(taxi)
passengers = defaultdict()
for _ in range(M):
	s_x, s_y, e_x, e_y = list(map(int, sys.stdin.readline().split()))
	passengers[(s_x-1, s_y-1)] = (e_x-1, e_y-1)
print(work(taxi, fuel, passengers, roads))

# import sys
# from collections import deque, defaultdict
# import heapq

# def find_passenger(taxi, passengers, roads):
# 	directions = [[-1,0],[0,1],[1,0],[0,-1]]
# 	queue = deque()
# 	visited = [list(taxi)]
# 	queue.append([taxi, 0, -1, visited])
# 	candi_passengers = []
# 	min_dist = float('inf')
# 	while queue:
# 		loc, cnt, d, v = queue.popleft()
# 		if loc in passengers.keys():
# 			min_dist = min(min_dist, cnt)
# 			heapq.heappush(candi_passengers, (loc , cnt))
# 		for d_idx, direc in enumerate(directions):
# 			if d == -1 or d_idx != (d + 2) % 4:
# 				new_x, new_y = [i+j for i, j in zip(loc, direc)]
# 				if 0 <= new_x < N and 0 <= new_y < N:
# 					if roads[new_x][new_y] == 0 and [new_x, new_y] not in v:
# 						queue.append([(new_x, new_y), cnt +1, d_idx, v+[[new_x, new_y]]])
# 		if cnt > min_dist:
# 			break
# 	return candi_passengers

# def move(taxi, destination, roads):
# 	directions = [[-1,0],[0,1],[1,0],[0,-1]]
# 	queue = deque()
# 	visited = [taxi]
# 	queue.append([taxi, 0, -1, visited])
# 	while queue:
# 		loc, cnt, d, v = queue.popleft()
# 		if loc == destination:
# 			return cnt
# 		for d_idx, direc in enumerate(directions):
# 			if d == -1 or d_idx != (d + 2) % 4:
# 				new_x, new_y = [i+j for i, j in zip(loc, direc)]
# 				if 0 <= new_x < N and 0 <= new_y < N:
# 					if roads[new_x][new_y] == 0 and [new_x, new_y] not in v:
# 						queue.append([(new_x, new_y), cnt +1, d_idx, v+[[new_x, new_y]]])
# 	return -1

# def work(taxi, fuel, passengers, roads):
# 	while passengers:
# 		candi_passengers = find_passenger(taxi, passengers, roads)
# 		if len(candi_passengers) == 0:
# 			return -1
# 		passenger = candi_passengers[0]
# 		fuel -= passenger[1]
# 		if fuel < 0:
# 			return -1
# 		destination = passengers[passenger[0]]
# 		consumed_fuel = move(passenger[0], destination, roads)
# 		if consumed_fuel == -1 or fuel < consumed_fuel:
# 			return -1
# 		taxi = passengers[passenger[0]]
# 		del passengers[passenger[0]]
# 		fuel += consumed_fuel
# 	return fuel

# N, M, fuel = map(int, sys.stdin.readline().split())
# roads = []
# for _ in range(N):
# 	roads.append(list(map(int, sys.stdin.readline().split())))
# taxi = list(map(int, sys.stdin.readline().split()))
# taxi[0] -= 1
# taxi[1] -= 1
# taxi = tuple(taxi)
# passengers = defaultdict()
# for _ in range(M):
# 	s_x, s_y, e_x, e_y = list(map(int, sys.stdin.readline().split()))
# 	passengers[(s_x-1, s_y-1)] = (e_x-1, e_y-1)
# print(work(taxi, fuel, passengers, roads))
