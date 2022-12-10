import random

def printFrame():
    out = ''
    for letter in secret:
        if letter in correct:
            out += letter
        else:
            out += '-'
    print('Слово:', out)
    print('Ошибки:', incorrect)
    print(frames[len(incorrect)])

def getUserMove():
    alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    while True:
        s = input('Ваш ход: ').lower()
        if len(s) != 1:
            print('Нужно ввести ровно одну букву')
            continue
        if not s in alf:
            print('Введена не буква')
            continue
        if s in correct or s in incorrect:
            print('Эта буква уже была')
            continue
        return s

def checkVictory():
    for letter in secret:
        if not letter in correct:
            return False
    return True

def checkLose():
    return len(incorrect) == len(frames) - 1

frames = [
'''
---------||
  |      ||
         ||
         ||
         ||
        /||\\
============
''',
'''
---------||
  |      ||
  o      ||
         ||
         ||
        /||\\
============
''',
'''
---------||
  |      ||
  o      ||
  0      ||
         ||
        /||\\
============
''',
'''
---------||
  |      ||
  o      ||
 /0      ||
         ||
        /||\\
============
''',
'''
---------||
  |      ||
  o      ||
 /0\\     ||
         ||
        /||\\
============
''',
'''
---------||
  |      ||
  o      ||
 /0\\     ||
 /       ||
        /||\\
============
''',
'''
---------||
  |      ||
  o      ||
 /0\\     ||
 / \\     ||
        /||\\
============
''',
]

fin = open('words.txt', 'r', encoding='utf8')
words = fin.read().splitlines()
fin.close()

secret = random.choice(words)

print('В И С Е Л И Ц А')
print('Компьютер загадал слово (письменная принадлежность). Попробуйте отгадать его по буквам. У вас будет 6 шансов на ошибку.')

correct = []
incorrect = []

gameOn = True
while gameOn:
    printFrame()
    letter = getUserMove()
    if letter in secret:
        print('Верно!')
        correct.append(letter)
    else:
        print('Такой буквы нет в слове')
        incorrect.append(letter)
    if checkLose():
        print('Вы проиграли. Было загадано слово ', secret)
        printFrame()
        gameOn = False
    if checkVictory():
        print('Поздравляем с победой!')
        printFrame()
        gameOn = False