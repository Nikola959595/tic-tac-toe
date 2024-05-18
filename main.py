print("Welcome to Tic Tac Toe")

board = []
for i in range(9):
    board.append(" ")

def print_board():
    for i in range(0, len(board), 3):
        print("|", board[i], "|", board[i + 1], "|", board[i + 2])
        print("__________")    


print_board()