import random
import time

def displayIntro():
    print('''Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры. В одной из них дружелюбный дракон,
    который готов поделиться с Вами своими сокровищами. Во второй - 
    жадный и голодный дракон, который мигом вас сьест.''')
    print()
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
        cave = input()
    
    return cave

def checkCave(chooseCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед Вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chooseCave == str(friendlyCave):
        print('...делится с Вами своими сокровищами!')
    else:
        print('...моментально Вас сьедает!')

playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input()
