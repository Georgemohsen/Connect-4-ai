from anytree import RenderTree, AnyNode
def make_move(col, board, p):
    if board[5][col] == 0:
        for i in range(0, 6):
            if board[i][col] == 0:
                board[i][col] = p
                return True, board
    else:
        return False, board


def tree(board):
    root=AnyNode(board,score=0)
    lvl1 = []
    lvl2 = []
    lvl3 = []
    nodes1=[]
    nodes2=[]
    nodes3=[]
    for j in range(0,7):
        flag, new_board = make_move(j, board, 1)
        if flag:
            lvl1.append(new_board)
            nodes1.append(AnyNode(new_board,parent=root,score=0))
    for b in lvl1:
        for j in range(0, 7):
            flag, new_board = make_move(j, b, 4)
            if flag:
                lvl2.append(new_board)
                nodes2.append(AnyNode(new_board,parent=nodes1[b],score=0))
    for b in lvl2:
        for j in range(0, 7):
            flag, new_board = make_move(j, b, 1)
            if flag:
                lvl3.append(new_board)
                nodes3.append(AnyNode(new_board,parent=nodes2[b],score=0))
    return lvl1, lvl2, lvl3
