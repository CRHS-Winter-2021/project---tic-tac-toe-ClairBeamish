##Tic Tac Toe
#Name: Clarissa Beamish
#Date: 02/10/21


#1. (Var) Setup the empty board as a list
theBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
B1 = ["X", " ", "O", " ", " ", " ", "X", " ", " ", " "]

#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none

def printBoard(board):
  print(board[7], "|", board[8], "|", board[9])
  print("--+---+--")
  print(board[4], "|", board[5], "|", board[6])
  print("--+---+--")
  print(board[1], "|", board[2], "|", board[3])

#3a. (fun) Determine if player is X or O
player1 = ''
player2 = ''

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None

def chooseLetter():
    print("x or o?")
    choice = input()
    if choice == "x":
      player1 = "x"
      player2 = "o"
    elif choice == "o":
      player1 == "o"
      player2 == "x"
    else:
      print("Try again")


#3b. (fun) Choose starting player 1 or 2
def chooseStart():
  print("Who will start? (player 1 or 2)")
  player = input()
  if player == "1":
    player = "e"
  elif player == "2":
    player = "t"
  else:
    print("Try again")

#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none

def playerMove(board, player):
  
    pass


#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
    
def checkWin(board, player):
    pass


#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise

def checkFull(board):
    pass

#7. Main function

def main():
    #print Welcome
    print("Welcome to the TicTacToe game!")
    #print instructions
    print("instructions: your goal ")

    #game play
    #get player letter choice
    
    #while board is not full
    ###first player move
        #player chooses move
        #print board
        #check win
        #check board full

    ###second player move
        #player chooses move
        #print baord
        #check win