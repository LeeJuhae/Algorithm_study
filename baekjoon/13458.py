'''
	Baekjoon - 13458. 시험 감독
	삼성 SW 역량 테스트 기출 문제
	언어 : PyPy3
	메모리 : 233,588kb
	실행시간 : 496ms
	코드길이 : 355b
'''
import sys

N = int(sys.stdin.readline())
candidates = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
answer = 0
for i in range(N):
	candidates[i] = 0 if B > candidates[i] else candidates[i] - B
answer += N
for i in range(N):
	answer += candidates[i] // C
	if candidates[i] % C != 0:
		answer += 1
print(answer)
