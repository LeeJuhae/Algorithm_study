def solution(record):
    userDict = dict()
    users = []
    answer = []
    for i in record:
        if i.split(' ')[0] == 'Enter':
            answer.append('들어왔습니다.')
            userDict[i.split(' ')[1]] = i.split(' ')[2]
            users.append(i.split(' ')[1])       
        elif i.split(' ')[0] == 'Leave':
            answer.append('나갔습니다.')
            users.append(i.split(' ')[1])  
        elif i.split(' ')[0] == 'Change':
            userDict[i.split(' ')[1]] = i.split(' ')[2] 
    for i,user in enumerate(users):
        answer[i] = (userDict[user]+'님이 ') + answer[i]
    return answer
