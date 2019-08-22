#File: PROJ2 proj2.py
#Author: Caleb Massey
#Date: 11/26/2015
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program is to prompt to the user for a file, then ask
# the user for a spot to start filling in the area, and to auto fill that
# blocked off area, with a symbol of the user's choice.

import math #imports sin, cos, pi.

#Function that is recursive and fills up the grid with users symbol.
def autoFill(grid, row, col, symb, show):    
    move = 0 #initializes the variable move, which will change causing the direction of the check to change.
    while move <= 3*(math.pi)/2: #move can only move to 3*pi/2
        if grid[row - int(math.cos(move))][col + int(math.sin(move))] == " ": #cos & sin change as move increases, checking top => right => bottom => left
            grid[row - int(math.cos(move))][col + int(math.sin(move))]= symb #changes spot in the grid that is blank to be the symbol.
            if show == True:
                printGrid(grid) #prints each recursion
            autoFill(grid, row - int(math.cos(move)), col + int(math.sin(move)), symb, show) #recursive part.
        move = move + (math.pi)/2 #move is increasing by pi/2 for every loop.
    return grid #changed grid is sent back to previous loop of function.
           
#Verifies that the coordinates given by the user is valid.
def checkPoint(grid, gridWidth, gridHeight):
    point = ""
    valid = False
    while valid == False:
        point = str(input("Please enter the coordinates you would like to start filling at in the form \"row,col\", or Q to quit: "))
        if point == "Q":
            valid = True #makes loop end
        elif len(point.split(',')) == 2: #splts point into a list and checks length to make sure there are two numbers.
            nums = point.split(',')
            row = int(nums[0])
            col = int(nums[1])
            if row < 0 or col < 0 or row >= gridHeight or col >= gridWidth: #runs if length error in input.
                if row < 0 or row > gridHeight - 1: #runs if error in the row
                    print("INVALID INPUT:", row, "is not a valid row input; please enter a number between 0 and", gridHeight - 1, "inclusive.")
                if col < 0 or col > gridWidth - 1: #runs if error in the column
                    print("INVALID INPUT:", col, "is not a valid column input; please enter a number between 0 and", gridWidth - 1, "inclusive.")
            elif grid[row][col] != " ": #returns 0,0 if there is something in coordinate already.
                return 0,0
            else:
                return row, col
        else:
            print("INVALID INPUT:", point, "must be input as \"row,col\" or Q to quit.") #error that runs if the input was done in the wrong format.
    return -1, -1 #returns -1,-1 if user input "Q", which will end the code in the main()

#Opens the file the user input, prints the original file, and saves the file to a list.
def callFile(myFile):    
    print("", end=" ")
    grid = [] 
    count = 0

    printGrid = open(myFile, "r") #Opens file.
    #Puts the file in a list and prints it.
    for line in printGrid:
        print(line, end = " ")
        grid.append([])
        for spot in line:
            grid[count].append(spot)
        count = count + 1
    printGrid.close() #Closes file
    return grid #Returns the list made from the file

#File that inputs grid and prints it.
def printGrid(grid):
    for line in grid:
        for spot in line:
            print(spot, end="")
        print(end="")
    print("")

def main():
    #Verifies input ends with ".txt" or ".dat"
    valid = False
    while valid == False:
        myFile = str(input("Please enter a file for input: "))
        if str(myFile[-4:]) == ".dat" or str(myFile[-4:]) == ".txt":
            valid = True
        else:
            print("INVALID INPUT: File must end with .dat or .txt")
    
    grid = callFile(myFile) #Sends inputed file to function callFile() and saves the return as grid
    gridWidth = len(grid[0]) #Finds width of the grid.
    gridHeight = len(grid) #Finds height of grid.
    
    #Loop that continually asks for coordinates to be autofilled until input "Q"
    run = True #Makes loop run.
    while run == True:
        row, col = checkPoint(grid, gridWidth, gridHeight) #Validates coordinates.
        if (row == -1 and col == -1) == False: #If the coordinates do not equal -1,-1 it runs.
            
            #Validates only one character is input for symbol.
            symLen = 0
            while symLen != 1:
                symb = str(input("Please enter a character to fill with: "))
                symLen = len(symb)
                if symLen != 1:
                    print("INVALID INPUT:", symb, "must be a single character.")
                    
            #Validates only "yes" and "no" can be responses for recursion.
            loop = True
            while loop == True:
                show = str(input("Would you like to show each step of the recursion? \n Enter \"yes\" or \"no\": "))
                if show == "yes":
                    show = True
                    loop = False #Ends loop
                elif show == "no":
                    show = False
                    loop = False #Ends loop
                else:
                    print("Invalid Input: Must enter \"yes\" or \"no\"")

            #Runs according to if the coordiante had something there already or not.
            if (row == 0 and col == 0) == False: #If the row,col doesnt equal 0,0 which means there is something already at coordinate
                grid[row][col] = symb
                if show == True:
                    printGrid(grid)
                newGrid = autoFill(grid, row, col, symb, show)
                print("================================================================")
                printGrid(newGrid)
            elif row == 0 and col == 0: #if the coordinate already had something there it prints out the same board.
                printGrid(grid)
        else: #ends the while loop and says goodbye
            run = False
main()
