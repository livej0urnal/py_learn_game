import random

NUM_DIGITS = 3
MAX_GUEST = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Guessed Correct!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Hot')
        elif guess[i] in secretNum:
            clues.append('Warm')
    if len(clues) == 0:
        return 'Cold!'

    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

print('Я загадаю %s-x значное число, которое вы должны отгадатью' % (NUM_DIGITS))
print('Я дам несколько подсказок..')
print('Когда я говорю: Это означает:')
print(' Cold Ни одна цифра не отгадана')
print(' Warm Одна цифра отгадана, но не отгадана ее позиция.')
print(' Hot  Одна цифра и ее позиция отгаданы')

while True:
    secretNum = getSecretNum()
    print('Итак я загадал число. Теперь у вас есть %s попыток, чтобы отгадать его.' % (MAX_GUEST))

    quessesTaken = 1
    while quessesTaken <= MAX_GUEST:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Попытка %s ' % (quessesTaken))
            quess = input()\

        print(getClues(guess, secretNum))
        quessesTaken += 1

        if guess == secretNum:
            break
        if quessesTaken > MAX_GUEST:
            print('Попыток больше не осталось. Я загадал число %s.' % (secretNum))
    print('Хотите сыграть еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break