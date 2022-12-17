import random

def printBoard():
    print(board[7], '|', board[8], '|', board[9])
    print('-' * 9)
    print(board[4], '|', board[5], '|', board[6])
    print('-' * 9)
    print(board[1], '|', board[2], '|', board[3])

def getUserMove(board):
    alf = '123456789'
    while True:
        printBoard()
        s = input('Ваш ход (1-9): ')
        if len(s) != 1:
            print('Нужно ввести ровно одну цифру')
            continue
        if not s in alf:
            print('Укажите цифру от 1 до 9')
            continue
        n = int(s)
        if board[n] != ' ':
            print('Клетка уже занята!')
            continue
        return n

def selectUserTile():
    tiles = ['X', 'O']
    random.shuffle(tiles)
    userTile, computerTile = tiles
    print('Вы играете за', userTile)
    ans = input('Поменять выбор (y / n)?')
    if ans.lower().startswith('y'):
        userTile, computerTile = computerTile, userTile
        print('Теперь вы играете за', userTile)
    return [userTile, computerTile]

def checkVictory(board, tile):
    if board[1] == tile and board[2] == tile and board[3] == tile or \
       board[4] == tile and ...

# board = ['', ' ', ' ', ' ', ' ', 'X', ' ', 'O', 'X', 'O']
# printBoard()

print('К Р Е С Т И К И - Н О Л И К И')
userTile, computerTile = selectUserTile()
turn = random.choice(['user', 'computer'])
if turn == 'user':
    print('Первым ходите вы')
else:
    print('Первым ходит компьютер')


userMove = getUserMove(board=board)
board[userMove] = userTile
printBoard()
