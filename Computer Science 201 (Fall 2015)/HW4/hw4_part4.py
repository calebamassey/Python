#File: HW4 hw4_part4.py
#Author: Caleb Massey
#Date: 9/26/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: 

def main():
    myList = []
#For loop to put every number from 1-100 into myList.
    for i in range(100):
        myList.append(i + 1)
#This for loop makes sure each number or phrase is in its own line. Also this 
# code checks conditions to see of divisible by 3 or 5 or both.
    for item in myList:
        if item % 3 == 0 and item % 5 == 0:
            print("In the future, everyone will be world-famous for 15 minutes.")
        elif item % 3 == 0:
            print("Better three hours too soon than a minute late.")
        elif item % 5 == 0:
            print("Where do you see yourself in five years?")
        else:
            print(item)
main()
