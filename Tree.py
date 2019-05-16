from anytree import RenderTree, AnyNode

from Score import *
import copy




def make_move(col, board, p):

    temp_board = copy.deepcopy(board)

    if board[5][col] == 0:

        for i in range(0, 6):

            if board[i][col] == 0:

                temp_board[i][col] = p

                return True, temp_board

    else:

        return False, board





def tree(board):

    root=AnyNode(br=board,score=score(board))

    lvl1 = []

    lvl2 = []

    lvl3 = []
    lvl4=[]
    lvl5=[]
    lvl6=[]
    lvl7=[]

    nodes1=[]

    nodes2=[]

    nodes3=[]
    nodes4 = []
    nodes5 = []
    nodes6 = []
    nodes7= []

    for j in range(0,7):

        flag, new_board = make_move(j, board, 1)

        if flag:

            lvl1.append(new_board)

            nodes1.append(AnyNode(br=new_board,parent=root,score=score(new_board)))

    k=0

    for b in lvl1:
        kawent4=connect4(b)
        if kawent4 == 2 or kawent4==1 :
            k+=1
        else:
            for j in range(0, 7):

                flag, new_board = make_move(j, b, 4)

                if flag:

                    lvl2.append(new_board)

                    nodes2.append(AnyNode(br=new_board,parent=nodes1[k],score=score(new_board)))

            k+=1

    kk=0

    for b in lvl2:
        kawent4 = connect4(b)
        if kawent4 == 2 or kawent4 == 1:
            kk += 1
        else:
            for j in range(0, 7):

                flag, new_board = make_move(j, b, 1)

                if flag:

                    lvl3.append(new_board)

                    nodes3.append(AnyNode(br=new_board,parent=nodes2[kk],score=score(new_board)))

            kk+=1
    kkk=0
    for b in lvl3:
        kawent4 = connect4(b)
        if kawent4 == 2 or kawent4 == 1:
            kkk += 1
        else:
            for j in range(0, 7):

                flag, new_board = make_move(j, b, 1)

                if flag:
                    lvl4.append(new_board)

                    nodes4.append(AnyNode(br=new_board, parent=nodes3[kkk], score=score(new_board)))

            kkk += 1

    kkkk = 0
    for b in lvl4:
        kawent4 = connect4(b)
        if kawent4 == 2 or kawent4 == 1:
            kkkk += 1
        else:
            for j in range(0, 7):

                flag, new_board = make_move(j, b, 1)

                if flag:
                    lvl5.append(new_board)

                    nodes5.append(AnyNode(br=new_board, parent=nodes4[kkkk], score=score(new_board)))

            kkkk += 1




    return root
