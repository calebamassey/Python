#File: HW8 hw8_part2.py
#Author: Caleb Massey
#Date: 11/20/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program prints out a right triangle pointing down,
# it is made by prompting the user for height and symbol.

def tri(sym, height):
    if height > 0:
        print(sym * height)
        height = height - 1
        tri(sym, height)

def main():
    num = 0
    while num < 1:
        num = int(input("Enter a height for the triangle: "))
        if num < 1:
            print("Error Invalid Input: Number Must Be Greater Than 0")
    sym = str(input("Enter the character for your triangle: "))
    tri(sym, num)
main() 
