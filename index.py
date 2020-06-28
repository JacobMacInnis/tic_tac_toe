from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9]+' ')
    print('---|---|---')
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6]+' ')
    print('---|---|---')
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3]+' ')

def player_input():
    
    marker = False
    while marker not in ['X', 'x', 'O', 'o']:
        marker = input("Please pick a marker ('X' or 'O'): ")
        
        if marker not in ['X', 'x', 'O', 'o']:
            print('you selected an invalid character')
        
        if marker in ['x', 'o']:
            marker = marker.upper()
    
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, mark):
    winning_places = [
        [1,2,3], 
        [4,5,6], 
        [7,8,9], 
        [1,4,7],
        [2,5,8],
        [3,6,9],
        [1,5,9],
        [3,5,7]
    ]
    winning_row = False
    for array in winning_places:
        if board[array[0]] == mark and board[array[1]] == mark and board[array[2]] == mark:
            return True
        else:
            pass
    return False

def choose_first():
    return f'player {random.randint(1, 2)}'

def space_check(board, position):
    return board[position] == ' '
    
def full_board_check(board):
    for space in board:
        if space != ' ':
            return False
    return True

def player_choice(board, player):
    position = False
    while position not in range(1,9):

        position = input(f'{player} Please enter a number: ')
        
        if position.isdigit():
            position = int(position)
        else:
            print('Input was not valid digit within (1-9)')
        
        if position not in range(1,9):
            print('input was not within (1-9)')
        
        if space_check(board, position):
            return position
        else:
            print('position is aready filled')

def replay():
    ans = 'awaiting'
    while ans not in ['Y', 'y', 'N', 'n']:
        ans = input('Do you want to play again? ')
        
        if ans not in ['Y', 'y', 'N', 'n']:
            print('not a valid answer, please enter (Y or N)')
        
        elif ans in ['Y', 'y']:
            return True
        elif ans in ['N', 'n']:
            return False

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the Board
    theBoard = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f'Player 1 is {player1_marker}, Player 2 is {player2_marker}')
    print(turn + ' will go first')
    
    play_game = input(f'{turn} Are you ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            print('\n'*100)
            display_board(theBoard)
            player = 'player 1'
            position = player_choice(theBoard, player)
            place_marker(theBoard, player1_marker, position)
            
            if win_check(theBoard, player1_marker):
                print('\n'*100)
                display_board(theBoard)
                print(f'Congrations! Player 1: {player1_marker} Wins!')
                game_on = False
                break
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            #Player2's turn.
            print('\n'*100)
            display_board(theBoard)
            player = 'player 2'
            position = player_choice(theBoard, player)
            place_marker(theBoard, player2_marker, position)
            
            if win_check(theBoard, player2_marker):
                print('\n'*100)
                display_board(theBoard)
                print(f'Congrations! Player 2: {player2_marker} Wins!')
                game_on - False
                break
            else: 
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
