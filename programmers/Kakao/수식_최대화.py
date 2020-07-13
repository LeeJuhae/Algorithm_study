import math
import copy
from itertools import permutations

def split_expression(expression):
    expression_list = []
    num = ''
    operator = set()
    for ch in expression:
        if ch in ['*', '-', '+']:
            expression_list.append(int(num))
            expression_list.append(ch)
            operator.add(ch)
            num = ''
        else:
            num += ch
    expression_list.append(int(num))
    return expression_list, list(operator)

def get_perm_operators(operator):
    return list(permutations(operator, len(operator)))

def get_reward(expression_list, perm_operators):
    reward = 0
    for perm_operator in perm_operators:
        temp = copy.deepcopy(expression_list)
        for operator in perm_operator:
            while operator in temp:
                idx = temp.index(operator)
                if operator == '*':
                    temp[idx - 1] = temp[idx - 1] * temp.pop(idx + 1)
                elif operator == '-':
                    temp[idx - 1] = temp[idx - 1] - temp.pop(idx + 1)
                else:
                    temp[idx - 1] = temp[idx - 1] + temp.pop(idx + 1)
                temp.pop(idx)
        reward = max(abs(temp[0]), reward)
    return reward

def solution(expression):
    expression_list, operator = split_expression(expression)
    perm_operators = get_perm_operators(operator)
    return get_reward(expression_list, perm_operators)
