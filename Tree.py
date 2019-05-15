def make_move(col, board, p):
    if board[5][col] == 0:
        for i in range(0, 6):
            if board[i][col] == 0:
                board[i][col] = p
                return True, board
    else:
        return False, board


def tree(board):
    lvl1 = []
    lvl2 = []
    lvl3 = []
    for j in range(0,7):
        flag, new_board = make_move(j, board, 1)
        if flag:
            lvl1.append(new_board)
    for b in lvl1:
        for j in range(0, 7):
            flag, new_board = make_move(j, b, 4)
            if flag:
                lvl2.append(new_board)
    for b in lvl2:
        for j in range(0, 7):
            flag, new_board = make_move(j, b, 1)
            if flag:
                lvl3.append(new_board)
    return lvl1, lvl2, lvl3
