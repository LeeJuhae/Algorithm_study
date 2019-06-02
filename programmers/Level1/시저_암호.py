def solution(str, n):
    answer = ""
    temp = 0
    for i in range(len(str)):
        if (65 <= ord(str[i])) and (ord(str[i])<=90):
            if (ord(str[i]) + n) % 91 < 65:
                temp = 65
            answer += chr(((ord(str[i])+ n) % 91) + temp)
        elif (97 <= ord(str[i])) and (ord(str[i])<=122):
            if (ord(str[i]) + n) % 123 < 97:
                temp = 97
            answer += chr(((ord(str[i])+ n) % 123) + temp)
        else:
            answer += " "
    return answer
