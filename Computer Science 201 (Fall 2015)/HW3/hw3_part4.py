#File: hw3 hw3_part4.py
#Author: Caleb Massey
#Date: 9/16/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program tells the user if the generator
#is on depending on position of switches, if both y or n the
#generator is off, if one is y and one is n the generator is on.

def main():
#First gets switch position input from user.
    switchOne = input("What is the state of switch 1? (y/n) ")
    switchTwo = input("What is the state of switch 2? (y/n) ")
#Now we compare switch positions and output whether generator is on or off.
    if ((switchOne == 'y') and (switchTwo == 'y')) or ((switchOne == 'n') and (switchTwo == 'n')):
        print ("The generator is off")
    else: 
        print ("The generator is on")
main()
