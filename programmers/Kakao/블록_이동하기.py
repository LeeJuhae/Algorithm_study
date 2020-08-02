'''
ref.) https://medium.com/@dltkddud4403/2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EB%B8%94%EB%9D%BC%EC%9D%B8%EB%93%9C-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EB%B8%94%EB%A1%9D-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0-57d668a744d0
'''
from collections import deque

def move(loc1,loc2,board):
    move = [(1,0), (0,1), (-1,0), (0,-1)]
    rotate=[1,-1]
    ret=[]
    for m in move:
        if board[loc1[0]+m[0]][loc1[1]+m[1]]==0 and board[loc2[0]+m[0]][loc2[1]+m[1]]==0:
            ret.append({(loc1[0]+m[0],loc1[1]+m[1]),(loc2[0]+m[0],loc2[1]+m[1])})
            
    if loc1[0]==loc2[0]:
        for r in rotate:
            if board[loc1[0]+r][loc1[1]]==0 and board[loc2[0]+r][loc2[1]]==0:
                ret.append({(loc1[0]+r,loc1[1]),(loc1[0],loc1[1])})
                ret.append({(loc2[0]+r,loc2[1]),(loc2[0],loc2[1])})
    else:
        for r in rotate:
            if board[loc1[0]][loc1[1]+r]==0 and board[loc2[0]][loc2[1]+r]==0:
                ret.append({(loc1[0],loc1[1]),(loc1[0],loc1[1]+r)})
                ret.append({(loc2[0],loc2[1]),(loc2[0],loc2[1]+r)})
    return ret

def solution(board):
    size = len(board)
    new_board = [[1 for i in range(len(board)+2)] for i in range(len(board)+2)]
    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i+1][j+1] = board[i][j]
    que = deque()
    visited = []
    que.append([{(1,1),(1,2)},0])
    visited.append({(1,1),(1,2)})
    while len(que) != 0:
        temp = que.popleft()
        location = list(temp[0])
        dist = temp[1]+1
        move_list = move(location[0],location[1],new_board)
        for m in move_list:
            if (size, size) in m: 
                return dist
            if not m in visited:
                que.append([m,dist])
                visited.append(m)
    return 0
