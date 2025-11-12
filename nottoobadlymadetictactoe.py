import random

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def list_free_fields(board):

    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', '0']:
                free_fields.append((r, c))
    return free_fields

def enter_move(board):
    while True:
        try:
            move = int(input("Hamle gir(1-9):"))
            if not (1 <= move <= 9):
                print("Yanlış hamle")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
 
            if board[row][col] not in ['X', '0']:
                board[row][col] = '0' 
                break 
            else:
                print("Bu kare dolu.")
        
        except ValueError:
            print("bir sayı girin.")

def victory_for(board, sign):

    for r in range(3):
        if board[r][0] == sign and board[r][1] == sign and board[r][2] == sign:
            return True

    for c in range(3):
        if board[0][c] == sign and board[1][c] == sign and board[2][c] == sign:
            return True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False

def draw_move(board):

    free_fields = list_free_fields(board)

    index = random.randrange(len(free_fields))

    row, col = free_fields[index]

    board[row][col] = 'X'
#OYUN
board = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

print("TicTacToe Oyunu")

board[1][1] = 'X'
print("('X')merkezden başladı")
display_board(board)

while True:

    enter_move(board)
    display_board(board)

    if victory_for(board, '0'):
        print("Aferin kazandın")
        break 

    if len(list_free_fields(board)) == 0:
        print("berabere")
        break

    print("Bilgisayarın sırası")
    draw_move(board)
    display_board(board)

    if victory_for(board, 'X'):
        print("bilgisayara kaybettin")
        break 

    if len(list_free_fields(board)) == 0:
        print("berabere")
        break 

print("Oyun bitti")
