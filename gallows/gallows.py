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

secret = 'карандаш'
correct = ['а', 'н']
incorrect = ['п', 'ф', 'я']

printFrame()
