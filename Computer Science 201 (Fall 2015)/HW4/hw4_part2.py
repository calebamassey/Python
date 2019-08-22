#File: HW4 hw4_part2.py
#Author: Caleb Massey
#Date: 9/26/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This is a program where I prompt the user for a height, width and
# symbol, and then make a empty box of that height and width made of that symbol.

def main():
#This is where I prompt the user for a height, width, and symbol input.
    height = int(input("Please enter the height of the box: "))
    width = int(input("Please enter the width of the box: "))
    symbol = str(input("PLease enter a single character fo the symbol: "))

#Prints a full length of the width, then prints the symbol and then blank spaces
# for a width-2 and then another symbol all the way down to the last line, where 
# it is fully filled in again.
    print(symbol * width)
    for i in range(height - 2):
        print (symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)
main()
