#imports
import random

#Builds a basic user interface in the command line
def display_board(board):
    print(' ',board[1],' | ',board[2],' | ',board[3])
    print('-----|-----|-----')
    print(' ',board[4],' | ',board[5],' | ',board[6])
    print('-----|-----|-----')
    print(' ',board[7],' | ',board[8],' | ',board[9])

def player_input():
    #First player chooses their token for the game. 
    choice = False
    while choice == False:
        player1 = input('Player 1 please choose your piece, X or O: ')
        if player1 == 'X':
            choice = True
            return player1
        elif player1 == 'O':
            choice = True
            return player1
        else:
            print('Not a valid choice, Please choose X or O: ')

def place_marker(board, marker, position):
    game_update = board
    game_update[position] = marker
    return game_update

def win_check(board, marker):
    
    win_cond = {'one':[1,2,3],'two':[4,5,6],'three':[7,8,9],'four':[1,4,7],'five':[2,5,8],'six':[3,6,9],'seven':[1,5,9],'eight':[3,5,7]}
    
    if marker == 'X':
        if [board[win_cond['one'][0]],board[win_cond['one'][1]],board[win_cond['one'][2]]] == ['X','X','X']:
            print('X wins!! Condition 1')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['two'][0]],board[win_cond['two'][1]],board[win_cond['two'][2]]] == ['X','X','X']:
            print('X wins!! Condition 2')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['three'][0]],board[win_cond['three'][1]],board[win_cond['three'][2]]] == ['X','X','X']:
            print('X wins!! Condition 3')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['four'][0]],board[win_cond['four'][1]],board[win_cond['four'][2]]] == ['X','X','X']:
            print('X wins!! Condition 4')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['five'][0]],board[win_cond['five'][1]],board[win_cond['five'][2]]] == ['X','X','X']:
            print('X wins!! Condition 5')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['six'][0]],board[win_cond['six'][1]],board[win_cond['six'][2]]] == ['X','X','X']:
            print('X wins!! Condition 6')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['seven'][0]],board[win_cond['seven'][1]],board[win_cond['seven'][2]]] == ['X','X','X']:
            print('X wins!! Condition 7')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['eight'][0]],board[win_cond['eight'][1]],board[win_cond['eight'][2]]] == ['X','X','X']:
            print('X wins!! Condition 8')
            replaying = replay()
            return continue_replay(replaying)
        else:
            return 'not yet', 'not, yet'
        
    elif marker == 'O':
        if [board[win_cond['one'][0]],board[win_cond['one'][1]],board[win_cond['one'][2]]] == ['O','O','O']:
            print('O wins!! Condition 1')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['two'][0]],board[win_cond['two'][1]],board[win_cond['two'][2]]] == ['O','O','O']:
            print('O wins!! Condition 2')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['three'][0]],board[win_cond['three'][1]],board[win_cond['three'][2]]] == ['O','O','O']:
            print('O wins!! Condition 3')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['four'][0]],board[win_cond['four'][1]],board[win_cond['four'][2]]] == ['O','O','O']:
            print('O wins!! Condition 4')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['five'][0]],board[win_cond['five'][1]],board[win_cond['five'][2]]] == ['O','O','O']:
            print('O wins!! Condition 5')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['six'][0]],board[win_cond['six'][1]],board[win_cond['six'][2]]] == ['O','O','O']:
            print('O wins!! Condition 6')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['seven'][0]],board[win_cond['seven'][1]],board[win_cond['seven'][2]]] == ['O','O','O']:
            print('O wins!! Condition 7')
            replaying = replay()
            return continue_replay(replaying)
        elif [board[win_cond['eight'][0]],board[win_cond['eight'][1]],board[win_cond['eight'][2]]] == ['O','O','O']:
            print('O wins!! Condition 8')
            replaying = replay()
            return continue_replay(replaying)
        else:
            return 'not yet', 'not, yet'

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
        print("Board is full!")
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
            if space_check(board,position):
                check = True
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

def switch_sides(player1,player2):
    if player1 == 'X':
        player1 = 'O'
        player2 = 'X'
        print(f"Player 1 is now {player1}")
    elif player1 == 'O':
        player1 = 'X'
        player2 = 'O'
        print(f"Player 1 is now {player1}")
    return player1,player2

def continue_replay(replayed):
    reset_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    if not replayed:
        thanks = 'Thank you for playing!'
        return False, thanks
    else: 
        board = reset_board
        return True, board
        
####################################
#function calls#
####################################
    
print('Welcome to Tic Tac Toe!')

game_on = True
while game_on == True:
        
        #Initial Board
        board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        turn = 0
        display_board(board)
    
        player1 = player_input() # X or O
        
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

        (play1,play2) = choose_first() # comes back as (1, 2) or (2, 1)
        
        # the game instance when Player1 is the first move
        while play1 == 1 and game_on == True:
                             
            if turn % 2 == 0:
                
                marker = player1
                turn += 1

                position = player_choice(board)

                place_marker(board, marker, position)

                space_check(board, position)
                
                display_board(board)
                
                next_game, newboard = win_check(board, marker)
                full = full_board_check(board)
                if full and next_game == 'not yet':
                    replaying = replay()
                    next_game, newboard = continue_replay(replaying)

                if next_game == True:
                    board = newboard
                    display_board(board)
                    player1, player2 = switch_sides(player1,player2)
                elif next_game == False:
                    print('End of Game')
                    #prints thank you for playing
                    print(newboard)
                    game_on = False
                    break
                    
            if turn % 2 != 0:
                
                marker = player2
                turn += 1

                position = player_choice(board)

                place_marker(board, marker, position)

                space_check(board, position)
                
                display_board(board)
                                
                next_game, newboard = win_check(board, marker)
                full = full_board_check(board)
                if full and next_game == 'not yet':
                    replaying = replay()
                    next_game, newboard = continue_replay(replaying)

                if next_game == True:
                    board = newboard
                    display_board(board)
                    player1, player2 = switch_sides(player1,player2)
                elif next_game == False:
                    print('End of Game')
                    print(newboard)
                    game_on = False
                    break            

        # the game instance when Player2 is the first move
        while play2 == 1 and game_on == True:         

            if turn % 2 == 0: 
                
                marker = player2
                turn += 1

                position = player_choice(board)

                place_marker(board, marker, position)

                space_check(board, position)
                
                display_board(board)
                                
                next_game, newboard = win_check(board, marker)
                full = full_board_check(board)
                if full and next_game == 'not yet':
                    replaying = replay()
                    next_game, newboard = continue_replay(replaying)

                if next_game == True:
                    board = newboard
                    display_board(board)
                    player1, player2 = switch_sides(player1,player2)
                elif next_game == False:
                    print('End of Game')
                    print(newboard)
                    game_on = False
                    break

            if turn % 2 != 0:
                
                marker = player1
                turn += 1

                position = player_choice(board)

                place_marker(board, marker, position)

                space_check(board, position)
                
                display_board(board)

                next_game, newboard = win_check(board, marker)
                full = full_board_check(board)
                if full and next_game == 'not yet':
                    replaying = replay()
                    next_game, newboard = continue_replay(replaying)

                if next_game == True:
                    board = newboard
                    display_board(board)
                    player1, player2 = switch_sides(player1,player2)
                elif next_game == False:
                    print('End of Game')
                    print(newboard)
                    game_on = False
                    break