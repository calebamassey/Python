#File: HW3 hw3_part3.py
#Author: Caleb Massey
#Date: 9/16/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This takes inputs from the user and outputs the medical diagnosis.

def main():
#This is where the user inputs which symptoms they have and depending on what
# symptoms they have it will ask for other symptoms, and then print the 
# diagnosis.
    fever = input("Do you have a fever? (y/n) ")
    if fever == 'y':
        rash = input ("Do you have a rash? (y/n) ")
        if rash == 'y':
            print ("You have Measles")
        else:
            earHurt = input("Does your ears hurt? (y/n) ")
            if earHurt == 'y':
                print("You have an Ear Infection")
            else:
                print("You have the Flu")
    else:
        stuffNose = input("Is your nose stuffy? (y/n) ")
        if stuffNose == 'y':
            print("You have a Head Cold")
        else:
            print("You have Hypochondriac")
main()
