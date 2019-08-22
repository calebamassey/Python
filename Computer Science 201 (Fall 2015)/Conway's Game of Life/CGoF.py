#File: PROJ1 proj1.py
#Author: Caleb Massey
#Date: 11/2/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This a simple cellular automata game, called
#Conway's Game of Life. In this game, you have a grid where
#pixels can either be on or off, and simple rules that govern
#whether those pixels will be on or off (dead or alive) at the next timestep.

#Prints a new board for each iteration
def nextIteration(board, iterate, time):
    newBoard = checkNewBoard(board)
    print ("Iteration ",(time - iterate + 1) , ":")
    printBoard(board)
    iterate = iterate - 1
    if iterate > 0:
        nextIteration(newBoard, iterate, time)

def checkNewBoard(board):
    countList = []
    board = list(board)
    for row in range(0, len(board)):
        countList.append([])
        for spot in range(0, len(board[row])):
            row = int(row)
            spot = int(spot)
            count = 0
            #check top left
            if row == 0 and spot == 0:
                if int(board[row][spot + 1]) == 1:
                    count = count + 1
                if int(board[row + 1][spot]) == 1:
                    count = count + 1
                if int(board[row + 1][spot + 1]) == 1:
                    count = count + 1
            #check top right
            elif row == 0 and spot == (len(board[row]) - 1):
                if int(board[row][spot - 1]) == 1:
                    count = count + 1
                if int(board[row + 1][spot - 1]) == 1:
                    count = count + 1
                if int(board[row + 1][spot]) == 1:
                    count = count + 1
            #check bottom left
            elif row == (len(board) - 1) and spot == 0:
                if int(board[row - 1][spot]) == 1:
                    count = count + 1
                if int(board[row - 1][spot + 1]) == 1:
                        count = count + 1
                if int(board[row][spot + 1]) == 1:
                        count = count + 1
            #check bottom right
            elif row == (len(board) - 1) and spot == (len(board[row]) - 1):
                if int(board[row - 1][spot - 1]) == 1:
                    count = count + 1
                if int(board[row - 1][spot]) == 1:
                    count = count + 1
                if int(board[row][spot - 1]) == 1:
                    count = count + 1
            #check top
            elif row == 0:
                for i in range(0, 2): #row
                    for j in range(-1, 2): #col
                        if i == 1 and j == 0:
                            donothing = 0
                        else:
                            if int(board[row + i][spot + j]) == 1:
                                count = count + 1
            #check bottom
            elif row == (len(board) - 1):
                for i in range(-1, 1): #row
                    for j in range(-1, 2): #col
                        if i == 0 and j == 0:
                            donothing = 0
                        else:
                            if int(board[row + i][spot + j]) == 1:
                                count = count + 1
            #check left side
            elif spot == 0:
                for i in range(-1, 2): #row
                    for j in range(0, 2): #col
                        if i == 0 and j == 0:
                            donothing = 0
                        else:
                            if int(board[row + i][spot + j]) == 1:
                                count = count + 1
            #check right side
            elif spot == (len(board[row]) - 1):
                for i in range(-1, 2): #row
                    for j in range(-1, 1): #col
                        if i == 0 and j == 0:
                            donothing = 0
                        else:
                            if int(board[row + i][spot + j]) == 1:
                                count = count + 1
           #check spots with no borders
            else:
                for i in range(-1, 2): #row
                    for j in range(-1, 2): #col
                        if i == 0 and j == 0:
                            donothing = 0
                        else:
                            if int(board[row + i][spot + j]) == 1:
                                count = count + 1
                    
            #make list of counts
            countList[row].append(count)
    return (checkLife(board, countList))

#check if cell lives or dies
def checkLife(board, countList):
    for row in  range(len(countList)):
        for spot in range(len(countList[row])):
            if (int(countList[row][spot]) == 2 or int(countList[row][spot]) == 3) and int(board[row][spot]) == 1:
                board[row][spot] = 1
            elif (int(countList[row][spot]) < 2) and (int(board[row][spot]) == 1):
                board[row][spot] = 0
            elif int(countList[row][spot]) > 3 and int(board[row][spot]) == 1:
                board[row][spot] = 0
            elif int(countList[row][spot]) == 3 and int(board[row][spot]) == 0:
                board[row][spot] = 1
    return board

#Print the starting board
def setLiving(board):
    rowSet = 0
    board = list(board)
    while rowSet != 'q':
        rowSet = input("Please enter  the row of a cell to turn on (or q to exit):")
        if rowSet != 'q':
            if int(rowSet) >= 0 and int(rowSet) <= (len(board) - 1):
                colSet = input("Please enter a column for that cell:")
                if int(colSet) >= 0 and int(colSet) < len(board[0]):
                    board[int(rowSet)][int(colSet)] = 1
                else:
                    print("Error Invalid input, input must be between 0 and ", len(board[0]))
            else:
                print("Error Invalid input, input must be between 0 and ", len(board))
        else:
            rowSet = 'q'
    print("Starting Board: ")
    printBoard(board)

#prints each iteration of the board.
def printBoard(board):
    for item in (board):
        for spot in item:
            if spot == 0:
                print ('.', end='')
            elif spot == 1:
                print ('A', end='')
        print("\n")

#Sets the board to desired length
def setBoard(row, col):
    board = []
    for colNum in range(col):
        board.append([])
        for rowNum in range(row):
            board[colNum].append(0)
    setLiving(board)
    return board

def main():
    #Error checks
    col = 0
    while col < 1:
        col = int(input("Please enter number of columns: "))
        if col < 1:
            print ("Invalid input")
    row = 0
    while row < 1:
        row = int(input("Please enter number of rows: "))
        if row < 1:
            print ("Invalid input")
    iterations = 0
    while iterations < 1:
        iterations = int(input("How many iterations should I run? "))
        if iterations < 1:
            print("Invalid input")
    
    #Calls functions
    board = setBoard(row, col)
    nextIteration(board, iterations, iterations)
main()
