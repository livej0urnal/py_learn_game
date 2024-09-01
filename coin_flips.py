import random

print('Я подброшу монетку 1000 раз. Угадай сколько раз выпадет "Орел"? (Нажмите Enter, чтобы начать)')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0,1) == 1:
        heads = heads + 1
    flips = flips + 1

