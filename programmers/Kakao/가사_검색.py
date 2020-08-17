import sys
sys.setrecursionlimit(10**8)

class Trie():
	def __init__(self, ch, length):
		self.ch = ch
		self.children = []
		self.length = length

	def add(self, child):
		self.children.append(child)

	def get_children_ch(self):
		return [child.ch for child in self.children]

	def get_child(self, ch):
		for child in self.children:
			if child.ch == ch:
				return child
		return None

def create_trie(root, words, reverse=False):
	trie = Trie(root, 0)
	for word in words:
		if reverse:
			word = word[::-1]
		parent = trie
		for ch in word:
			child = parent.get_child(ch)
			if child is None:
				child = Trie(ch, parent.length + 1)
				parent.add(child)
			parent = child
		parent.add(Trie('',parent.length))
	return trie

def search(parent, query, query_idx, cnt):
	if parent.length > query_idx:
		return cnt
	if query_idx >= len(query):
		if parent.length == len(query) and '' in parent.get_children_ch():
			return cnt + 1
		else:
			return cnt
	else:
		children = parent.children
		if query[query_idx] == '?':
			for child in children:
				cnt = search(child, query, query_idx+1, cnt)
		elif query[query_idx] in parent.get_children_ch():
			child = parent.get_child(query[query_idx])
			cnt = search(child, query, query_idx+1, cnt)
	return cnt

def solution(words, queries):
	answer = []
	dic = {}
	trie = create_trie('',words)
	reverse_trie = create_trie('',words, True)
	for query in queries:
		if query not in dic:
			query_len = len(query)
			if query.count('?') == query_len:
				cnt = 0
				for word in words:
					if 	query_len == len(word):
						cnt += 1
				answer.append(cnt)
			elif query[0] == '?':
				answer.append(search(reverse_trie, query[::-1], 0, 0))
			else:
				answer.append(search(trie, query, 0, 0))
			dic[query] = answer[-1]
		else:
			answer.append(dic[query])
	return answer

# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
