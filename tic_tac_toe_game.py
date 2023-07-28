# from IPython.display import clear_output

def display_board(board):
    print(' ',board[1],' | ',board[2],' | ',board[3])
    print('-----|-----|-----')
    print(' ',board[4],' | ',board[5],' | ',board[6])
    print('-----|-----|-----')
    print(' ',board[7],' | ',board[8],' | ',board[9])

# players = []
def player_input():
    
    choice = False
    
    while choice == False:
        player1 = input('Player 1 please choose your piece, X or O: ')

        if player1 == 'X':
            player2 = 'O'
            choice = True
            return player1
#             players.append(player1)
#             players.append(player2)
        elif player1 == 'O':
            player2 = 'X'
            choice = True
            return player1
#             players.append(player1)
#             players.append(player2)
        else:
            print('Not a valid choice, Please choose X or O: ')
#     return players
#     print(player1)
#     print(player2)

def place_marker(board, marker, position):
    game_update = board
    game_update[position] = marker
    return game_update

# win_cond = {one:[1,2,3],two:[4,5,6],three:[7,8,9],four:[1,4,7],five:[2,5,8],six:[3,6,9],seven:[1,5,9],eight:[3,5,7]}

def win_check(board, marker):
    
    win_cond = {'one':[1,2,3],'two':[4,5,6],'three':[7,8,9],'four':[1,4,7],'five':[2,5,8],'six':[3,6,9],'seven':[1,5,9],'eight':[3,5,7]}
    reset_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    
    if marker == 'X':
        if [board[win_cond['one'][0]],board[win_cond['one'][1]],board[win_cond['one'][2]]] == ['X','X','X']:
            print('X wins!!1')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['two'][0]],board[win_cond['two'][1]],board[win_cond['two'][2]]] == ['X','X','X']:
            print('X wins!!2')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['three'][0]],board[win_cond['three'][1]],board[win_cond['three'][2]]] == ['X','X','X']:
            print('X wins!!3')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['four'][0]],board[win_cond['four'][1]],board[win_cond['four'][2]]] == ['X','X','X']:
            print('X wins!!4')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['five'][0]],board[win_cond['five'][1]],board[win_cond['five'][2]]] == ['X','X','X']:
            print('X wins!!5')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['six'][0]],board[win_cond['six'][1]],board[win_cond['six'][2]]] == ['X','X','X']:
            print('X wins!!6')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['seven'][0]],board[win_cond['seven'][1]],board[win_cond['seven'][2]]] == ['X','X','X']:
            print('X wins!!7')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['eight'][0]],board[win_cond['eight'][1]],board[win_cond['eight'][2]]] == ['X','X','X']:
            print('X wins!!8')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        else:
            return 'not yet', 'not, yet'
        
    if marker == 'O':
        if [board[win_cond['one'][0]],board[win_cond['one'][1]],board[win_cond['one'][2]]] == ['O','O','O']:
            print('O wins!!1')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['two'][0]],board[win_cond['two'][1]],board[win_cond['two'][2]]] == ['O','O','O']:
            print('O wins!!2')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['three'][0]],board[win_cond['three'][1]],board[win_cond['three'][2]]] == ['O','O','O']:
            print('O wins!!3')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['four'][0]],board[win_cond['four'][1]],board[win_cond['four'][2]]] == ['O','O','O']:
            print('O wins!!4')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['five'][0]],board[win_cond['five'][1]],board[win_cond['five'][2]]] == ['O','O','O']:
            print('O wins!!5')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['six'][0]],board[win_cond['six'][1]],board[win_cond['six'][2]]] == ['O','O','O']:
            print('O wins!!6')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['seven'][0]],board[win_cond['seven'][1]],board[win_cond['seven'][2]]] == ['O','O','O']:
            print('O wins!!7')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        elif [board[win_cond['eight'][0]],board[win_cond['eight'][1]],board[win_cond['eight'][2]]] == ['O','O','O']:
            print('O wins!!8')
            if not replay():
                game_on = False
                thanks = 'Thank you for playing!'
                return game_on, thanks
            else: 
                board = reset_board
                return True, board
        else:
            return 'not yet', 'not, yet'

import random

def choose_first():
    num = random.randint(1,101)
    if num % 2 == 0:
        play1 = 1
        play2 = 2
        print("Player 1 goes first!")
        return play1, play2
    else:
        play1 = 2
        play2 = 1
        print("Player 2 goes first!")
        return play1, play2
        
