# https://www.acmicpc.net/problem/14719

import sys

h, w = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))
stack = []
cnt = 0
pivot = blocks[0]
for block in blocks[1:]:
    if block >= pivot:
        while stack:
            height = stack.pop()
            cnt += (pivot - height)
        pivot = block
    else:
        stack.append(block)

pivot = -1
while stack:
    height = stack.pop()
    if pivot < height:
        pivot = height
    else:
        cnt += (pivot - height)
print(cnt)
