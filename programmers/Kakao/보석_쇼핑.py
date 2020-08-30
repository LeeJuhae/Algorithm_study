def solution(gems):
    gems_cnt = len(set(gems))
    start, end = 0, 0
    buy_gems = {gems[0] : 1}
    answer = [start, len(gems)]
    while start < len(gems) and end < len(gems):
        if len(buy_gems) == gems_cnt:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            if buy_gems[gems[start]] == 1:
                del buy_gems[gems[start]]
            else:
                buy_gems[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if len(gems) == end:
                break
            if gems[end] in buy_gems:
                buy_gems[gems[end]] += 1
            else:
                buy_gems[gems[end]] = 1
    return [answer[0]+1, answer[1]+1]
