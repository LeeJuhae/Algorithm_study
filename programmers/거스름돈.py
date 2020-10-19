# table[y][x] = 0부터 y까지의 화폐로 i원을 내는 법
def solution(n, money):
	table = [[0 for _ in range(n+1)] for _ in range(len(money))]
	# for t in table:
	# 	print(t)
	table[0][0] = 1
	# 동전의 최솟값으로 만들 수 있는 값들. 최소 동전이 1이 아닌 경우도 있을 수 있으므로.
	# print(money[0])
	for i in range(money[0], n+1, money[0]):
		# print(i)
		table[0][i] = 1
	# for t in table:
	# 	print(t)
	for y in range(1, len(money)):
		for x in range(n+1):
			if x >= money[y]:
				table[y][x] = (table[y-1][x] + table[y][x - money[y]]) % 1000000007
			else:
				table[y][x] = table[y-1][x]
	for t in table:
		print(t)
	return table[-1][-1]

print(solution(5, [1,2,5]))
# print(solution(7,[2,3,4]))


# import sys
# sys.setrecursionlimit(10**9)

# def dfs(num, cards, cnt):
# 	if num == 0:
# 		cnt += 1
# 	elif len(cards) != 0:
# 		div = num // cards[0]
# 		mod = num % cards[0]
# 		for x in range(0, div+1):
# 			cnt = dfs(num-x*cards[0], cards[1:],cnt)
# 	return cnt

# def solution(num, cards):
# 	cards.sort(reverse=True)
# 	min_cnt = dfs(num, cards, 0)
# 	return min_cnt
