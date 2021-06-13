# https://www.acmicpc.net/problem/1759
import sys


def combinations(arr: list, idx: int, ele: list, comb: list) -> list:
    if idx == len(arr):
        comb.append(ele)
        return comb
    combinations(arr, idx + 1, ele, comb)
    combinations(arr, idx + 1, ele + [arr[idx]], comb)
    return comb


def getCombinations(arr: list) -> list:
    return combinations(arr, 0, [], [])


L, C = list(map(int, sys.stdin.readline().split()))
input_ch = list(sys.stdin.readline().split())
vowels, constants = [], []
result = []

for ch in input_ch:
    vowels.append(ch) if ch in ["a", "e", "i", "o", "u"] else constants.append(ch)

vowels_comb = getCombinations(arr=vowels)
constants_comb = getCombinations(arr=constants)

for vowel in vowels_comb:
    v_num = len(vowel)
    if v_num < 1:
        continue
    for constant in constants_comb:
        c_num = len(constant)
        if c_num >= 2 and v_num + c_num == L:
            result.append("".join(sorted(vowel + constant)))

result.sort()
for ele in result:
    print(ele)
