import random

NUM_DIGITS = 3
MAX_GUEST = 10

def secretNum():
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