#File: HW5 hw5_part3.py
#Author: Caleb Massey
#Date: 10/12/15
#Section: 23
#Email: cmassey1@gmail.com
#Description: This program simulates the movement of a hailstorm
# If the current height is 1, quit the program
# If the current height is even, cut it in half (divide by 2)
# If the current height is odd, multiply it by 3, then add 1

def main():
    user = int(input("Please enter a postitve integer: ")) #Prompts user.
    print("Hail is currently at", int(user))
    while user > 0:
        if user == 1: #Checks to see if program needs to close.
            user = -1
            print("PROGRAM CLOSED")
        elif user % 2 == 0: #Checks for even.
            user = user / 2 #Divides even by 2
            print("Hail is currently at", int(user))
        else: #Runs for odds.
            user = (user * 3) + 1 #Multiplies odd by 3 then adds 1.
            print("Hail is currently at", int(user))
    print()
main()
