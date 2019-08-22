#File: HW5 hw5_part2.py
#Author: Caleb Massey
#Date: 10/12/15
#Section: 23
#Email: cmassey1@gmail.com
#Description: This program takes an input height and width
# and prints out numbers in order to fill it.

def main():
    width = int(input( "Input a width: "))
    height = int(input("Input a height: "))
    myList = [] #total list
    i = 0
    
    while i <= (height - 1): #so we have height number of rows
        for j in range (width): #so each row has width length
            j = j + (width * i)   #changes number depending on row
            myList.append(j + 1)
        i = i + 1               #keeps count for while loop
        fullList = myList[0]
        for k in range (1, width):
            fullList = str(fullList) + str(myList[k])  # makes list str
        print(fullList)    #prints a row
        print()        #moves to next row
        myList.clear()     #restarts list for next row
main()


