def solution(skill, skill_trees):
    cnt = 0
    for i in range(len(skill_trees)):
        num = -1
        change_cnt = 0
        include = True
        for j in range(len(skill)):
            if skill[j] in skill_trees[i]:
                if include:
                    if num <skill_trees[i].index(skill[j]) and change_cnt == j:
                        num = skill_trees[i].index(skill[j])
                        change_cnt += 1
                    else:
                        cnt += 1
                        break
                else:
                    cnt += 1
                    break
            else:
                incude = False
    answer = len(skill_trees) - cnt
    return answer