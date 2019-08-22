#File: HW5 hw5_part1.py
#Author: Caleb Massey
#Date: 10/12/15
#Section: 23
#Email: cmassey1@gmail.com
#Description: This program prompts user for a number between 0-100(inclusive)
# and continues to ask until number between 0-100 is given.

def main():
    user = 1 #Used to make while statement true and begin loop.
    while user >= 0 and user <= 100:
        user = int(input("Please enter a number (between 0-100, inclusive): "))
        if user >= 0 and user <= 100:
            print("Thank you for selecting the number", user, "\n")
            user = -1 #Used to make while statement false.
        else:
            print("Invalid number, try again.")
            user = 1 #Used to make while statement true and restart loop.
main()
