import random

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
 /|\\|
    |
   ===''', '''
+---+
  0 |
 /|\\|
 /  |
   ===''', '''
+---+
  0 |
 /|\\|
 / \\|
   ===''', '''
+---+
[ O |
 /|\\ |
 / \\ |
 ===''', '''
+---+
[O] |
 /|\\ |
 / \\ |
 ===''']


words = {'Цвета': 'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
         'Фигуры': 'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм пятиугольник шестиугольник восьмиугольник'.split(),
         'Фрукты': 'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split(),
         'Животные': 'аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик крыса лев лиса лось медведь мул мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова тигр тюлень хорек ящерица'.split()}


def getRandomWord(wordList):
    wordKey = random.choice(list(wordList.keys()))
    wordIndex = random.randint(0, len(wordList[wordKey]) - 1)
    return wordList[wordKey][wordIndex], wordKey


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
        print('Введите букву: ')
        guess = input().lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите букву русского алфавита.')
        else:
            return guess


def playAgain():
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')


print('В И С Е Л И Ц А')

difficulty = ''
while difficulty not in 'ЛСТ':
    print('Выберите уровень сложности: Л - легкий, С - средний, Т - тяжелый')
    difficulty = input().upper()

if difficulty == 'С':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]

if difficulty == 'T':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False


while True:
    print('Секретное слово из набора: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Получаем букву от игрока
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess

        # Проверяем, угаданы ли все буквы
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Да! Секретное слово - "' + secretWord + '"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters += guess

        # Если все картинки использованы — игрок проиграл
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\nНеугаданное слово: "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
