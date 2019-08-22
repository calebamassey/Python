#File: HW4 hw4_part3.py
#Author: Caleb Massey
#Date: 9/26/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program determines whether the 10 subject input can or cannot
# be studied

def main():
    myList = []
#Ask for the ten inputs
    for i in range(10):
        subject = str(input("Please enter a word: "))
        myList.append(subject)

#Checks the list for the subjects, then checks if it ends with 'ology' and 
# prints can study subject if it does end with 'ology'.
    for item in myList:
        list(item)
        if str(item[-5:]) == 'ology':
            print ("You can study", str(item))
        else: 
            print(str(item))

main()
