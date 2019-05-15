from anytree import Node, RenderTree, AnyNode
play=AnyNode
def alphabeta(position,level,isMin,alpha,beta):
    global play
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
            sscore = alphabeta(y, level + 1, True, alpha, beta)
            if ScoreToPlay < sscore:
                ScoreToPlay = sscore
            if alpha < ScoreToPlay:
                alpha = ScoreToPlay
                if level==0 :
                    play=y

            if beta <= alpha:
                break
        return ScoreToPlay

#just for testing w el id dah badal shakl el board masalan
if __name__ =="__main__" :


    udo=AnyNode(id="udo",score=0)
    lian=AnyNode(id="lian", parent=udo,score=0)
    marco=AnyNode(id="marco",parent=udo,score=0)
    haf=AnyNode(id="haf", parent=lian,score=0)
    haw = AnyNode(id="haw", parent=lian, score=0)
    maf = AnyNode(id="maf", parent=marco, score=0)
    maw = AnyNode(id="maw", parent=marco, score=5)
    h=AnyNode(id="h", parent=haf, score=25)
    k=AnyNode(id="k", parent=haf, score=35)
    a=AnyNode(id="a", parent=haw, score=12)
    s=AnyNode(id="s", parent=haw, score=26)
    q=AnyNode(id="q", parent=maf, score=60)
    w=AnyNode(id="w", parent=maf, score=54)
    vn=AnyNode(id="vn", parent=maw, score=25)

    elmafrood=alphabeta(udo,0,False,-999999,999999)
    print(RenderTree(udo))
    print(elmafrood)
    print(play)




