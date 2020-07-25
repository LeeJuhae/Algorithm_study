from itertools import permutations

def is_banned_user(user_ids, banned_ids):
    for i, user_id in enumerate(user_ids):
        if len(user_id) != len(banned_ids[i]):
            return False
        for j in range(len(user_id)):
            if banned_ids[i][j] == '*':
                continue
            if banned_ids[i][j] != user_id[j]:
                return False
    return True
            
def solution(user_ids, banned_ids):
    user_ids = list(permutations(user_ids, len(banned_ids)))
    answer = []
    for user_id in user_ids:
        if is_banned_user(user_id, banned_ids):
            if sorted(list(user_id)) not in answer:
                answer.append(sorted(list(user_id)))
    return len(answer)
