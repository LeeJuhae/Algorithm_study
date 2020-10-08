def isSingleData(arr):
	data = arr[0][0]
	N = len(arr)
	for row in arr:
		if row.count(data) != N:
			return False
	return True

def divide(arr):
	ret_arr = [[],[],[],[]]
	N = len(arr)
	for idx, row in enumerate(arr):
		n = int(N / 2)
		if idx < n:
			ret_arr[0].append(row[:n])
			ret_arr[1].append(row[n:])
		else:
			ret_arr[2].append(row[:n])
			ret_arr[3].append(row[n:])
	return ret_arr

def test(arr, result):
	N = len(arr)
	if len(arr) == 1 or isSingleData(arr):
		if arr[0][0] == 0:
			result[0] += 1
		else:
			result[1] += 1
	else:
		divide_arr = divide(arr)
		for a in divide_arr:
			result = test(a, result)
	return result

def solution(arr):
	return test(arr, [0, 0])

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
