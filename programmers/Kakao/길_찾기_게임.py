import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def make_tree(nodeinfo, y):
	new_node = Node(nodeinfo[0][2])
	if len(nodeinfo) != 0:
		left_nodes, left_y = [], []
		right_nodes = []
		right_y = []
		for node in nodeinfo:
			if node[0] < nodeinfo[0][0]:
				left_nodes.append(node)
				left_y.append(node[1])
			elif node[0] > nodeinfo[0][0]:
				right_nodes.append(node)
				right_y.append(node[1])
		if len(left_nodes) != 0:
			left_nodes.sort(key=lambda x:x[1], reverse=True)
			new_node.left = make_tree(left_nodes, left_y)
		if len(right_nodes) != 0:
			right_nodes.sort(key=lambda x:x[1], reverse=True)
			new_node.right = make_tree(right_nodes, right_y)
	return new_node

def preOrder(node, preOrderList):
	preOrderList.append(node.data)
	if node.left != None:
		preOrderList = preOrder(node.left, preOrderList)
	if node.right != None:
		preOrderList = preOrder(node.right, preOrderList)
	return preOrderList

def postOrder(node, postOrderList):
	postOrderList.append(node.data)
	if node.right != None:
		postOrderList = postOrder(node.right, postOrderList)
	if node.left != None:
		postOrderList = postOrder(node.left, postOrderList)
	return postOrderList

def solution(nodeinfo):
	answer = []
	preOrderList = []
	postOrderList = []
	y = [node[1] for node in nodeinfo]
	for idx, node in enumerate(nodeinfo):
		node.append(idx + 1)
	nodeinfo.sort(key=lambda x: x[1], reverse=True)
	node = make_tree(nodeinfo, y)
	preOrderList = preOrder(node, preOrderList)
	postOrderList = postOrder(node, postOrderList)
	answer.append(preOrderList)
	postOrderList.reverse()
	answer.append(postOrderList)
	return answer
