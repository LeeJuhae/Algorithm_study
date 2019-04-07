def solution(answers):
    answer = []
    num = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    cntarr = [0,0,0]

    for j in range(len(answers)):
        for i in range(0, 3):
            if answers[j] == num[i][j % len(num[i])]:
                cntarr[i] += 1    
                
    for i in range(0, 3):
        if cntarr[i] == max(cntarr):
            answer.append(i+1)

    return answer
