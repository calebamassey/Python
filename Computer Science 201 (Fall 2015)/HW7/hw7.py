#File: HW7 hw7.y
#Author: Caleb Massey
#Date: 10/23/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program uses prompts user for a list of integers, then
# it prompts user for a function and then runs the integers through the function
# and prints out results.

#Prints the Menu for the calculator.
def printMenu():
    print("\n", "Please choose the statistic you would like to calculate!")
    print(" 1. Min\n","2. Max\n","3. Mean\n","4. Median\n", "5. Clear List\n")
    choice = int(input("Please enter your choice, or 0 to exit: "))
    return choice

#Fills list with users inputs until user types "q".
def getList():
    myList = []
    num = 0
    while str(num) != 'q':
        num = input("Enter an integer (or \"q\" to quit): ")
        if str(num) != 'q':
            myList.append(num)
    return myList

#Finds the mean of the list.
def getMean(userList):
    total = 0
    for num in userList:
        total = total + int(num)
    finalNum = total / int(len(userList))
    return finalNum

#Finds the median depending on whether the length of the list is even or odd.
def getMedian(userList):
    userList = sortList(userList) #Sends to sort list into least to greatest order.
    length = int(len(userList))
    if length % 2 == 0: #Finds median if even numbers in List.
        median = (int(userList[int((length / 2) - 1)]) + int(userList[int(length / 2)])) / 2
    else: #Finds median if odd numbers in List.
        median = userList[len(userList) // 2]
    return median

#Sets first number in list to lowest and then searches list for any
# numbers lower and replaces it until it has no lower numbers that it.
def getMin(userList):
    mini = int(userList[0])
    for num in userList:
        if int(num) < int(mini):
            mini = num
        print(mini)
    return mini

#Sets first number in list to greatest and then searches list for any
# numbers higher and replaces it until it has no higher numbers that it.
def getMax(userList):
    maxi = userList[0]
    for num in userList:
        if int(num) > int(maxi):
            maxi = num
    return maxi

#Reinitializes list to be empty.
def emptyList(userList):
    userList = []
    return userList
    
#Sorts the list to return in order from least to greatest numbers
def sortList(userList):
    sortList = []
    for i in range(len(userList)):
        mini = userList[0]
        for item in userList:
            if int(item) < int(mini):
                mini = item
        sortList.append(mini)
        userList.remove(mini)
    return sortList

def main():
    choice = 1
    print("\n", "Welcome to the List Statistics Calculator")
    myList = getList() #Gets the list

    while choice > 0: #Makes while loop run until person inputs "0".
        choice = printMenu() 
        if int(choice) == 1:
            print("The minimum number is: ", getMin(myList)) #Gets and prints Min.
        elif int(choice) == 2:
            print("The maximum number is: ", getMax(myList)) #Gets and prints Max.
        elif int(choice) == 3:
            print("The mean value is: ", getMean(myList)) #Gets and prints Mean Value.
        elif int(choice) == 4:
            print("The median value is: ", getMedian(myList)) #Gets and prints Median Value.
        elif int(choice) == 5:
            emptyList(myList) #Erases List.
            myList = getList() #Refills List.
        elif int(choice) == 0: #Ends the while loop.
            print("Goodbye, Thank You for using our Calculator.")
main()
