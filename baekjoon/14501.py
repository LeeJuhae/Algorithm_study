def can_work_days(N, schedule):
	work_days = dict()
	for i in range(N):
		if i + schedule[i][0] <= N:
			work_days[i] = []
			for j in range(i+schedule[i][0], N):
				if j + schedule[j][0] <= N:
					work_days[i].append(j)
	return work_days

def do_work(schedule, work_days, now, money, max_money):
	if len(work_days[now]) == 0:
		return money
	for next_day in work_days[now]:
		max_money = max(do_work(schedule, work_days, next_day, money + schedule[next_day][1], max_money), max_money)
	return max_money

def solution(N, schedule):
	work_days = can_work_days(N, schedule)
	money = 0
	for now in work_days.keys():
		money = max(do_work(schedule, work_days, now, schedule[now][1], 0), money)
	return money

N = int(input())
schedule = []
for i in range(N):
	schedule.append(list(map(int, input().split())))
print(solution(N, schedule))
