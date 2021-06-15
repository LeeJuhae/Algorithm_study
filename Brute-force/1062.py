# https://www.acmicpc.net/problem/1062
import sys


def dfs(start: int, depth: int):
    global max_cnt
    if depth == K - 5:
        cnt = 0
        for word in words:
            for i, ch in enumerate(word):
                if not ch in learned:
                    break
                if i == len(word) - 1:
                    cnt += 1
        max_cnt = max(max_cnt, cnt)
        return

    for ch in range(start, ord("z") + 1):
        if not chr(ch) in learned:
            learned.add(chr(ch))
            dfs(ch + 1, depth + 1)
            learned.remove(chr(ch))


N, K = list(map(int, sys.stdin.readline().split()))
words = [sys.stdin.readline().rstrip() for _ in range(N)]
learned = {"a", "c", "i", "n", "t"}
max_cnt = 0

if K >= 5:
    dfs(ord("a"), 0)
print(max_cnt)

# 시간 초과

# N, K = list(map(int, sys.stdin.readline().split()))
# words = []
# default = {"a", "c", "i", "n", "t"}
# remain_ch = set()
# max_cnt = 0
# for i in range(N):
#     word = set(sys.stdin.readline().rstrip()) - default
#     words.append(word)
#     remain_ch.update(word)
# if K >= 5:
#     combs = combinations(remain_ch, K - 5)
#     for comb in combs:
#         cnt = 0
#         for word in words:
#             if len(set(word) - set(comb)) == 0:
#                 cnt += 1
#         max_cnt = max(max_cnt, cnt)
# print(max_cnt)
