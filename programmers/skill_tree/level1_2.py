def solution(answers):
    people = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    cnt = [0,0,0]
    answer = []
    for i in range(3):
        for j in range(len(answers)):
            if answers[j] == people[i][j%len(people[i])]:
                cnt[i] += 1
    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i+1)
    return answer
