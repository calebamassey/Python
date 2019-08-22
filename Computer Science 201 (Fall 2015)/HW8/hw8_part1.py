#File: HW8 hw8_part1.py
#Author: Caleb Massey
#Date: 11/20/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program takes in integers and stores them in a list until
# they enter "-1", then the list will be printed and then printed out in reverse
# order.


def rev(myList):
    print(myList[len(myList) - 1])
    myList.remove(myList[len(myList) - 1])
    if len(myList) > 0:
        rev(myList)
    

def makeList(num, myList):
    while num != -1:
        num = int(input("Enter a number to append to the list, or -1 to stop: "))
        if num != -1:
            myList.append(num)
    return myList

def main():
    myList = []
    myList = makeList(0, myList)
    print("The list as you entered it is: ", myList)
    print("The reversed list is: ")
    rev(myList)
main()
