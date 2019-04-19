def solution(n, words):
    answer = [0,0]
    word_history = []
    for i in range(len(words)):
        if words[i] in word_history:
            answer = [int(i%n)+1,int(i/n)+1]
            break
        else:
            word_history.append(words[i])
        if i != len(words)-1:
            if words[i][-1] != words[i+1][0]:
                answer = [int((i+1)%n)+1,int((i+1)/n)+1]
                break
    return answer

###reference_code :(
# def solution(n, words):
#     for p in range(1, len(words)):
#         if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
#     else:
#         return [0,0]