def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True

def full_board_check(board):
    if ' ' not in board:
        #board full
        print("Board is full! Try again!")
        return True
    else:
        return False

def player_choice(board):
    check = False
    while check == False:
        pos = input('Choose your next move (1-9): ')
        position = 100
        if pos in ['1','2','3','4','5','6','7','8','9']:
            position = int(pos)
#         elif position in range(1,10):
            if space_check(board,position):
                check = True
#                 print('returnedddddddddddddddddddd')
                return position
            else:
                print('This position is taken, please choose another position ')
                continue
        else:
            print('Invalid choice, please choose a position in the range of 1 and 9 ')
            continue

def replay():
    play = False
    while play == False:
        playagain = input('Would you like to play again? (Y / N): ')
        if playagain == 'Y' or playagain == 'N':
            if playagain == 'Y':
                play = True
                print('Now switch who goes first!')
                return True
            else:
                play = True
                return False
        else:
            print('Incorrect input, use only Y or N ')
            continue
    
####################################
#function calls#
####################################
    
    
print('Welcome to Tic Tac Toe!')

# from IPython.display import clear_output

game_on = True

while game_on == True: 
    
#     game_on = True

    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    while game_on == True:
        
#         clear_output
        
        turn = 0
        
#         newboard = 1
#         next_game = 1
        
        display_board(board)
    
        player1 = player_input() # X or O
#         print(player1)
        
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

        (play1,play2) = choose_first() # comes back as (1, 2) or (2, 1)
        
#         print(player1)
#         print(player2)
#         print(play1)
#         print(play2)
        
        while play1 == 1 and game_on == True:
            
#             clear_output

#             print(turn)                 
            if turn % 2 == 0:
                
                marker = player1
                turn += 1

                position = player_choice(board)

                place_marker(board, marker, position)

                space_check(board, position)
                
                display_board(board)
                
#                 print('Loop 1')
#                 print(f'next_game: {next_game}')
#                 print(f'newboard: {newboard}') 
                
                (next_game, newboard) = win_check(board, marker)

                
                if next_game == True:
#                     print("1111")
                    board = newboard
                elif next_game == False:
                    print(newboard)
                    game_on = next_game
                
                full_board_check(board)
                
                
#                 if not replay():
#                     game_on = False
#                     break
                    
            if turn % 2 != 0:
                
                marker = player2
                turn += 1

                position = player_choice(board)

                place_marker(board, marker, position)

                space_check(board, position)
                
                display_board(board)
                
#                 print('Loop 2')
#                 print(f'next_game: {next_game}')
#                 print(f'newboard: {newboard}')
                
                (next_game, newboard) = win_check(board, marker)
                
                if next_game == True:
#                     print("2222")
                    board = newboard
                elif next_game == False:
                    print(newboard)
                    game_on = next_game
                
                full_board_check(board)
            
            else:
                continue

#                 if not replay():
#                     game_on = False
#                     break
                    
        while play2 == 1 and game_on == True:
            
#             clear_output
                
#             print(turn)

            if turn % 2 == 0: 
                
                marker = player2
                turn += 1

                position = player_choice(board)

                place_marker(board, marker, position)

                space_check(board, position)
                
                display_board(board)
                
#                 print('Loop 3')
#                 print(f'next_game: {next_game}')
#                 print(f'newboard: {newboard}')
                
                (next_game, newboard) = win_check(board, marker)
                
                if next_game == True:
#                     print("3333")
                    board = newboard
                elif next_game == False:
                    print(newboard)
                    game_on = next_game
                
                full_board_check(board)

#                 if not replay():
#                     game_on = False
#                     break
                    
            if turn % 2 != 0:
                
                marker = player1
                turn += 1

                position = player_choice(board)

                place_marker(board, marker, position)

                space_check(board, position)
                
                display_board(board)
                
#                 print('Loop 4')
#                 print(f'next_game: {next_game}')
#                 print(f'newboard: {newboard}')
                
                (next_game, newboard) = win_check(board, marker)
                
                if next_game == True:
#                     print("4444")
                    board = newboard
                elif next_game == False:
                    print(newboard)
                    game_on = next_game
                
                full_board_check(board)
                
            else:
                continue

#                 if not replay():
#                     game_on = False
#                     break


#     break       
# break 
    