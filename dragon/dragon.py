import random, time

secret = random.randint(1, 2)
print('Перед вами две пещеры. В одной из них спрятано сокровище, в другой сидит голодный дракон. Какую пещеру вы выберете (1 или 2)?')
userChoice = int(input())

time.sleep(1)
print('Вы заходите в пещеру...')
time.sleep(2)
print('В пещере темно и сыро...')
time.sleep(2)
print('Вы включаете фонарь и видите...')
time.sleep(2)

if secret == userChoice:
    print('Сундук с сокровищами. Теперь вы богаты!')
else:
    print('Глаза огромного дракона! К сожалению, вы проиграли...')