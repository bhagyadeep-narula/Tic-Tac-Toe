                                          #TIC TAC TOE GAME#

import random

def display_board(board):

    print("\n"*12)
    print(board[1]+" | "+board[2]+" | "+board[3])
    print("----------")
    print(board[4]+" | "+board[5]+" | "+board[6])
    print("----------")
    print(board[7]+" | "+board[8]+" | "+board[9])
    print("\n"*14)


def player_input():

    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Player1: Choose X or O: ").upper()

    if marker == "X":
        return "X", "O"
    else:
        return "O", "X"

def place_marker(board, marker, position_):

    board[position_] = marker

def win_check(board, mark):

    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return "Player 2"
    else:
        return "Player 1"


def space_check(board, position_):

    return board[position_] == " "

def full_board_check(board):

    return " " not in board[1:10]

def player_choice(board):

    position_ = 0

    while position_ not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position_):

        position_ = int(input("Enter the position: (1-9)"))

    return position_

def replay():

    replay_choice = input("Do You Want To Play Again? YES or NO: ")

    return replay_choice == "yes"

print("WELCOME TO TIC TAC TOE ")


while True:

    the_board = [" "]*10
    player1_marker , player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? YES or NO: ")

    if play_game == "yes":
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == "Player 1":
            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON !!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME !!")
                    game_on =False
                else:
                    turn = "Player 2"
        else:

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player2_marker,  position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON !!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME !!")
                    game_on =False
                else:
                    turn = "Player 1"

    if not replay():
        break
