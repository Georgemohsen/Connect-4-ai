import numpy as np


def score(board):
    ai_score = 0
    player_score = 0
    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == 1:
                flag = 0
                for k in range(i, 6):
                    if board[k][j] == 4 or board[k][j] == 1:
                        flag = 1
                        break
                if flag == 0:
                    if board[i-1][j] == 1:
                        if board[i-2][j] == 1 and i < 5:
                            if board[i-3][j] == 1:
                                ai_score += 10000
                            else: ai_score += 130
                        elif i < 4:
                            ai_score += 5
                    elif i < 3:
                        ai_score += 2
                if j - 3 >= 0:
                    if board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 0:
                        ai_score += 2
                    elif board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 1:
                        ai_score += 5
                    elif board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 2:
                        ai_score += 130
                    elif board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 3:
                        ai_score += 10000
                if j + 3 < 7:
                    if board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 0:
                        ai_score += 2
                    elif board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 1:
                        ai_score += 5
                    elif board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 2:
                        ai_score += 130
                    elif board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 3:
                        ai_score += 10000
                if i - 3 >= 0 and j - 3 >= 0:
                    if board[i - 3][j - 3] + board[i - 2][j - 2] + board[i - 1][j - 1] == 1:
                        ai_score += 5
                    elif board[i - 3][j - 3] + board[i - 2][j - 2] + board[i - 1][j - 1] == 2:
                        if board[i - 3][j - 3] == 0:
                            flag2 = 0
                            for k in range(0, i-3):
                                if board[k][j-3] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i-3-flag2)*50)
                        elif board[i - 2][j - 2] == 0:
                            flag2 = 0
                            for k in range(0, i-2):
                                if board[k][j-3] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i-2-flag2)*35)
                        elif board[i - 1][j - 1] == 0:
                            flag2 = 0
                            for k in range(0, i-1):
                                if board[k][j-3] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i-1-flag2)*25)
                    elif board[i - 3][j - 3] + board[i - 2][j - 2] + board[i - 1][j - 1] == 3:
                        ai_score += 10000
                if i - 3 >= 0 and j + 3 < 7:
                    if board[i - 3][j + 3] + board[i - 2][j + 2] + board[i - 1][j + 1] == 1:
                        ai_score += 5
                    elif board[i - 3][j + 3] + board[i - 2][j + 2] + board[i - 1][j + 1] == 2:
                        if board[i - 3][j + 3] == 0:
                            flag2 = 0
                            for k in range(0, i-3):
                                if board[k][j+3] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i-3-flag2)*50)
                        elif board[i - 2][j +2] == 0:
                            flag2 = 0
                            for k in range(0, i-2):
                                if board[k][j+2] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i-2-flag2)*35)
                        elif board[i - 1][j +1] == 0:
                            flag2 = 0
                            for k in range(0, i-1):
                                if board[k][j+1] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i-1-flag2)*25)
                    elif board[i - 3][j + 3] + board[i - 2][j + 2] + board[i - 1][j + 1] == 3:
                        ai_score += 10000
                if i + 3 < 6 and j + 3 < 7:
                    if board[i + 3][j + 3] + board[i + 2][j + 2] + board[i + 1][j + 1] == 1:
                        ai_score += 5
                    elif board[i + 3][j + 3] + board[i + 2][j + 2] + board[i + 1][j + 1] == 2:
                        if board[i + 3][j + 3] == 0:
                            flag2 = 0
                            for k in range(0, i+3):
                                if board[k][j+3] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i+3-flag2)*25)
                        elif board[i + 2][j +2] == 0:
                            flag2 = 0
                            for k in range(0, i+2):
                                if board[k][j+2] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i+2-flag2)*35)
                        elif board[i + 1][j +1] == 0:
                            flag2 = 0
                            for k in range(0, i+1):
                                if board[k][j+1] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i+1-flag2)*50)
                    elif board[i + 3][j + 3] + board[i + 2][j + 2] + board[i + 1][j + 1] == 3:
                        ai_score += 10000
                if i + 3 < 6 and j - 3 >= 0:
                    if board[i + 3][j - 3] + board[i + 2][j - 2] + board[i + 1][j - 1] == 1:
                        ai_score += 5
                    elif board[i + 3][j - 3] + board[i + 2][j - 2] + board[i + 1][j - 1] == 2:
                        if board[i + 3][j - 3] == 0:
                            flag2 = 0
                            for k in range(0, i+3):
                                if board[k][j-3] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i+3-flag2)*25)
                        elif board[i + 2][j -2] == 0:
                            flag2 = 0
                            for k in range(0, i+2):
                                if board[k][j-2] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i+2-flag2)*35)
                        elif board[i + 1][j -1] == 0:
                            flag2 = 0
                            for k in range(0, i+1):
                                if board[k][j-1] != 0:
                                    flag2 += 1
                                ai_score += 130 - ((i+1-flag2)*50)
                    elif board[i + 3][j - 3] + board[i + 2][j - 2] + board[i + 1][j - 1] == 3:
                        ai_score += 10000
            elif board[i][j] == 4:
                flag = 0
                for k in range(i, 6):
                    if board[k][j] == 4 or board[k][j] == 1:
                        flag = 1
                        break
                if flag == 0:
                    if board[i - 1][j] == 4:
                        if board[i - 2][j] == 4 and i < 5:
                            player_score += 9000
                        elif i < 4:
                            player_score += 5
                    elif i < 3:
                        player_score += 2
                if j - 3 >= 0:
                    if board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 0:
                        player_score += 2
                    elif board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 4:
                        player_score += 5
                    elif board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 8:
                        player_score += 9000
                if j + 3 < 7:
                    if board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 0:
                        player_score += 2
                    elif board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 4:
                        player_score += 5
                    elif board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 8:
                        player_score += 9000
                if i - 3 >= 0 and j - 3 >= 0:
                    if board[i - 3][j - 3] + board[i - 2][j - 2] + board[i - 1][j - 1] == 4:
                        player_score += 5
                    elif board[i - 3][j - 3] + board[i - 2][j - 2] + board[i - 1][j - 1] == 8:
                        if board[i - 3][j - 3] == 0:
                            flag2 = 0
                            for k in range(0, i-3):
                                if board[k][j-3] != 0:
                                    flag2 += 1
                                if flag2 == i-4:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i - 3 - flag2) * 50)
                        elif board[i - 2][j - 2] == 0:
                            flag2 = 0
                            for k in range(0, i-2):
                                if board[k][j-3] != 0:
                                    flag2 += 1
                                if flag2 == i-3:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i-2-flag2)*35)
                        elif board[i - 1][j - 1] == 0:
                            flag2 = 0
                            for k in range(0, i-1):
                                if board[k][j-3] != 0:
                                    flag2 += 1
                                if flag2 == i-2:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i-1-flag2)*25)
                if i - 3 >= 0 and j + 3 < 7:
                    if board[i - 3][j + 3] + board[i - 2][j + 2] + board[i - 1][j + 1] == 1:
                        player_score += 5
                    elif board[i - 3][j + 3] + board[i - 2][j + 2] + board[i - 1][j + 1] == 2:
                        if board[i - 3][j + 3] == 0:
                            flag2 = 0
                            for k in range(0, i-3):
                                if board[k][j+3] != 0:
                                    flag2 += 1
                                if flag2 == i-4:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i-3-flag2)*50)
                        elif board[i - 2][j +2] == 0:
                            flag2 = 0
                            for k in range(0, i-2):
                                if board[k][j+2] != 0:
                                    flag2 += 1
                                if flag2 == i-3:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i-2-flag2)*35)
                        elif board[i - 1][j +1] == 0:
                            flag2 = 0
                            for k in range(0, i-1):
                                if board[k][j+1] != 0:
                                    flag2 += 1
                                if flag2 == i-2:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i-1-flag2)*25)
                if i + 3 < 6 and j + 3 < 7:
                    if board[i + 3][j + 3] + board[i + 2][j + 2] + board[i + 1][j + 1] == 1:
                        player_score += 5
                    elif board[i + 3][j + 3] + board[i + 2][j + 2] + board[i + 1][j + 1] == 2:
                        if board[i + 3][j + 3] == 0:
                            flag2 = 0
                            for k in range(0, i+3):
                                if board[k][j+3] != 0:
                                    flag2 += 1
                                if flag2 == i+2:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i+3-flag2)*25)
                        elif board[i + 2][j +2] == 0:
                            flag2 = 0
                            for k in range(0, i+2):
                                if board[k][j+2] != 0:
                                    flag2 += 1
                                if flag2 == i+1:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i+2-flag2)*35)
                        elif board[i + 1][j +1] == 0:
                            flag2 = 0
                            for k in range(0, i+1):
                                if board[k][j+1] != 0:
                                    flag2 += 1
                                if flag2 == i:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i+1-flag2)*50)
                if i + 3 < 6 and j - 3 >= 0:
                    if board[i + 3][j - 3] + board[i + 2][j - 2] + board[i + 1][j - 1] == 1:
                        player_score += 5
                    elif board[i + 3][j - 3] + board[i + 2][j - 2] + board[i + 1][j - 1] == 2:
                        if board[i + 3][j - 3] == 0:
                            flag2 = 0
                            for k in range(0, i+3):
                                if board[k][j-3] != 0:
                                    flag2 += 1
                                if flag2 == i+2:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i+3-flag2)*25)
                        elif board[i + 2][j -2] == 0:
                            flag2 = 0
                            for k in range(0, i+2):
                                if board[k][j-2] != 0:
                                    flag2 += 1
                                if flag2 == i+1:
                                    player_score += 9000
                                else:
                                 player_score += 130 - ((i+2-flag2)*35)
                        elif board[i + 1][j -1] == 0:
                            flag2 = 0
                            for k in range(0, i+1):
                                if board[k][j-1] != 0:
                                    flag2 += 1
                                if flag2 == i:
                                    player_score += 9000
                                else:
                                    player_score += 130 - ((i+1-flag2)*50)
    return ai_score - player_score


