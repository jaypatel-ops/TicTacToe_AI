import random
from math import inf


def draw_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def user_input_letter():
    print("Choose X or O")
    player_letter = ''
    player_letter = input("Player -> ").upper()

    if player_letter == 'X':
        return ['X', 'O']
    elif player_letter == 'O':
        return ['O', 'X']


def coin_toss():
    num = random.randrange(2)
    if num == 1:
        return "AI"
    else:
        return "Player"


def ai_move(board, ai_symbol):
    best_score = -inf
    best_move = -inf
    for i in range(10):
        if board[i] == ' ':
            board[i] = ai_symbol
            score_var = minimax(board, 0, False)
            board[i] = ' '
            if score_var > best_score:
                best_score = score_var
                best_move = i

    print("AI -> " + str(best_move))
    board[int(best_move)] = ai
    draw_board(board)


def minimax(board, depth, maximizing):
    # result = -inf
    result = check_score(board, player, ai)
    if result is not None:
        return result

    if maximizing:
        best_score = -inf
        for i in range(10):
            if board[i] == ' ':
                board[i] = ai
                score_l = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score_l, best_score)
        return best_score
    else:
        best_score = inf
        for i in range(10):
            if board[i] == ' ':
                board[i] = player
                score_l = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score_l, best_score)
        return best_score


def player_move(board, player_symbol):
    player_chose = int(input("Player -> "))

    if board[player_chose] == ' ':
        board[player_chose] = player_symbol
    else:
        print("Invalid Input")
        player_move(board, player_symbol)

    draw_board(board)


def diagonal_crossed(board, symbol):
    if board[1] == board[5] == board[9] == symbol:
        return True
    elif board[3] == board[5] == board[7] == symbol:
        return True
    else:
        return False


def row_crossed(board, symbol):
    if board[1] == board[2] == board[3] == symbol:
        return True
    elif board[4] == board[5] == board[6] == symbol:
        return True
    elif board[7] == board[8] == board[9] == symbol:
        return True
    else:
        return False


def column_crossed(board, symbol):
    if board[1] == board[4] == board[7] == symbol:
        return True
    elif board[2] == board[5] == board[8] == symbol:
        return True
    elif board[3] == board[6] == board[9] == symbol:
        return True
    else:
        return False


def check_score(board, player_, ai_):
    # Players wins -> -1, AI wins -> 1, Tie -> 0
    if row_crossed(board, player_) or column_crossed(board, player_) or diagonal_crossed(board, player_):
        return -1
    elif row_crossed(board, ai_) or column_crossed(board, ai_) or diagonal_crossed(board, ai_):
        return 1
    elif board_full(board):
        return 0
    else:
        return None


def play_again(user_input):
    if user_input.upper() == "Y":
        return True
    else:
        return False


def board_full(board):
    for x in board:
        if x == ' ':
            return False
    return True


# main game loop
while True:
    the_board = ['-']  # this index 0 of the board array, we are not using it.
    the_board.extend([' '] * 9)
    score = -inf
    print("Welcome to TIC TAC TOE")
    player, ai = user_input_letter()
    print("the AI -> " + ai)
    draw_board(the_board)
    turn = coin_toss()
    game_over = False

    while not game_over:

        if turn == "Player":
            print("Player's turn")
            player_move(the_board, player)

            # IF PLAYER WON
            if check_score(the_board, player, ai) == -1:
                game_over = True
                score = -1
                print("Player won the Game")
                print("Score-> " + str(score))
                inp = input("\nWant to play again? Press Y for Yes, N for No\n ")
                if play_again(inp):
                    continue
                else:
                    exit(1)

            elif check_score(the_board, player, ai) == 0:
                score = 0
                game_over = True
                print("This game is a TIE!")
                print("Score-> " + str(score))
                inp = input("\nWant to play again? Press Y for Yes, N for No\n ")
                if play_again(inp):
                    continue
                else:
                    exit(1)
            else:
                turn = "AI"

        elif turn == "AI":
            print("AI's turn")
            ai_move(the_board, ai)

            # IF AI WON
            if check_score(the_board, player, ai) == 1:
                game_over = True
                score = 1
                print("AI won the game")
                print("Score-> " + str(score))
                inp = input("\nWant to play again? Press Y for Yes, N for No\n ")
                if play_again(inp):
                    continue
                else:
                    exit(1)

            elif check_score(the_board, player, ai) == 0:
                score = 0
                game_over = True
                print("This game is a TIE!")
                print("Score-> " + str(score))
                inp = input("\nWant to play again? Press Y for Yes, N for No\n ")
                if play_again(inp):
                    continue
                else:
                    exit(1)
            else:
                turn = "Player"
        else:
            print("OOPS! There's a problem!")
