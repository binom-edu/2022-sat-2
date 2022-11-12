import random, time

gameOn = True
while gameOn:
    secret = random.randint(1, 2)
    print('Перед вами две пещеры. В одной из них спрятано сокровище, в другой сидит голодный дракон. Какую пещеру вы выберете (1 или 2)?')
    userChoice = input()

    while userChoice != '1' and userChoice != '2':
        print('Недопустимый ввод. Выберите 1 или 2.')
        userChoice = input()

    time.sleep(1)
    print('Вы заходите в пещеру...')
    time.sleep(2)
    print('В пещере темно и сыро...')
    time.sleep(2)
    print('Вы включаете фонарь и видите...')
    time.sleep(2)

    userChoice = int(userChoice)

    if secret == userChoice:
        print('Сундук с сокровищами. Теперь вы богаты!')
    else:
        print('Глаза огромного дракона! К сожалению, вы проиграли...')
    
    playAgain = input('Хотите сыграть еще? (y/n) ')
    if playAgain.lower().startswith('n'):
        gameOn = False
    