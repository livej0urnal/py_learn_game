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
        for column in range(60):
            boardRow += board[column][row]
    print('%s%s %s' % (extraSpace, row, boardRow, row))
    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChest(numChests):
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests:
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    smallestDistance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
        if distance < smallestDistance:
            smallestDistance = distance
    smallestDistance = round(smallestDistance)
    if smallestDistance == 0:
        chests.remove((x, y))
        return 'Вы нашли сундук с сокровищами на затонувшем судне!'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
        else:
            board[x][y] = 'X'
