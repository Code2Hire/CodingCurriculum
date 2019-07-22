

from IPython.display import clear_output

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])



def player_input(): 
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Please choose X or O: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[1] == mark and board[2] == mark and board[3] == mark) or (board[7] == mark and board[4] == mark and board[1] == mark) or (board[8] == mark and board[5] == mark and board[2] == mark) or (board[9] == mark and board[6] == mark and board[3] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark) or (board[9] == mark and board[5] == mark and board[1] == mark))



import random

def choose_first():
    rand = random.randint(0,1)
    if rand == 0:
        return '1'
    else:
        return '2'

def space_check(board, position):
    return (board[position] == ' ')


def full_board_check(board):
    for space in range(1,10):
        if space_check(board, space):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose a space 1-9: '))
    return position


def replay():
    choice = input('Do you want to play again? Please enter Yes or No: ')
    if choice == 'Yes':
        return True
    else:
        return False
    


print('Welcome to Tic Tac Toe!')

while True:
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    marker = player_input()
    turn = choose_first()
    print('Player ' + turn + ' goes first')
    display_board(board)
    game_on = True
    while game_on:
        if turn == '1':
            place_marker(board, marker[0], player_choice(board))
            display_board(board)
            if win_check(board, marker[0]):
                print('Player 1 wins')
                game_on = False
                break
            elif full_board_check(board):
                print('Tie')
                game_on = False
                break
            turn = '2'
        if turn == '2':  
            place_marker(board, marker[1], player_choice(board))
            display_board(board)
            if win_check(board, marker[1]):
                print('Player 2 wins')
                game_on = False
                break
            elif full_board_check(board):
                print('Tie')
                game_on = False
                break
            turn = '1'
    if not replay():
        break


