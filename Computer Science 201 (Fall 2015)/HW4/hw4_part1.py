#File: HW4 hw4_part1.py
#Author: Caleb Massey
#Date: 9/26/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program takes an input from the user for a height and a
# symbol, then prints out a triangle of the height given with symbols given.

def main():
#This is the code that prompts the user for a height and symbol.
    height = int(input("Please enter the height of the triangle: "))
    symbol = str(input("Please enter a single character for the symbol: "))

#Prints the triangle by printing one symbol and increasing until at height.
    for i in range(height):
        print(symbol * (i + 1))

main()
