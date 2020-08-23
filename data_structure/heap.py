class Node():
	def __init__(self, data):
		self.data = data

class Heap():
	def __init__(self):
		self.queue = [None]

	def swap(self, i, j):
		self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

	def insert(self, data):
		self.queue.append(Node(data))
		idx = len(self.queue) - 1
		while idx > 1:
			parent_idx = idx // 2
			if self.queue[parent_idx].data > self.queue[idx].data:
				self.swap(parent_idx, idx)
				idx = parent_idx
			else:
				break

	def delete(self):
		queue_len = len(self.queue)
		self.queue[1], self.queue[queue_len-1] = self.queue[queue_len-1], self.queue[1]
		ret = self.queue.pop()
		queue_len -= 1
		idx = 1
		while idx < queue_len:
			l_child = idx * 2
			r_child = idx * 2 + 1
			if l_child < queue_len and self.queue[idx].data > self.queue[l_child].data:
				self.swap(idx, l_child)
				idx = l_child
			elif r_child < queue_len and self.queue[idx].data > self.queue[r_child].data:
				self.swap(idx, r_child)
				idx = r_child
			else:
				break
		return ret.data

def get_heap(arr):
	heap = Heap()
	for ele in arr:
		heap.insert(ele)
	return heap

arr = [1,3,11,6,5,2]
heap = get_heap(arr)
print([ele.data for ele in heap.queue[1:]])
