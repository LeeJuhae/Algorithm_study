from itertools import combinations_with_replacement

def get_beauty(s):
	if s.count(s[0]) == len(s):
		return 0
	start, end = 0, len(s)-1
	while start < end:
		if s[start] == s[end]:
			end -= 1
		else:
			break
	return end - start

def solution(s):
	N = len(s)
	answer = 0
	if s.count(s[0]) == N:
		return 0
	arr = list(range(0, N))
	comb = list(combinations_with_replacement(arr, 2))
	for c in comb:
		start, end = c
		answer += get_beauty(s[start:end+1])
	return answer
print(solution("oo"))
