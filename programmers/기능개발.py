import math
def solution(progresses, speeds):
    answer = []
    k = 0
    standard = 0
    for i in range(len(progresses)):
        speeds[i] = math.ceil((100-progresses[i])/speeds[i])
    for i in range(len(speeds)):
        if standard != 0:
            if speeds[i] <= standard:
                answer[-1] += 1
            else:
                standard = 0
        if standard == 0:
            standard = speeds[i]
            answer.append(1)
    print(answer)
    return answer
