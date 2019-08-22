#File: hw6 hw6_part1.py
#Author: Caleb Massey
#Date: 10/19/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program propmts the user for names and saves them to 
# names.txt until user types DONE.

def main():
    
    nameList = open("names.txt", "w") #opens names.txt file.
    stop = False #makes while loop true.
    #Continually asks for name until DONE is entered.
    while stop != True:
        name = str(input("Please enter a name (or \"DONE\" to stop): "))
        if name == "DONE":
            stop = True #causes while loop to end.
        else: 
            nameList.write("Hello " + name + "!\n") #writes name into file.
    nameList.close()
main()
