#File: HW4 hw4_part5.py
#Author: Caleb Massey
#Date: 9/26/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program prompts a user for a string and then prints out
# the number of times a certain character appears in string.

def main():
#This code asks user for a string and a character.
    string = str(input("Please enter a string: "))
    character = str(input("Please enter a character: "))

#This code goes through ever charachter in string and keeps count of the number 
# of times the input character appears.
    COUNT = 0
    strList = list(string)
    for item in strList:
        if item == character:
            COUNT = COUNT + 1
    print("The character", character, "appears", COUNT, "times in the string", string)
        
    

main()
