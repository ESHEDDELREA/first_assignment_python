import random


def display_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def player_input():
    mark1 = input("first player mark will be 'X' or 'O'? \n")
    while mark1 != 'X' and mark1 != 'O':
        mark1 = input("first player mark will be 'X' or 'O'? \n")
    if mark1 == 'X':
        mark2 = 'O'
    else:
        mark2 = 'X'
    return mark1, mark2


def place_marker(board, marker, position1):
    board[position] = marker


def win_check(board, mark):
    # if one of this condition happen the function return True

    return (board[1] == mark and board[2] == mark and board[3] == mark) or \
           (board[4] == mark and board[5] == mark and board[6] == mark) or \
           (board[7] == mark and board[8] == mark and board[9] == mark) or \
           (board[1] == mark and board[4] == mark and board[7] == mark) or \
           (board[2] == mark and board[5] == mark and board[8] == mark) or \
           (board[3] == mark and board[6] == mark and board[9] == mark) or \
           (board[1] == mark and board[5] == mark and board[9] == mark) or \
           (board[3] == mark and board[5] == mark and board[7] == mark)


def choose_first():
    lottery = random.randint(1, 2)
    if lottery == 1:
        return "first to play is player 1\n"
    else:
        return "first to play is player 2\n"


def space_check(board, position):
    if board[position] == ' ':
        return True  # THE POSITION IS EMPTY
    else:
        return False  # THE POSITION IS FULL


def full_board_check(board):
    for i in range(len(board)):
        if space_check(board, i):
            return False  # THE BOARD IS NOT FULL
    else:
        return True  # THE BOARD IS FULL


def player_choice(board):
    position = int(input("what is your next position(1-9) \n "))
    while not space_check(board, position):
        position = int(input("what is your next position(1-9) \n "))
    return position  # THE POSITION IS EMPTY AND READY FOR USE


def replay():
    return input("do you want to play again?\n").upper().startswith('Y')


while True:

    board_list = ['@', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print(choose_first())  # set the game up here
    marks = player_input()
    print(marks[0])

    while not full_board_check(board_list) and not win_check(board_list, 'X') or not win_check(board_list, 'O'):
        display_board(board_list)
        position = player_choice(board_list)
        place_marker(board_list, marks[0], position)
        space_check(board_list, position)
        if full_board_check(board_list) and not win_check(board_list, marks[0]):
            display_board(board_list)
            break
        if win_check(board_list, marks[0]):
            display_board(board_list)
            print("player 1 has won")
            break
        # PLAYER 1
        display_board(board_list)
        position = player_choice(board_list)
        place_marker(board_list, marks[1], position)
        space_check(board_list, position)
        if full_board_check(board_list) and not win_check(board_list, marks[1]):
            display_board(board_list)
            break
        if win_check(board_list, marks[1]):
            print("player 2 is won")
            display_board(board_list)
            break

    if not replay():
        break
    else:
        print('\n' * 100)
