def rotate_right(map):
    new_map = []
    i = 0
    for row in map[::-1]:
        for item in row:
            if i < len(map) :
                new_map.append([item])
            else:
                new_map[i % len(map)].append(item)
            i += 1
    return new_map

def check_map(key, extend_key):
    E = len(extend_key)
    size = len(key)
    for i in range(E - size + 1):
        for col in range(size):
            for j in range(E - size + 1):
                for row in range(size):
                    if key[row][col] == 1 and extend_key[row + j][col + i] == 1:
                        return False
    return True

def solution(key, lock):
    if key.count(1) < lock.count(0):
        return False
    extend_key = []
    start_r, start_c = 20, 20
    M, N = len(key), len(lock)
    for row,items in enumerate(lock):
        temp = []
        for col,item in enumerate(items):
            temp.append(0 if item == 1 else 1)
            if item == 0:
                start_r = min(start_r, row)
                start_c = min(start_c, col)
        extend_key.append(temp)
    for row in extend_key:
        for i in range(M - start_c - 1):
            row.append(2)
    for i in range(M - start_r - 1):
        extend_key.append([2] * (M + start_r))
        
    for rotate_cnt in range(4):
        if check_map(key, extend_key) == False:
            return False
        key = rotate_right(key)
    return True