def connect4(board):  # returns 1 if ai wins , 2 if player wins, 0 if no win

    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == 1:
                if i - 3 >= 0:
                    if board[i - 3][j] + board[i - 2][j] + board[i - 1][j] == 3:
                        return 1
                if i + 3 < 6:
                    if board[i + 3][j] + board[i + 2][j] + board[i + 1][j] == 3:
                        return 1
                if j - 3 >= 0:
                    if board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 3:
                        return 1
                if j + 3 < 7:
                    if board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 3:
                        return 1
                if i - 3 >= 0 and j - 3 >= 0:
                    if board[i - 3][j - 3] + board[i - 2][j - 2] + board[i - 1][j - 1] == 3:
                        return 1
                if i - 3 >= 0 and j + 3 < 7:
                    if board[i - 3][j + 3] + board[i - 2][j + 2] + board[i - 1][j + 1] == 3:
                        return 1
                if i + 3 < 6 and j + 3 < 7:
                    if board[i + 3][j + 3] + board[i + 2][j + 2] + board[i + 1][j + 1] == 3:
                        return 1
                if i + 3 < 6 and j - 3 >= 0:
                    if board[i + 3][j - 3] + board[i + 2][j - 2] + board[i + 1][j - 1] == 3:
                        return 1
            elif board[i][j] == 4:
                if i - 3 >= 0:
                    if board[i - 3][j] + board[i - 2][j] + board[i - 1][j] == 12:
                        return 2
                if i + 3 < 6:
                    if board[i + 3][j] + board[i + 2][j] + board[i + 1][j] == 12:
                        return 2
                if j - 3 >= 0:
                    if board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 12:
                        return 2
                if j + 3 < 7:
                    if board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 12:
                        return 2
                if i - 3 >= 0 and j - 3 >= 0:
                    if board[i - 3][j - 3] + board[i - 2][j - 2] + board[i - 1][j - 1] == 12:
                        return 2
                if i - 3 >= 0 and j + 3 < 7:
                    if board[i - 3][j + 3] + board[i - 2][j + 2] + board[i - 1][j + 1] == 12:
                        return 2
                if i + 3 < 6 and j + 3 < 7:
                    if board[i + 3][j + 3] + board[i + 2][j + 2] + board[i + 1][j + 1] == 12:
                        return 2
                if i + 3 < 6 and j - 3 >= 0:
                    if board[i + 3][j - 3] + board[i + 2][j - 2] + board[i + 1][j - 1] == 12:
                        return 2
    return 0

