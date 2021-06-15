# https://www.acmicpc.net/problem/1107
import sys

N = int(sys.stdin.readline().rstrip())
sys.stdin.readline().rstrip()
broken = set(sys.stdin.readline().split())
min_val = abs(N - 100)

for channel in range(1000000):
    str_channel = str(channel)
    if len(set(str_channel) & broken) == 0:
        min_val = min(min_val, len(str_channel) + abs(N - channel))
print(min_val)
