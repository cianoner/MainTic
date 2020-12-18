#Import Needed libraries, maybe numPy, random, sys? 
import sys
##Define Board 3x3 
board =[[0,1,0],
        [0,0,0],
        [0,2,0]]

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
show_board(board)
#function that allows user input. passes in the current board and the current player
def userInput(thisBoard, currentPlayer):
    print("\t Current Player: ", currentPlayer)
    
    row = int(input("Please choose a row to play: "))
    column = int(input("Please choose a column to play: "))

    if thisBoard[row][column] == 0:
        thisBoard[row][column] = currentPlayer
    else:
        print("Taken! please choose again.")
        userInput(thisBoard,currentPlayer)
    
    userInput(board,1)
    show_board(board)

    sys.stdin.readline()