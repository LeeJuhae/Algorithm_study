# https://i-am-wendy.tistory.com/12
def solution(N, number):
	s = [set() for x in range(8)]
	for i, x in enumerate(s):
		x.add(int(str(N)*(i+1)))
	for i in range(1, len(s)):
		for j in range(i):
			for op1 in s[j]:
				for op2 in s[i-j-1]:
					s[i].add(op1+op2)
					s[i].add(op1-op2)
					s[i].add(op1*op2)
					if op2 != 0:
						s[i].add(op1//op2)
		if number in s[i]:
			return i+1
	return -1
# print(solution(5,12))
