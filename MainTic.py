#Import Needed libraries, maybe numPy, random, sys? 
##
##Define Board 3x3 
board =[[0,0,0],
        [0,0,0],
        [0,0,0]]


#Function that prints board to terminal.        
def show_board(thisBoard):
#Prints  axis for the board
    print("  "+"   ".join([str(i) for i in range(len(thisBoard))]))
#For all rows in the board, for all columns in rows print "" to space out into 3x3 
    count = 0
    for i in thisBoard:
        in_row = ""
        for j in i[:len(thisBoard)-1]:
            in_row+=str(j)+" | "
        in_row+=str(i[len(thisBoard)-1])
        print(count,in_row)
        if count!=len(thisBoard)-1:
            print("  ----------")
        count+=1

show_board(board)