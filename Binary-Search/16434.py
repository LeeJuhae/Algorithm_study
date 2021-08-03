# https://www.acmicpc.net/problem/16434

import sys

def fight(mid, attack):
	hp = mid
	my_a = attack
	for t, a, h in rooms:
		if t == 1:
			atk_cnt = h // my_a
			atk_cnt += 1 if h % my_a else 0

			my_cnt = hp // a
			my_cnt += 1 if hp % a else 0

			if atk_cnt > my_cnt:
				return False
			hp -= a * (atk_cnt - 1)
		else:
			my_a += a
			hp = min(mid, hp + h)
	return True

n, attack = map(int, sys.stdin.readline().split())
rooms = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

left, right = 1, 1000000 * 1000000 * 123456
max_hp = 0
while left <= right:
	mid = (left + right) // 2
	if fight(mid, attack):
		max_hp = mid
		right = mid - 1
	else:
		left = mid + 1
print(max_hp)
