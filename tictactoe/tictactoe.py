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
       board[4] == tile and board[5] == tile and board[6] == tile or \
       board[7] == tile and board[8] == tile and board[9] == tile or \
       board[1] == tile and board[4] == tile and board[7] == tile or \
       board[2] == tile and board[5] == tile and board[8] == tile or \
       board[3] == tile and board[6] == tile and board[9] == tile or \
       board[1] == tile and board[5] == tile and board[9] == tile or \
       board[7] == tile and board[5] == tile and board[3] == tile:
       return True
    else:
        return False

def checkDraw(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    if checkVictory(board, userTile) or checkVictory(board, computerTile):
        return False
    return True

def getBoardCopy(boad):
    res = []
    for i in board:
        res.append(i)
    return res

def getComputerMove(board):
    valid_moves = []
    for i in range(1, 10):
        if board[i] == ' ':
            valid_moves.append(i)
    # пытаемся сделать выигрывающий ход
    for i in valid_moves:
        bc = getBoardCopy(board)
        makeMove(bc, i, computerTile)
        if checkVictory(bc, computerTile):
            return i
    # пытаемся сделать блокирующий ход
    for i in valid_moves:
        bc = getBoardCopy(board)
        makeMove(bc, i, userTile)
        if checkVictory(bc, userTile):
            return i
    if 5 in valid_moves:
        return 5
    corners = []
    for i in [1, 3, 7, 9]:
        if i in valid_moves:
            corners.append(i)
    if corners:
        return random.choice(corners)
    return random.choice(valid_moves)


def makeMove(board, move, tile):
    board[move] = tile

board = [' '] * 10
printBoard()

print('К Р Е С Т И К И - Н О Л И К И')
userTile, computerTile = selectUserTile()
turn = random.choice(['user', 'computer'])
if turn == 'user':
    print('Первым ходите вы')
else:
    print('Первым ходит компьютер')

gameOn = True
while gameOn:
    printBoard()
    if turn == 'user':
        userMove = getUserMove(board)
        makeMove(board, userMove, userTile)
        if checkVictory(board, userTile):
            print('Поздравляем! Вы победили!')
            gameOn = False
        turn = 'computer'
    else:
        print('Ход компьютера:')
        computerMove = getComputerMove(board)
        makeMove(board, computerMove, computerTile)
        if checkVictory(board, computerTile):
            print('Победил компьютер')
            gameOn = False
        turn = 'user'
    if checkDraw(board):
        print('Ничья!')
        gameOn = False
printBoard()