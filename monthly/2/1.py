def solution(n):
	three_digits = '0123'
	answer = ''
	decimal = 0
	while n > 0:
		answer += three_digits[n % 3]
		n = n // 3
	answer = answer[::-1]
	for i, ch in enumerate(answer):
		decimal += int(ch) * pow(3, i)
	return decimal

print(solution(45))
