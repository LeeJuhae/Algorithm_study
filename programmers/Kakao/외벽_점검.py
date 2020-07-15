from itertools import permutations
import copy

def solution(n, weak, dist):
    answer = 0
    if len(weak) == 1:
        return 1
    perm_dists = permutations(dist)
    min_friend = 9
    for perm_dist in perm_dists:
        perm_dist = list(perm_dist)
        temp_weak = copy.deepcopy(weak)
        i = 0
        while i < len(temp_weak) - 1:
            who = []
            dist_idx = 0
            impossible = 0
            temp_perm_dist = copy.deepcopy(perm_dist)
            #print("original",perm_dist, temp_weak)
            for weak_idx in range(len(temp_weak)-1):
                #print(temp_perm_dist, temp_weak, dist_idx, weak_idx)
                if dist_idx >= len(temp_perm_dist):
                    impossible = 1
                    break
                who.append(dist_idx)
                if temp_weak[weak_idx + 1] - temp_weak[weak_idx] <= temp_perm_dist[dist_idx]:
                    temp_perm_dist[dist_idx] -= (temp_weak[weak_idx + 1] - temp_weak[weak_idx])
                else:
                    dist_idx += 1
            who.append(dist_idx)
            #print("who", who)
            if impossible == 0:
                min_friend = min(len(set(who)), min_friend)
                #print("min", min_friend, who)
            temp_weak.append(temp_weak.pop(0) + n)
            i += 1
    return min_friend
