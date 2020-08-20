def insertion(arr):
	for i in range(1, len(arr)):
		for j in range(i):
			if arr[i] < arr[j]:
				arr[i], arr[j] = arr[j], arr[i]
	return arr

if __name__ == "__main__":
	arr = [5,3,8,4,9,1,6,2,7]
	print(insertion(arr))
