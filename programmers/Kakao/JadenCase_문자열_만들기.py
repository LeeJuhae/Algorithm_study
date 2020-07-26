def solution(s):
    s = s.lower()
    isBlank = True
    for idx, ch in enumerate(s):
        if isBlank and ch.isalpha():
            s = s[:idx] + chr(ord(ch) - 32) + s[idx + 1:]
            isBlank = False
        if ch == ' ':
            isBlank = True
        elif ch.isdigit():
            isBlank = False
    return s
