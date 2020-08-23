import heapq

def solution(jobs):
	last, now = -1, 0
	answer, count = 0, 0
	wait = []
	while (count < len(jobs)):
		for job in jobs:
			if last < job[0] <= now:
				answer += (now - job[0])
				heapq.heappush(wait, job[1])
		if len(wait) > 0:
			answer += len(wait) * wait[0]
			last = now
			now += heapq.heappop(wait)
			count += 1
		else:
			now += 1
	return answer // len(jobs)
