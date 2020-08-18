class Trie():
	def __init__(self, ch):
		self.ch = ch
		self.children = dict()
		self.children_cnt = 0

	def add(self, child):
		self.children[child.ch] = child

	def get_child(self, ch):
		if ch in self.children:
			return self.children[ch]
		return None

def create_trie(words):
	trie = Trie('')
	for word in words:
		parent = trie
		for ch in word:
			child = parent.get_child(ch)
			if child is None:
				child = Trie(ch)
				parent.add(child)
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
