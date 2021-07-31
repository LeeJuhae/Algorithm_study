# https://www.acmicpc.net/problem/6198

import sys

n = int(sys.stdin.readline().strip())
buildings = [int(sys.stdin.readline().strip()) for _ in range(n)]
stack = []
cnt = 0
for i, building in enumerate(buildings):
    while stack and stack[-1][1] <= building:
        idx, h = stack.pop()
        cnt += i - idx - 1
    stack.append((i, building))

while stack:
    i, h = stack.pop()
    cnt += n - i - 1
print(cnt)
