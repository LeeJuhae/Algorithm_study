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

def create_tries(words, reverse=False):
	trie_dict = {}
	for word in words:
		if reverse:
			word = word[::-1]
		if len(word) in trie_dict:
			parent = trie_dict[len(word)]
		else:
			parent = Trie('')
			trie_dict[len(word)] = parent
		for ch in word:
			child = parent.get_child(ch)
			if child is None:
				child = Trie(ch)
				parent.append(child)
			parent.children_cnt += 1
			parent = child
		parent.children_cnt += 1
	return trie_dict

def search(parent, query):
	for query_ch in query:
		if query_ch == '?':
			return parent.children_cnt
		else:
			child = parent.get_child(query_ch)
			if child is None:
				return 0
			else:
				parent = child
	return parent.children_cnt

def solution(words, queries):
	answer = []
	query_dic = {}
	trie_dict = create_tries(words)
	reverse_trie_dict = create_tries(words, True)
	for query in queries:
		if query not in query_dic:
			query_len = len(query)
			if '?'*query_len == query:
				cnt = len([word for word in words if len(word) == query_len])
				answer.append(cnt)
			elif query[0] == '?' and query_len in reverse_trie_dict:
				answer.append(search(reverse_trie_dict[query_len], query[::-1]))
			elif query[0] != '?' and query_len in trie_dict:
				answer.append(search(trie_dict[query_len], query))
			else:
				answer.append(0)
			query_dic[query] = answer[-1]
		else:
			answer.append(query_dic[query])
	return answer

# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
# print(solution(["frost", "fro", "kakaka"], ["?????"]))
