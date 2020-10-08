# 60 / 100
def solution(balloons):
	answer = 1
	l_min = balloons[0]
	r_min = min(balloons[1:])
	for idx in range(1,len(balloons)):
		if balloons[idx] == r_min:
			if idx +1 != len(balloons):
				r_min = min(balloons[idx+1:])
				if max(l_min, r_min, balloons[idx]) != balloons[idx]:
					answer += 1
				l_min = min(l_min, balloons[idx])
			else:
				answer += 1
		else:
			if max(l_min, r_min, balloons[idx]) != balloons[idx]:
				answer += 1
			l_min = min(l_min, balloons[idx])
	return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
# print(solution([9,-1,-5]))

# def canBeLeft(b_idx, balloons):
# 	balloon = balloons[b_idx]
# 	temp = [balloon]
# 	if b_idx != 0:
# 		temp.insert(0, min(balloons[:b_idx]))
# 	if b_idx != len(balloons)-1:
# 		temp.append(min(balloons[b_idx+1:]))
# 	if len(temp) == 3 and max(temp) == balloon:
# 		return False
# 	return True
# def solution(balloons):
# 	answer = 0
# 	for idx in range(len(balloons)):
# 		if canBeLeft(idx, balloons):
# 			answer += 1
# 	return answer


# def solution(balloons):
# 	answer = 1
# 	l_min = balloons[0]
# 	r_min = min(balloons[1:])
# 	for idx in range(1,len(balloons)):
# 		if balloons[idx] == r_min:
# 			if idx +1 != len(balloons):
# 				r_min = min(balloons[idx+1:])
# 				if max(l_min, r_min, balloons[idx]) != balloons[idx]:
# 					answer += 1
# 				l_min = min(l_min, balloons[idx])
# 			else:
# 				answer += 1
# 		else:
# 			if max(l_min, r_min, balloons[idx]) != balloons[idx]:
# 				answer += 1
# 			l_min = min(l_min, balloons[idx])
# 	return answer
