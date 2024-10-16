import random
import sys
import math


def getNewBoard():
    board = []
    for x in range(60):
        board.append([])
    for y in range(15):
        if random.randint(0, 1) == 0:
            board[x].append('~')
        else:
            board[x].append('`')
    return board

def drawBoard(board):
    tensDigitsLine = ''
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)
    print(tensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()

    for row in range(15):
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        boardRow = ''