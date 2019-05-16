from Tree import tree, make_move
from Score import score, connect4
from anytree import RenderTree, AnyNode
import numpy as np

play=AnyNode # da global variable fi kol mara tendah alpha beta haigilak fiha el node eli el mafrood tero7laha

#dah el alphabrta function
def alphabeta(position,level,isMin,alpha,beta):
    global play
    pplay=AnyNode
    if position.is_leaf :
        return position.score
    if isMin:
        ScoreToPlay = 999999
        for i in position.children:
           sscore=alphabeta(i,level+1,False,alpha,beta)
           if ScoreToPlay > sscore:
               ScoreToPlay = sscore
           if beta > ScoreToPlay:
               beta = ScoreToPlay
           if beta <= alpha:
               break
        return ScoreToPlay
    else :
        ScoreToPlay = -999999
        for y in position.children :
            sscore= alphabeta(y, level + 1, True, alpha, beta)
            if ScoreToPlay < sscore:
                ScoreToPlay = sscore
            if alpha < ScoreToPlay:
                alpha = ScoreToPlay
                if level==0 :
                    play=y

            if beta <= alpha:
                break
        return ScoreToPlay

def draw(board):
    for row in range(0,6):
        for col in range(0,7):
            if board[row][col] == 4:
                print("|x", end='')
            elif board[row][col] == 1:
                print("|0", end='')    
            else:
                print("| ", end='')  
        print("|")       

def game():
    board = np.zeros((6,7), dtype=int)
    draw(board)
    i=0
    while True:
        col = input("Enter Col: ")    
        if i ==0:
            _, board =make_move(int(col), board, 4)
            draw(np.flipud(board))
            root = tree(board)
            _ = alphabeta(root, 0,False,-999999,999999)
            draw(np.flipud(play.br))
        else:
            _, board =make_move(int(col), play.br, 4)
            draw(np.flipud(board))
            root = tree(board)
            _ = alphabeta(root, 0,False,-999999,999999)
            draw(np.flipud(play.br))
        i=i+1

if __name__ == "__main__":
    game()