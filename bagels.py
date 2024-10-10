import random

NUM_DIGITS = 3
MAX_GUESSES = 10


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
    # Проверяем, что строка состоит только из цифр и не пуста
    return num.isdigit()


print('Я загадаю %s-значное число, которое вы должны отгадать.' % (NUM_DIGITS))
print('Я дам несколько подсказок..')
print('Когда я говорю: Это означает:')
print(' Cold - Ни одна цифра не отгадана')
print(' Warm - Одна цифра отгадана, но не отгадана ее позиция.')
print(' Hot  - Одна цифра и ее позиция отгаданы')

while True:
    secretNum = getSecretNum()
    print('Итак, я загадал число. Теперь у вас есть %s попыток, чтобы отгадать его.' % (MAX_GUESSES))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESSES:
        guess = ''
        # Требуем корректный ввод, пока не получим 3-значное число
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Попытка %s: Введите %s-значное число.' % (guessesTaken, NUM_DIGITS))
            guess = input().strip()  # Убираем пробелы по краям, если они есть

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            print('Вы угадали число за %s попыток!' % guessesTaken)
            break

        if guessesTaken > MAX_GUESSES:
            print('Попыток больше не осталось. Я загадал число %s.' % (secretNum))

    print('Хотите сыграть еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
