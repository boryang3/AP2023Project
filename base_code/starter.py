import random

board = [[' '] * 3 for _ in range(3)]


def display_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')
    print()



def make_move(board, row, col, player):
    board[row][col] = player



def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True


    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True



    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False




def check_board_full(board):
    return all(cell != ' ' for row in board for cell in row)



def ai_make_move_easy(board, player):
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    row, col = random.choice(available_moves)
    make_move(board, row, col, player)

def ai_make_move_hard(board, player):
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']

    # Checks if the AI can win in the move
    for row, col in available_moves:
        board[row][col] = player
        if check_win(board, player):
            return


        # Reset the board after checking
        board[row][col] = ' '



    # Prevents two in a row pieces from winning from the player
    opponent_player = 'X' if player == 'O' else 'O'
    for row, col in available_moves:
        board[row][col] = opponent_player
        if check_win(board, opponent_player):
            make_move(board, row, col, player)
            return



        # Reset the board after checking
        board[row][col] = ' '

    # If no winning or blocking moves, computer makes any move
    row, col = random.choice(available_moves)
    make_move(board, row, col, player)



player_choice = input("What character do you want? (X or O): ")
while player_choice not in ['X', 'O']:
    print("You can't choose that You can only choose X or O!")
    player_choice = input("What character do you want? (X or O): ")

difficulty_choice = input("Do you want easy or BO mode? (easy or hard): ")
while difficulty_choice not in ['easy', 'hard']:
    print("You can't choose that. You can only choose easy or hard!")
    difficulty_choice = input("Do you want easy or BO mode? (easy or hard): ")


players = ['user', 'computer']
random.shuffle(players)
current_player = player_choice if players[0] == 'user' else 'X' if player_choice == 'O' else 'O'


probability_of_winning = random.randint(0, 100)
print("The chance you have at winning:", probability_of_winning,"%")



while True:
    display_board(board)

    if current_player == player_choice:
        row = int(input("Row (1, 2, or 3): ")) - 1
        col = int(input("Column (1, 2, or 3): ")) - 1
        make_move(board, row, col, current_player)
    else:
        if difficulty_choice == 'easy':
            ai_make_move_easy(board, current_player)
        else:
            ai_make_move_hard(board, current_player)


    if check_win(board, current_player):
        display_board(board)
        print("Player " + current_player  + " wins!")
        if current_player == player_choice and probability_of_winning > 50:
            print("I was correct about you!")
        elif current_player == player_choice and probability_of_winning <= 50:
            print("I was wrong about you!")
            
        break


    if check_board_full(board):
        display_board(board)
        print("You tied!")
        if current_player == player_choice and probability_of_winning < 50:
            print("I was correct about you!")
        elif current_player == player_choice and probability_of_winning >= 50:
            print("I was wrong about you!")
        break


    current_player = 'O' if current_player == 'X' else 'X'