def Connect4(board): #returns 1 if ai wins , 2 if player wins, 0 if no win
    
    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == 4:
                if i-3 >= 0:
                    if board[i-3][j]+board[i-2][j]+board[i-1][j] == 3:
                        return 1
                    elif board[i-3][j]+board[i-2][j]+board[i-1][j] == 12:
                        return 2
                if i+3 < 6:
                    if board[i+3][j]+board[i+2][j]+board[i+1][j] == 3:
                        return 1
                    elif board[i + 3][j] + board[i + 2][j] + board[i + 1][j] == 12:
                        return 2
                if j-3 >= 0:
                    if board[i][j-3]+board[i][j-2]+board[i][j-1] == 3:
                        return 1
                    elif board[i][j-3]+board[i][j-2]+board[i][j-1] == 12:
                        return 2
                if j+3 < 7:
                    if board[i][j+3]+board[i][j+2]+board[i][j+3] == 3:
                        return 1
                    elif board[i][j+3]+board[i][j+2]+board[i][j+3] == 12:
                        return 2
                if i-3 >= 0 and j-3 >= 0:
                    if board[i-3][j-3]+board[i-2][j-2]+board[i-1][j-1] == 12:
                        return 2
                    elif board[i-3][j-3]+board[i-2][j-2]+board[i-1][j-1] == 3:
                        return 1
                if i-3 >= 0 and j+3 < 7:
                    if board[i-3][j+3]+board[i-2][j+2]+board[i-1][j+1] == 12:
                        return 2
                    elif board[i-3][j+3]+board[i-2][j+2]+board[i-1][j+1] == 3:
                        return 1
                if i+3 < 6 and j+3 < 7:
                    if board[i+3][j+3]+board[i+2][j+2]+board[i+1][j+1] == 12:
                        return 2
                    elif board[i+3][j+3]+board[i+2][j+2]+board[i+1][j+1] == 3:
                        return 1
                if i+3 < 6 and j-3 >= 0:
                    if board[i+3][j-3]+board[i+2][j-2]+board[i+1][j-1] == 12:
                        return 2
                    elif board[i+3][j-3]+board[i+2][j-2]+board[i+1][j-1] == 3:
                        return 1
    return 0
