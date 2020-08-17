class Trie():
	def __init__(self, ch):
		self.ch = ch
		self.children = list()
		self.children_cnt = 0

	def append(self, child):
		self.children.append(child)

	def get_child(self, ch):
		for child in self.children:
			if child.ch == ch:
				return child
		return None

def create_trie(words):
	trie = Trie('')
	for word in words:
		parent = trie
		for ch in word:
			child = parent.get_child(ch)
			if child is None:
				child = Trie(ch)
				parent.append(child)
			parent.children_cnt += 1
			parent = child
		parent.children_cnt += 1
	return trie

def search(parent, word):
	cnt = 0
	while len(word) != cnt and parent.children_cnt > 1:
		parent = parent.get_child(word[cnt])
		cnt += 1
	return cnt

def solution(words):
	answer = 0
	trie = create_trie(words)
	for word in words:
		answer += search(trie, word)
	return answer

# print(solution(["go","gone","guild"]))
# print(solution(["word","war","warrior","world"]))
