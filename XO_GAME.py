
board=[0,1,2,
       3,4,5,
       6,7,8]
#menu function to start or exit the game
def menu():
    while True:
        try:
          print("Welcom in tic_tac_toe\n 1)Start game. \n 2)Exit. ")
          choice = int(input("Please choose from 1 or 2:"))
          print("")
          if choice in [1,2]:
             return choice
          else:
             print("Invalid number!please choose from 1 or 2.\n")
        except ValueError:
             print("Invalid number!please choose from 1 or 2.\n")
             
#function to display the Tic Tac Toe board             
def tic_tac_toe(): 
    print('-------------')
    print('|',board[0],'|',board[1],'|',board[2],'|')
    print('-------------')
    print('|',board[3],'|',board[4],'|',board[5],'|')
    print('-------------')
    print('|',board[6],'|',board[7],'|',board[8],'|')
    print('-------------')
    
#move function 
def move(player,position): 
    board[position] =player

#turn function
def turn(player):
    print ("\n", player, 'your turn\n')
    while True:
        try:
            player_input = int(input("Enter your position (0-8): "))
            if player_input in range(9) and board[player_input] not in ["X", "O"]:
                move(player, player_input)
                break
            else:
                print("Invaled input! Entar number (1-8):\n")
        except ValueError:
            print("Invaled input! Entar number (1-8):\n")
            
# function to check for a winner
def check_winner():
    for i in range(0,9,3):
     #check rows
        if board[i]==board[i+1]==board[i+2]:
           return True
     #check columns
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]:
           return True
     #check diagonals
    if  board[0]==board[4]==board[8]or board[2]==board[4]==board[6]:
        return True
    return False

#game function
def game():
    global board
    while True:
        try:
            player = 'X'
            choice=menu()           
            if choice==1:
                board=[0,1,2,3,4,5,6,7,8]
                while True:
                    tic_tac_toe()
                    turn(player)
                    if check_winner():
                        print(player,"is winner\n")
                        break
                    if all([cell == 'X' or cell == 'O' for cell in board]):
                        print("Draw!\n")
                        break
                    #switch player for the next turn
                    player = 'O' if player == 'X' else 'X'              
            else:
                print("Exiting the game.") #if choice =2
                break
        except ValueError:
             print("Invaled input! Entar number (1-8):\n")   
#start game              
game()              