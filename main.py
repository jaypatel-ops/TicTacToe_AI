import random


def draw_board(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def user_input_letter():
    print("Choose X or O")
    player_letter = ''
    player_letter = input().upper()

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
    player_chose = int(input())
    print("Player -> " + str(player_chose))
    # print(type(player_chose))

    if board[player_chose] == ' ':
        board[player_chose] = player_symbol
    else:
        print("Invalid Input")
        player_move(board, player_symbol)

    draw_board(board)


def diagonal_crossed(board, symbol):
    if board[1] == board[5] == board[9]:
        return True
    elif board[3] == board[5] == board[7]:
        return True
    else:
        return False


# def game_logic():
# if()


# main game loop
while True:
    theBoard = [' '] * 10
    print("Welcome to TIC TAC TOE")
    player, ai = user_input_letter()
    print(player + " -> player")
    print(ai + " -> the AI")
    draw_board(theBoard)
    turn = coin_toss()
    board_full = False

    while not board_full:
        if turn == "Player":
            print("Player's turn")
            player_move(theBoard, player)
            turn = "AI"

        elif turn == "AI":
            print("AI's turn")
            ai_move(theBoard, ai)
            turn = "Player"

        else:
            print("There's some problem!")
