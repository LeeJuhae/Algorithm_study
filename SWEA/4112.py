'''
	SWEA - 4112.이상한 피라미드 탐험
	언어 : Python
	메모리 : 67,828kb
	실행시간 : 403ms
	코드길이 : 636
'''
def get_location(ele):
    i = 2
    num = 1
    pre_num = 0
    while True:
        if ele > num:
            pre_num = num
            num += i
            i += 1
        else:
            return [i-1, ele-pre_num]
 
def dfs(node, target, depth):
    if node[0] == target[0]:
        return depth + abs(target[1]-node[1])
    node[0] += 1
    node[1] = node[1] + ( 1 if node[1] < target[1] else 0)
    return dfs(node, target, depth+1)
 
def solution(testcase):
    a = min(testcase)
    b = max(testcase)
    a_loc = get_location(a)
    b_loc = get_location(b)
    return dfs(a_loc,b_loc,0)
 
N = int(input())
testcases = []
for i in range(1, N+1):
    a, b= map(int, input().split(' '))
    print('#{} {}'.format(i, solution([a,b])))
		#print("#", str(i), " ", str(solution([a,b])))
