def solution(d, budget):
    d.sort()
    sum = 0
    for i in d:
        sum += i
    for i in range(len(d)):
        if sum > budget:
            sum -= d[-1]
            d.pop(-1)
        else:
            break
    return len(d)