# https://www.acmicpc.net/problem/9655

def game(who, stone):
    if stone == 0:
        if who == 0:
            return 'CY'
        else:
            return 'SK'

    if dp[who][stone] != '':
        return dp[who][stone]

    ret = ''
    if stone - 1 >= 0:
        ret = game(1-who, stone-1)
    if stone - 3 >= 0:
        ret = game(1-who, stone-3)
        dp[who][stone] = ret
    return ret


n = int(input())
dp = [['' for _ in range(n+1)]for _ in range(2)]
print(game(0, n))
