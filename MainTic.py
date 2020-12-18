#Import Needed libraries, maybe numPy, random, sys? 
##
##Define Board 3x3 
board =[[0,0,0],
        [0,0,0],
        [0,0,0]]

#Prints a horizontal axis for the board
print(" ".join([str(i)for i in range (len(board))]))

#print(board)
#For all rows in the board, for all columns in rows print "" to space out into 3x3 
for i in board:
    for j in i:
        print(j, end = " ")
    print(" ")

