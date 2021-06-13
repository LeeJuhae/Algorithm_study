# https://www.acmicpc.net/problem/1759
import sys
from itertools import combinations


def getCombinations(arr: [], isVowel: bool) -> []:
    comb = []
    start = 1 if isVowel else 2
    for i in range(start, len(arr) + 1):
        comb.extend(list(combinations(arr, i)))
    return comb


L, C = list(map(int, sys.stdin.readline().split()))
input_ch = list(sys.stdin.readline().split())
vowels, constants = [], []
result = []

for ch in input_ch:
    vowels.append(ch) if ch in ["a", "e", "i", "o", "u"] else constants.append(ch)

vowels_comb = getCombinations(arr=vowels, isVowel=True)
constants_comb = getCombinations(arr=constants, isVowel=False)

for vowel in vowels_comb:
    v_num = len(vowel)
    for constant in constants_comb:
        c_num = len(constant)
        if v_num + c_num == L:
            result.append("".join(sorted(list(vowel + constant))))

result.sort()
for ele in result:
    print(ele)
