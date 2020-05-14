import random
from math import inf


# import infinity as infinity


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
    for i in range(1, 10):
        if board[i] == ' ':
            print("AI -> " + str(i))
            board[i] = ai_symbol;
            break
    draw_board(board)


def player_move(board, player_symbol):
    player_chose = int(input("Player -> "))
    # print("Player -> " + str(player_chose))
    # print(type(player_chose))

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


def won(board, symbol):
    if row_crossed(board, symbol) or column_crossed(board, symbol) or diagonal_crossed(board, symbol):
        return True
    else:
        return False


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
    the_board = ['-']
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

            if won(the_board, player):
                game_over = True
                score = 1
                print("Player won the Game")
                print("Score-> " + str(score))
                inp = input("\nWant to play again? Press Y for Yes, N for No\n ")
                if play_again(inp):
                    continue
                else:
                    exit(1)
            elif board_full(the_board):
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

            if won(the_board, ai):
                game_over = True
                score = -1
                print("AI won the game")
                print("Score-> " + str(score))
                inp = input("\nWant to play again? Press Y for Yes, N for No\n ")
                if play_again(inp):
                    continue
                else:
                    exit(1)
            elif board_full(the_board):
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
            print("There's some problem!")
