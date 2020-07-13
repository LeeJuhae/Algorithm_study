base_str = "0123456789ABCDEF"

def change_base(base, num):
    num_str = ''
    if num == 0:
        return '0'
    while num > 0:
        num_str += base_str[num % base]
        num = int (num / base)
    return num_str[::-1]

def solution(n, t, m, p):
    answer = ''
    num_str = ''
    num = 0
    while len(num_str) < m * (t - 1) + p:
        num_str += change_base(n, num)
        num += 1
    idx = 0
    for i in range(t):
        answer += num_str[idx + (p-1)]
        idx += m
    return answer
