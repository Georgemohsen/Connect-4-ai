import numpy as np


def score(board):
    ai_score = 0
    player_score = 0
    for i in range(0, 6):
        for j in range(0, 7):
            if board[i][j] == 1:
                if i-3 >= 0:
                    if board[i-3][j]+board[i-2][j]+board[i-1][j] == 0:
                        ai_score += 2
                    elif board[i - 3][j] + board[i - 2][j] + board[i - 1][j] == 1:
                        ai_score += 5
                    elif board[i - 3][j] + board[i - 2][j] + board[i - 1][j] == 2:
                        ai_score += 130
                if i+3 < 6:
                    if board[i+3][j]+board[i+2][j]+board[i+1][j] == 0:
                        ai_score += 2
                    elif board[i + 3][j] + board[i + 2][j] + board[i + 1][j] == 1:
                        ai_score += 5
                    elif board[i + 3][j] + board[i + 2][j] + board[i + 1][j] == 2:
                        ai_score += 130
                if j-3 >= 0:
                    if board[i][j-3]+board[i][j-2]+board[i][j-1] == 0:
                        ai_score += 2
                    elif board[i][j-3]+board[i][j-2]+board[i][j-1] == 1:
                        ai_score += 5
                    elif board[i][j-3]+board[i][j-2]+board[i][j-1] == 2:
                        ai_score += 130
                if j+3 < 7:
                    if board[i][j+3]+board[i][j+2]+board[i][j+3] == 0:
                        ai_score += 2
                    elif board[i][j+3]+board[i][j+2]+board[i][j+3] == 1:
                        ai_score += 5
                    elif board[i][j+3]+board[i][j+2]+board[i][j+3] == 2:
                        ai_score += 130
                if i-3 >= 0 and j-3 >= 0:
                    if board[i-3][j-3]+board[i-2][j-2]+board[i-1][j-1] == 1:
                        ai_score += 5
                    elif board[i-3][j-3]+board[i-2][j-2]+board[i-1][j-1] == 2:
                        ai_score += 130
                if i-3 >= 0 and j+3 < 7:
                    if board[i-3][j+3]+board[i-2][j+2]+board[i-1][j+1] == 1:
                        ai_score += 5
                    elif board[i-3][j+3]+board[i-2][j+2]+board[i-1][j+1] == 2:
                        ai_score += 130
                if i+3 < 6 and j+3 < 7:
                    if board[i+3][j+3]+board[i+2][j+2]+board[i+1][j+1] == 1:
                        ai_score += 5
                    elif board[i+3][j+3]+board[i+2][j+2]+board[i+1][j+1] == 2:
                        ai_score += 130
                if i+3 < 6 and j-3 >= 0:
                    if board[i+3][j-3]+board[i+2][j-2]+board[i+1][j-1] == 1:
                        ai_score += 5
                    elif board[i+3][j-3]+board[i+2][j-2]+board[i+1][j-1] == 2:
                        ai_score += 130
            elif board[i][j] == 4:
                if i - 3 >= 0:
                    if board[i - 3][j] + board[i - 2][j] + board[i - 1][j] == 0:
                        player_score += 2
                    elif board[i - 3][j] + board[i - 2][j] + board[i - 1][j] == 4:
                        player_score += 5
                    elif board[i - 3][j] + board[i - 2][j] + board[i - 1][j] == 8:
                        player_score += 100
                if i + 3 < 6:
                    if board[i + 3][j] + board[i + 2][j] + board[i + 1][j] == 0:
                        player_score += 2
                    elif board[i + 3][j] + board[i + 2][j] + board[i + 1][j] == 4:
                        player_score += 5
                    elif board[i + 3][j] + board[i + 2][j] + board[i + 1][j] == 8:
                        player_score += 100
                if j - 3 >= 0:
                    if board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 0:
                        player_score += 2
                    elif board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 4:
                        player_score += 5
                    elif board[i][j - 3] + board[i][j - 2] + board[i][j - 1] == 8:
                        player_score += 100
                if j + 3 < 7:
                    if board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 0:
                        player_score += 2
                    elif board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 4:
                        player_score += 5
                    elif board[i][j + 3] + board[i][j + 2] + board[i][j + 3] == 8:
                        player_score += 100
                if i - 3 >= 0 and j - 3 >= 0:
                    if board[i - 3][j - 3] + board[i - 2][j - 2] + board[i - 1][j - 1] == 4:
                        player_score += 5
                    elif board[i - 3][j - 3] + board[i - 2][j - 2] + board[i - 1][j - 1] == 8:
                        player_score += 100
                if i - 3 >= 0 and j + 3 < 7:
                    if board[i - 3][j + 3] + board[i - 2][j + 2] + board[i - 1][j + 1] == 4:
                        player_score += 5
                    elif board[i - 3][j + 3] + board[i - 2][j + 2] + board[i - 1][j + 1] == 8:
                        player_score += 100
                if i + 3 < 6 and j + 3 < 7:
                    if board[i + 3][j + 3] + board[i + 2][j + 2] + board[i + 1][j + 1] == 4:
                        player_score += 5
                    elif board[i + 3][j + 3] + board[i + 2][j + 2] + board[i + 1][j + 1] == 8:
                        player_score += 100
                if i + 3 < 6 and j - 3 >= 0:
                    if board[i + 3][j - 3] + board[i + 2][j - 2] + board[i + 1][j - 1] == 4:
                        player_score += 5
                    elif board[i + 3][j - 3] + board[i + 2][j - 2] + board[i + 1][j - 1] == 8:
                        player_score += 100
    return ai_score - player_score


def connect4(board): #returns 1 if ai wins , 2 if player wins, 0 if no win
    
    for i in range(0, 7):
        for j in range(0, 6):
            if board[i][j] == 1:
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
