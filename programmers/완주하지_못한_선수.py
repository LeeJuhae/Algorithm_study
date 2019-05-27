import collections
def solution(participant, completion):
    p = collections.Counter(participant)
    c = collections.Counter(completion)
    return list(p-c)[0]
