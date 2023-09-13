# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 08:47:11 2021

@author: 1531402
"""

import sys
board = "........."
turn = 0
computerToken = 'X'
playerToken = 'O'
#turn = 1

def gameOver(board): #TEST FOR ROWS, COLS, DIAGS
    for i in range(3):
        if(board[3*i]==board[3*i+1] and board[3*i+1]==board[3*i+2]):
            if(not board[3*i]=='.'): return board[3*i]
        if(board[i]==board[i+3] and board[i]==board[i+6]):
            if(not board[i]=='.'): return board[i]
    if(board[0]==board[4] and board[4]==board[8]):
        if(not board[0]=='.'): return board[0]
    if(board[2]==board[4] and board[4]==board[6]): 
        if(not board[2]=='.'): return board[2]
    if('.' not in board): return "full"
    return None

def choose_move(board):
    best_result = max_step(board)
    ind = 0
    i = 0
    ilist = indexList(board, 2)
    for next_board in possible_next(board, turn):
        k = min_step(next_board)
        k2 = ""
        if(k==0): k2 = "tie"
        if(k==1): k2 = "win"
        if(k==-1): k2 = "loss"
        print("space " + str(ilist[i]) + ": " + str(k2))
        if(k==best_result):
            ind = ilist[i]
        i+=1
    return ind

def max_step(board):
    if(not gameOver(board)==None):
        if(gameOver(board)=="full"): return 0
        if(gameOver(board)==computerToken): return 1
        if(gameOver(board)==playerToken): return -1
    results = []
    for next_board in possible_next(board, 2):
        results.append(min_step(next_board))
    return max(results)
    
def min_step(board):
    if(not gameOver(board)==None):
        if(gameOver(board)=="full"): return 0
        if(gameOver(board)==computerToken): return 1
        if(gameOver(board)==playerToken): return -1
    results = []
    for next_board in possible_next(board, 1):
        results.append(max_step(next_board))
    return min(results)

def possible_next(board, turn):
    player = '.'
    if(turn%2==0): player = computerToken
    else: player = playerToken
    boardList = []
    for index in range(len(board)):
        if(board[index]=='.'): 
            boardList.append(board[0:index]+player+board[index+1:])
    return boardList

def indexList(board, turn):
    boardList = []
    for index in range(len(board)):
        if(board[index]=='.'): 
            boardList.append(index)
    return boardList

def printBoard(board):
    print(board[0:3] + "    " + "012")
    print(board[3:6]+ "    " + "345")
    print(board[6:9]+ "    " + "678")

"""
Accept one command line argument – a 9-character Tic Tac Toe board.
If the board is empty, ask the user (using an input statement) whether the computer should go first or the user should go first. X always plays first, but either the computer or the user might be player X.
If the board is not empty, assume that the computer plays next and figure out which token the computer should be. (Since X plays first, if there are an equal number of Xs and Os, X should play next. Otherwise, O.)
At each computer turn, your script should print out all possible moves and classify them as L (losing), T (tying), or W (winning), under the assumption of perfect play from both sides going forward.
At each player turn, just display the board and ask the player to type in a number from 0 to 8 to move.
Play perfectly.
"""

board = sys.argv[1]
if(board=='.........'):
    tur = input("who should go first? 0 for computer, 1 for player: ")
    if(tur=='0'):
        computerToken = 'X'
        playerToken = 'O'
        turn = 0
    if(tur=='1'):
        playerToken = 'X'
        computerToken = 'O'
        turn = 1
        printBoard(board)
else:
    xC = board.count('X')
    oC = board.count('O')
    if(xC==oC or xC<oC): 
        computerToken = 'X'
        playerToken = 'O'
        turn = 0
    else:
        computerToken = 'O'
        playerToken = 'X'
        turn = 0
    printBoard(board)
done = None
while(done==None):
    if(turn%2==0): 
        #X TURN
        print()
        move = choose_move(board)
        print("i choose "+ str(move))
        board = board[0:move] + computerToken + board[move+1:]
        print()
        printBoard(board)
    else:
        #O TURN
        move = int(input("your move: "))
        if(move<0 or move>8 or not board[move]=='.'):
            print("invalid move! try again")
            turn-=1
        else: board = board[0:move] + playerToken + board[move+1:]
        printBoard(board)
    turn+=1
    done = gameOver(board)

if(done==computerToken):
    print("i win!")
if(done==playerToken):
    print("you win")
if(done=='full'):
    print('tie!')