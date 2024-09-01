import random

from random_int import quess

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
  0 |
    |
    |
   ===''', '''
+---+
  0 |
  | |
    |
   ===''', '''
+---+
  0 |
 /| |
    |
   ===''', '''
+---+
  0 |
 /|\|
    |
   ===''', '''
+---+
  0 |
 /|\|
 /  |
   ===''', '''
+---+
  0 |
 /|\|
 / \|
   ===''']

words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея
         индюк кит кобра коза козел койот корова кролик крыса курица лама ласка лебедь лев лиса лосось лось
         лягушка медведь моллюск моль мул муравей мышь норка носорок обезьяна овца окунь олень орел осел
        панда паук питорн попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Введите букву,')
        quess = input()
        quess = quess.lower()
        if len(quess) != 1:
            print('Пожалуйста введите одну букву')
        elif quess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую')
        elif quess not in 'абвгдуужзийклмнопрстуфчцчшщъыьэюя':
            print('Пожалуйста введите букву')
        else:
            return quess

def playAgain():
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')

print('В И С Е Л И Ц Ф')

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    quess = getGuess(missedLetters + correctLetters)

    if quess in secretWord:
        correctLetters = correctLetters + quess

        foundAllLetters = True

        for i in range(len(secretWord)):
            if secretWord[i] in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Да! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + quess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break