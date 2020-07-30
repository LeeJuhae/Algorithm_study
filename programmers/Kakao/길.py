class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def make_tree(nodeinfo, y, node_dict):
	parent_idx = -1
	for idx, node in enumerate(nodeinfo):
		if node[1] == max(y):
			parent_idx = idx
			break
	print(parent_idx)

	new_node = Node(node_dict.values().index(nodeinfo[parent_idx]))
	print(new_node.data)
	if len(nodeinfo) == 0:
		return new_node
	left_nodes, left_y = [], []
	right_nodes = []
	right_y = []
	print(nodeinfo, parent_idx)
	for node in nodeinfo:
		if node[0] < nodeinfo[parent_idx][0]:
			left_nodes.append(node)
			left_y.append(node[1])
		elif node[0] > nodeinfo[parent_idx][0]:
			right_nodes.append(node)
			right_y.append(node[1])

	if len(left_nodes) != 0:
		new_node.left = make_tree(left_nodes, left_y, node_dict)
		# make_tree(left_nodes, left_y)
	if len(right_nodes) != 0:
		new_node.right = make_tree(right_nodes, right_y, node_dict)
		# make_tree(right_nodes, right_y)
	return new_node

def solution(nodeinfo):
	answer = [[]]
	y = [node[1] for node in nodeinfo]
	node_dict = dict()
	for idx, node in enumerate(nodeinfo):
		node_dict[idx + 1] =  node
		print(node)
	node = make_tree(nodeinfo, y, node_dict)
	#print(node.right.data)
	return answer

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
