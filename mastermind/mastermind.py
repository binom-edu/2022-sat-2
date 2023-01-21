import random

NUM_DIGITS = 3
MAX_ATTEMPTS = 20

def generateSecret():
    alf = '0 1 2 3 4 5 6 7 8 9'.split()
    random.shuffle(alf)
    return alf[:NUM_DIGITS]

def getUserMove():
    while True:
        s = input('Ваш ход: ')
        if len(s) != NUM_DIGITS:
            print(f'Принимаются только {NUM_DIGITS}-значные числа')
            continue
        if not s.isdigit():
            print('Введенная строка содержит недопустимые символы')
            continue
        return s

def checkAttempt(attempt):
    ans = {
        'bulls': 0,
        'cows': 0
    }
    for i in range(NUM_DIGITS):
        if attempt[i] == secret[i]:
            ans['bulls'] += 1
        elif attempt[i] in secret:
            ans['cows'] += 1
    return ans

def intro():
    print(f'Компьютер загадал число из {NUM_DIGITS} цифр. Попробуйте отгадать его. У вас будет {MAX_ATTEMPTS} попыток. После каждой попытки вы будете получать ответ: быки - количество цифр в вашей попытке, которые стоят на тех же позициях, что в загаданном числе, коровы - количество цифр, которые есть в загаданном числе, но на других позициях.')

intro()
secret = generateSecret()
for i in range(MAX_ATTEMPTS):
    print('Попытка номер', i + 1)
    attempt = getUserMove()
    res = checkAttempt(attempt=attempt)
    print(f'Быки: {res["bulls"]}, коровы: {res["cows"]}.')
    if res['bulls'] == NUM_DIGITS:
        print('Вы победили!')
        break
else:
    print('Ваши попытки исчерпаны')
