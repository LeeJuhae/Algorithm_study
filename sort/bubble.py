def bubble(arr):
	for i in range(len(arr)-1):
		for j in range(1, len(arr)-i):
			if arr[j-1] > arr[j]:
				arr[j-1], arr[j] = arr[j], arr[j-1]
	return arr

if __name__ == "__main__":
	arr = [5,3,8,4,9,1,6,2,7]
	print(bubble(arr))
