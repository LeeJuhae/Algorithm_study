def solution(n, arr):
    tree = {}
    key = -1
    for a in arr:
        if len(tree.keys()) < 2:
            tree[a] = []
            if len(tree.keys()) == 2:
                tree[key].append(a)
        else:
            if a in tree.keys():
                if not key in tree[a]:
                    tree[a].append(key)
            else:
                tree[a] = []
        key = a
    return tree

print(solution(19,[0, 1, 2, 1, 3, 4, 3, 5, 3, 1, 6, 1, 0, 7, 8, 7, 9, 7, 0]))
