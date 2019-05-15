def solution(priorities, location):
    p = []
    k = 0
    for j in enumerate(priorities):
        p.append(list(j))
    while(True):
        if priorities[0] == max(priorities):
            k += 1
            if location == p[0][0]:
                return k
            priorities.pop(0)
            p.pop(0)
        else:
            priorities.append(priorities.pop(0))
            p.append(p.pop(0))
