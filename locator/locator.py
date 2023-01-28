import random

WIDTH = 30
HEIGHT = 11
MAX_CHESTS = 3
MAX_ATTEMPTS = 30
EMPTY = '~-*'

def getNewBoard() -> list:
    board = []
    for i in range(HEIGHT):
        buf = []
        for j in range(WIDTH):
            buf.append(random.choice(EMPTY))
        board.append(buf)
    return board

def printBoard(board: list) -> None:
    print('   ', end='')
    for i in range(WIDTH):
        print(i // 10, end='')
    print()
    print('   ', end='')
    for i in range(WIDTH):
        print(i % 10, end='')
    print()
    for i in range(len(board)):
        print("%2d" % i, '|', *board[i], sep='')

def getNewChests() -> list:
    res = []
    while len(res) < MAX_CHESTS:
        chest = (random.randrange(0, HEIGHT), random.randrange(0, WIDTH))
        if not chest in res:
            res.append(chest)
    return res

board = getNewBoard()
chests = getNewChests()
for i, j in chests:
    board[i][j] = '@'
    
printBoard(board)