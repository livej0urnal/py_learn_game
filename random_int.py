import random

quessesTaken = 0

print('Hello. What is you name?')

myName = input()

number = random.randint(1, 20)

print('Please , ' + myName + ' select integer from 1 to 20.')

for quessesTaken in range(6):
    print('Select integer ')
    quess = input()
    quess = int(quess)
    
    if quess < number:
        print('You number very small')
    
    if quess > number:
        print('You number very big')
        
    if quess == number:
        break
    
if quess == number:
    quessesTaken = str(quessesTaken + 1)
    print('Nice ' + myName + '! Correct ' + quessesTaken + ' attempt')
    
if quess != number:
    number = str(number)
    print('Its not correct ' + number)