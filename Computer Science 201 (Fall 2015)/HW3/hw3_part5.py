#File: hw3 hw3_part5.py
#Author: Caleb Massey
#Date: 9/16/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program tells the day of the week from the
#day of the month, assuming there are 31 days in the month and day 1
#starts on Monday.

def main():
#First we ask for users input of the day of the month.
    day = int(input("What is the day of the month? "))
#Then we test validity of the day.
    if ((day > 31) or (day < 1)):
        print ("Invalid Day")
#Now the program find remainder of day %7 and then finds which day it is.
    elif (0 == day % 7):
        print ("Today is Sunday")
    elif (1 == day % 7):
        print ("Today is Monday")
    elif (2 == day % 7):
        print ("Today is Tuesday")
    elif (3 == day % 7):
        print ("Today is Wednesday")
    elif (4 == day % 7):
        print ("Today is Thursday")
    elif (5 == day % 7):
        print ("Today is Friday")
    elif (6 == day % 7):
        print ("Today is Saturday")
main()
