import random
import time
print("Welcome to Tic Tac Toe!")

difficulty_choice = ""
while True:
    difficulty_choice = str(input("Difficulty: Easy or Impossible?")).lower()
    if difficulty_choice == "easy" or difficulty_choice == "impossible":
        break
    else:
        print("Please provid valid input.")

board = [" " for _ in range(9)]
choices = [i for i in range(9)]

def print_board():
    for i in range(0, len(board), 3):
        print(board[i], "|", board[i + 1], "|", board[i + 2])
        if i <= 3:
            print("_________")    


print_board()


player_symbol = "X"
computer_symbol = "O"

    

def random_computer():
    computer_choice = random.choice(choices)
    board[computer_choice] = computer_symbol    
    choices.remove(computer_choice)


def minimax(board, depth, is_maximizing):
    if check_win(computer_symbol):
        return 1
    if check_win(player_symbol):
        return -1
    if check_tie():
        return 0
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = computer_symbol
                score = minimax(board, depth + 1, False)
                board[i] =" "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = player_symbol
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score        

def impossible_computer():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = computer_symbol
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move            

def check_win(player):
    for i in range(0, len(board), 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i +3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

def check_tie():
    return all(space !=" " for space in board)        

while True:
    while True:
        try:
            user_input = int(input("Please type your move (1-9)\n")) - 1
            if user_input in choices and board[user_input] == " ":  
                board[user_input] = player_symbol
                choices.remove(user_input) 
                break
            else:
                print("Please provid a valid input!")
        except ValueError:
            print("Please Provide a valid input")                    
    if check_win(player_symbol):
        print("You win!")
        break
    if check_tie():
        print("It's a tie.")
        break
    time.sleep(1)
    if difficulty_choice == 'easy':
        random_computer()
    else:
        computer_choice = impossible_computer()
        board[computer_choice] = computer_symbol
        choices.remove(computer_choice)    
    print_board()
    if check_win(computer_symbol):
        print("The computer wins!")
        break
    if check_tie():
        print("It's a tie")
        break
    