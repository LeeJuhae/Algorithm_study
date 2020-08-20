def merge(left, right):
	result = []
	l_idx, r_idx = 0, 0
	while l_idx < len(left) and r_idx < len(right):
		if left[l_idx] <= right[r_idx]:
			result.append(left[l_idx])
			l_idx += 1
		else:
			result.append(right[r_idx])
			r_idx += 1
	if l_idx < len(left):
		result = result + left[l_idx:]
	else:
		result = result + right[r_idx:]
	return result

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return merge(left, right)

if __name__ == "__main__":
	arr = [5,3,8,4,9,1,6,2,7]
	print(merge_sort(arr))
