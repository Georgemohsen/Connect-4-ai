from Score import *
import numpy as np
from tree import *
#from alphabeta import *
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

if __name__ =="__main__" :

    #hena part el code eli nersem fih el shakl w ne2ool l el user yel3ab w make_move hatraga3li board f nersemha
    bboard=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    print(bboard)

    #hena 3arafna board 2D array w kolaha zeroes

    nefe3,newbboard= make_move(0,bboard,4) #awel parameter beia5od el column number w tani wa7ed beia5od board w beierga3 bool w board el gedida
    if nefe3:
        draw=True #sheel true di w ersem el board el gedida (newbboard)
    else :
        print("el3ab le3ba tania") #w 5ali user yel3ab tani
    print (newbboard)
    #fi dor el AI hanendah el tree function w nediha el board eli tel3et mn make_move beta3et el user zai eli gai

    rroot=tree(newbboard)
    kher=alphabeta(rroot,0,False,-999999,999999)#nendah  hena el alphabeta w kher di bethil el score malhash lazma
    print(kher)
    print(play.br) #el board eli matloob tersemha w kda AI yekoon le3eb hatkoon fi " play.bt " di
    print(RenderTree(rroot))# w di rasmet el tree lw 3aiez te3mel check