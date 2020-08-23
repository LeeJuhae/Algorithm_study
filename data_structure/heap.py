class Node():
	def __init__(self, data):
		self.data = data

class Heap():
	def __init__(self, isMaxHeap=True):
		self.queue = [None]
		self.isMaxHeap = isMaxHeap

	def swap(self, i, j):
		self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

	def insert(self, data):
		self.queue.append(Node(data))
		idx = len(self.queue) - 1
		while idx > 1:
			parent_idx = idx // 2
			if (self.isMaxHeap and self.queue[parent_idx].data < self.queue[idx].data) \
				or (not self.isMaxHeap and self.queue[parent_idx].data > self.queue[idx].data):
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
			if self.isMaxHeap:
				if l_child < queue_len and self.queue[idx].data < self.queue[l_child].data:
					self.swap(idx, l_child)
					idx = l_child
				elif r_child < queue_len and self.queue[idx].data < self.queue[r_child].data:
					self.swap(idx, r_child)
					idx = r_child
				else:
					break
			if not self.isMaxHeap:
				if l_child < queue_len and self.queue[idx].data > self.queue[l_child].data:
					self.swap(idx, l_child)
					idx = l_child
				elif r_child < queue_len and self.queue[idx].data > self.queue[r_child].data:
					self.swap(idx, r_child)
					idx = r_child
				else:
					break
		return ret.data

if __name__ == "__main__":
	arr = [1,3,11,6,5,2]
	maxHeap = Heap()
	minHeap = Heap(False)
	for ele in arr:
		maxHeap.insert(ele)
		minHeap.insert(ele)
	print([ele.data for ele in maxHeap.queue[1:]])
	print([ele.data for ele in minHeap.queue[1:]])
