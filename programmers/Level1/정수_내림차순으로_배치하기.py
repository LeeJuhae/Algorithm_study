def solution(n):
    return int("".join(sorted([char for char in str(n)], reverse=True)))
