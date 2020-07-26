def can_go(stones, k, stone_cnt, friend):
    dist = 1
    stones = [stone-friend if stone - friend > 0 else 0 for stone in stones]
    idx = stones.index(0)
    while idx < stone_cnt and dist <= k:
        if stones[idx] == 0:
            dist += 1
        else:
            dist = 1
        idx += 1
    if dist > k:
        return False
    return True

def solution(stones, k):
    friend = min(stones)
    max_friend = max(stones)
    stone_cnt = len(stones)
    while friend <= max_friend:
        mid = (friend + max_friend) // 2
        if can_go(stones, k, stone_cnt, mid):
            friend = mid + 1
        else:
            max_friend = mid - 1
    return friend
