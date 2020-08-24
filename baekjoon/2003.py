'''
	Baekjoon - 2003. 수들의 합 2
	언어 : Python
	메모리 : 29,532kb
	실행시간 : 576ms
	코드길이 : 358b
'''

def solution(M, arr):
	start, end , cnt = 0, 0, 0
	while start <= end <= len(arr):
		now_sum = sum(arr[start:end])
		if now_sum == M:
			cnt += 1
			start += 1
		elif now_sum < M:
			end += 1
		else:
			start += 1
	return cnt

if __name__ == "__main__":
	N, M = list(map(int, input().split()))
	arr = list(map(int, input().split()))
	print(solution(M, arr))
