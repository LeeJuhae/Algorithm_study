def selection(arr):
	for idx in range(len(arr)):
		min_idx = arr.index(min(arr[idx:]))
		arr[idx], arr[min_idx] = arr[min_idx] , arr[idx]
	return arr

if __name__ == "__main__":
	arr = [5,3,8,4,9,1,6,2,7]
	print(selection(arr))
