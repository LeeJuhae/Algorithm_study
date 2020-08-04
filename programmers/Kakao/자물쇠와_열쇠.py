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

def check_map(key, lock, ori_lock_zero_cnt):
	key_size = len(key)
	lock_size = len(lock)
	key_one_cnt = 0
	lock_zero_cnt = 0
	for key_rows in key:
		key_one_cnt += key_rows.count(1)

	for lock_r_start in range(lock_size - key_size + 1):
		for lock_c_start in range(lock_size - key_size + 1):
			lock_zero_cnt = 0
			for key_r in range(key_size):
				for key_c in range(key_size):
					if lock[lock_r_start+key_r][lock_c_start+key_c] == 0:
						lock_zero_cnt += 1
			if ori_lock_zero_cnt != lock_zero_cnt:
				continue
			isFit = True
			for key_r in range(key_size):
				for key_c in range(key_size):
					lock_r = lock_r_start + key_r
					lock_c = lock_c_start + key_c
					if key[key_r][key_c]== 1 and lock[lock_r][lock_c] == 0:
						lock_zero_cnt -= 1
					if lock[lock_r][lock_c] != 2 and key[key_r][key_c] == lock[lock_r][lock_c]:
						isFit = False
						break
				if isFit == False:
					break
			if isFit == True and lock_zero_cnt == 0:
				return True
	return False

def get_extended_lock(key, lock):
	key_size = len(key)
	lock_size = len(lock)
	#extended_reversed_lock = [[0] * (lock_size + 2*(key_size-1))] * (lock_size + 2*(key_size-1))
	extended_lock = [[2 for i in range(lock_size + 2*(key_size-1))] for j in range(lock_size + 2*(key_size-1))]
	for r_idx in range(lock_size):
		for c_idx in range(lock_size):
			extended_lock[r_idx+key_size-1][c_idx+key_size-1] = lock[r_idx][c_idx]
	return extended_lock

def solution(key, lock):
	lock_zero_cnt = 0
	for lock_rows in lock:
		lock_zero_cnt += lock_rows.count(0)
	extended_lock = get_extended_lock(key, lock)
	for i in range(4):
		if check_map(key, extended_lock, lock_zero_cnt) == True:
			return True
		key = rotate_right(key)
	return False

#print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
