def scan_board(m, n, board):
    can_delete = 0
    check_board = [[0]*n for _ in range(m)]
    for i, v in enumerate(board[:m - 1]):
        for j, block in enumerate(v[:n - 1]):
            if block != ' ' and block == board[i][j+1] and block == board[i+1][j] and block == board[i+1][j+1]:
                check_board[i][j] = 1
                can_delete = 1
    return can_delete, check_board

def pop_block(board, check_board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if check_board[i][j] == 1:
                board[i] = board[i][:j] + '  ' + board[i][j+2:]
                board[i+1] = board[i+1][:j] + '  ' + board[i+1][j+2:]
    return board

def rearrange_board(m, n, board):
    for j in range(n):
        for i in range(m-1,-1,-1):
            if board[i][j] == ' ':
                for k in range(i-1,-1,-1):
                    if board[k][j] != ' ':
                        board[i] = board[i][:j] + board[k][j] + board[i][j+1:]
                        board[k] = board[k][:j] + ' ' + board[k][j+1:]
                        break
    return board

def solution(m, n, board):
    answer = 0
    while True:
        can_delete, check_board = scan_board(m, n, board)
        if can_delete == 0:
            break
        board = pop_block(board, check_board)
        board = rearrange_board(m, n, board)
    for i in board:
        answer += i.count(" ")
    return answer
