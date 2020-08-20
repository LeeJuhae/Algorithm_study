def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[len(arr)//2]
	less = []
	equal = []
	greater = []
	for ele in arr:
		if ele < pivot:
			less.append(ele)
		elif ele > pivot:
			greater.append(ele)
		else:
			equal.append(ele)
	return quick_sort(less) + equal + quick_sort(greater)

if __name__ == "__main__":
	arr = [5,3,8,4,9,1,6,2,7]
	print(quick_sort(arr))
