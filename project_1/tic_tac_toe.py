#Imported modules
import random
# Global variables
theBoard = [' '] * 10   # a list of empty spaces
available = [str(num) for num in range(0,10)] # a List Comprehension
players = [0,'X','O']   # note that players[1] == 'X' and players[-1] == 'O'

#Step 1: Write a function that can print out a board. Set up your board as a list, 
#where each index 1-9 corresponds with a number on a number pad,
# so you get a 3 by 3 board representation.
def display_board(x,y):
    print('\n'*100)
    print('Available   TIC-TAC-TOE\n'+
           '  moves\n\n  '+
          x[7]+'|'+x[8]+'|'+x[9]+'        '+y[7]+'|'+y[8]+'|'+y[9]+'\n  '+
          '-+-+-        -+-+-\n  '+
          x[4]+'|'+x[5]+'|'+x[6]+'        '+y[4]+'|'+y[5]+'|'+y[6]+'\n  '+
          '-+-+-        -+-+-\n  '+
          x[1]+'|'+x[2]+'|'+x[3]+'        '+y[1]+'|'+y[2]+'|'+y[3]+'\n')
    
display_board(available,theBoard)

#Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
#Think about using while loops to continually ask until you get a correct answer.
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board.
def place_marker(avail,board,marker,position):
    board[position] = marker
    avail[position] = ' '

#Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board,marker):
    return ((board[7] ==  board[8] ==  board[9] == marker) or # across the top
    (board[4] ==  board[5] ==  board[6] == marker) or # across the middle
    (board[1] ==  board[2] ==  board[3] == marker) or # across the bottom
    (board[7] ==  board[4] ==  board[1] == marker) or # down the left
    (board[8] ==  board[5] ==  board[2] == marker) or # down the middle
    (board[9] ==  board[6] ==  board[3] == marker) or # down the right 
    (board[7] ==  board[5] ==  board[3] == marker) or # diagonal
    (board[9] ==  board[5] ==  board[1] == marker)) # diagonal

#Step 5: Write a function that uses the random module to randomly decide which player goes first.
def random_player():
    return random.choice((-1, 1))


#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.  
def space_check(board,position):
    return board[position] == ' ' #bool to check the position between 0,10 

#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.
def full_board_check(board):
    return ' ' not in board[1:]

#Step 8: Write a function that asks for a player's next position (as a number 1-9) 
#and then uses the function from step 6 to check if it's a free position. 
# If it is, then return the position for later use.
def player_choice(board,player):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input('Player %s, choose your next position: (1-9) '%(player)))
        except:
            print("I'm sorry, please try again.")  
    return position

#Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#Run the game 
while True:
    print('\n'*100)
    print('Welcome to Tic Tac Toe!')
    toggle = random_player()
    player = players[toggle]
    print('For this round, Player %s will go first!' %(player))
    game_on = True
    input('Hit Enter to continue')    
    while game_on:
        display_board(available,theBoard)
        position = player_choice(theBoard,player)
        place_marker(available,theBoard,player,position)
        if win_check(theBoard, player):
            display_board(available,theBoard)
            print('Congratulations! Player '+player+' wins!')
            game_on = False
        else:
            if full_board_check(theBoard):
                display_board(available,theBoard)
                print('The game is a draw!')
                break
            else:
                toggle *= -1
                player = players[toggle]
                print('\n'*100)
    # reset the board and available moves list
    theBoard = [' '] * 10
    available = [str(num) for num in range(0,10)]
    if not replay():
        break
