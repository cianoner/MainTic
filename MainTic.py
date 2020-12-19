#Import Needed libraries, maybe numPy, random, sys? 
import sys
import itertools
##Define Board 3x3 


#defines board numbers as Xs or Os
def printXO(xo):
    if xo == 1:
        return "X"
    elif xo == 2:
        return "O"
    else:
        return " "
#Function that prints board to terminal.        
def show_board(thisBoard):
#Prints  axis for the board
    print("  "+"   ".join([str(i) for i in range(len(thisBoard))]))
#For all rows in the board, for all columns in rows print "" to space out into 3x3 
    count = 0
    for i in thisBoard:
        in_row = ""
        for j in i[:len(thisBoard)-1]:
            in_row+=printXO(j)+" | "
        in_row+=printXO(i[len(thisBoard)-1])
        print(count,in_row)
        if count!=len(thisBoard)-1:
            print("  ----------")
        count+=1

#function that allows user input. passes in the current board and the current player
def userInput(thisBoard, currentPlayer):
    print("\t Current Player: ", currentPlayer)
    
    row = int(input("Please choose a row to play: "))
    column = int(input("Please choose a column to play: "))
    #If the space is empty take it
    #added error handling Try Except for index error.

    try:
        if thisBoard[row][column] == 0:
            thisBoard[row][column] = currentPlayer
        else: #if the space is taken print Taken 
            print("Taken! please choose again.")
            userInput(thisBoard,currentPlayer)
    except IndexError as e:
        print("Please use the format for rows and columns with 0, 1 or 2")
        userInput(thisBoard, currentPlayer)
    except Exception as e:
        print("Error", e)
        userInput(thisBoard, currentPlayer)

#Function that checks for wins
#Vertical Win
#Horizontal Win 
#Diagonal Win

#threeOfKind returns true of all elements are the same.
#stops a winning condition with an empty board.
def threeOfKind(thisList):
    if thisList.count(thisList[0])==len(thisList) and thisList[0]!=0:
        return True
    else:
        return False
def winner(thisBoard):
#Horizontal Winner
    for row in thisBoard:
        if threeOfKind(row):
            print(f"Player {row[0]} is the winner")
            return True
#Vertical
    for i in range(len(thisBoard)):
        vert = []
        #range from 0-2
        for j in range(len(thisBoard)):
            #adds element at 0 position from every row to vert
            vert.append(thisBoard[j][i])
            #checks if all the values are the same if they are, winner!
        if threeOfKind(vert):
            print(f"Player {vert[0]} is the winner")
            return True
#Right Diagonal
    r_diag = []
    for p in range(len(thisBoard)):
        for l in range(len(thisBoard)):
            if p+l == len(thisBoard) - 1:
                r_diag.append(thisBoard[p][l])
    if threeOfKind(r_diag):
        print(f"Player {r_diag[0]} is the winner")
        return True 

#Left Diagonal
    l_diag = []
    for i in range(len(thisBoard)):
        l_diag.append(thisBoard[i][i])
    if threeOfKind(l_diag):
         print(f"Player {l_diag[0]} is the winner")
         return True    


# if winner(board):
#     print("Winner")
# else:
#     print("No winner")

game = True
while game:
    board =[[0,0,0],
        [0,0,0],
        [0,0,0]]

#Loops game while nobody is the winner.
    game_win = False
    show_board(board) # Shows the board before first move is made
    counter = 0 #Variable to track tie game
    playerChoose = itertools.cycle([1,2]) #Iterates of Player 1 and 2
    while not game_win:
        currentPlayer = next(playerChoose)
        userInput(board,currentPlayer)
        counter+=1
        show_board(board)
        if winner(board) or counter == 9:
        #Checks for draw 
            if counter == 9:
                print("Tie Game! ")
            game_win = True
            again = input("Would you like to play again? (y/n): ")
            if again.lower()=="y":
                print("Loading new game... ")
                game = True
            elif again.lower() == "n":
                print("Goodbye!")
                game = False
            else:
                print("Invalid choice, Goodbye!")
                game = False


sys.stdin.readline()