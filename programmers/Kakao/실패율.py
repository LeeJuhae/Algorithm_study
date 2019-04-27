def solution(N, stages):
    answer = []
    failure = []
    userCnt = len(stages)
    for i in range(1,N+1):
        failure.append(stages.count(i)/userCnt)        
        userCnt -= stages.count(i)
    for i in range(N):
        answer.append(failure.index(max(failure))+1)
        failure[answer[-1]-1] = -1
    return answer
