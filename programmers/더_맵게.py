import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(True):
        if scoville[0] >= K:
            return answer
        elif len(scoville) == 1:
            return -1
        heapq.heappush(scoville,heapq.heappop(scoville)+ heapq.heappop(scoville)*2)
        answer += 1
