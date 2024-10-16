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
            return 'Сундук с сокровищами обнаружен на расстоянии %s от гидролокатора.' % (smallestDistance)
        else:
            board[x][y] = 'X'
            return 'Гидролокатор ничего не обнаружил. Все сундуки с сокровищами вне пределов досягаемости.'

def enterPlayerMove(previousMoves):
    print('Где следует опустить гидролокатор? (координаты: 0-59 0-14) (или введите "выход")')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Thanks for playing!')
            sys.exit()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('Здесь вы уже опускали гидролокатор.')
                continue
        print('Введите число от 0 до 59, потом пробел, а затем число от 0 до 14.')


def showInstructions():
    print('''Инструктаж:
Вы - капитан корабля, плывущего за сокровищами. Ваша задача - с помощью
гидролокаторов найти три сундука с сокровищами в затонувших судах на дне океана.
Но гидролокаторы очень просты и определяют только расстояние, но не направление.				
Введите координаты, чтобы опустить гидролокатор в воду. На карте будет показано
число, обозначающее, на каком расстоянии находится ближайший сундук. Или будет
показана буква Х, обозначающая, что сундук в области действия гидролокатора не 
обнаружен. На карте ниже метки C - это сундуки. 
Цифра 3 обозначает, что ближайший сундук находится на отдалении в 3 единицы.

                            1         2         3
                  012345678901234567890123456789012

                0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
                1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
                2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
                3 ````````~~~`````~~~`~`````~`~``~` 3
                4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

                  012345678901234567890123456789012		
                            1         2         3
(Во время игры сундуки на карте не обозначаются!)

Нажмите клавишу Enter, чтобы продолжить...''')
    input()

    print('''Если гидролокатор опущен прямо на сундук, вы сможете поднять
сундук. Другие гидролокаторы обновят данные о расположении ближайшего сундука.
Сундуки ниже находятся вне диапазона локатора, поэтому отображается буква X.		

                            1         2         3
                  012345678901234567890123456789012		

                0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
                1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
                2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
                3 ````````~~~`````~~~`~`````~`~``~` 3
                4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

                  012345678901234567890123456789012
                            1         2         3

Сундуки с сокровищами не перемещаются. Гидролокаторы определяют сундуки
на расстоянии до 9 единиц. Попробуйте поднять все 3 сундука до того, как все
гидролокаторы будут опущены на дно. Удачи!		

Нажмите клавишу Enter, чтобы продолжить...''')
    input()


print('Охотник за сокровищами!')
print()
print('Показать инструктаж? (да/нет)')
if input().lower().startswith('д'):
    showInstructions()

while True:
    # Настройка игры
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        # Показать сонарные устройства и сундуки с сокровищами.
        print('Осталось гидролокаторов: %s. Осталось сундуков с сокровищами: %s.' % (sonarDevices, len(theChests)))

        x, y = enterPlayerMove(previousMoves)
        previousMoves.append([x, y])  # Мы должны отслеживать все ходы, чтобы сонары могли обновляться.

        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'Вы нашли сундук с сокровищами на затонувшем судне!':
                # Обновить все сонарные устройства, в настоящее время находящиеся на карте.
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)

        if len(theChests) == 0:
            print('Вы нашли все сундуки с сокровищами на затонувших судах! Поздравляем и приятной игры!')
            break

        sonarDevices -= 1

    if sonarDevices == 0:
        print('Все гидролокаторы опущены на дно! Придется разворачивать корабль и')
        print('отправляться домой, в порт! Игра окончена.')
        print('Вы не нашли сундуки в следующих местах:')
        for x, y in theChests:
            print('	%s, %s' % (x, y))

    print('Хотите сыграть еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        sys.exit()

