#File: HW5 hw5_part4.py
#Author: Caleb Massey
#Date: 10/12/15
#Section: 23
#Email: cmassey1@gmail.com
#Description: This program takes 2 lists and creates a new list of the original
# lists added together.

def main():
    list1 = []
    list2 = []
    fullList = []
    num = 0

    while num != "end": #Compiled the first list.
        num = input("Please enter a number (or \"end\" to stop): ")
        if num != "end":
            num = int(num)
            list1.append(num)
    print("Thank you for completing te first list.")
    
    num = 0  #Reset num to not equal 'end'
    while num != "end": #Compiled the second list.
        num = input("Please enter a number (or \"end\" to stop): ")
        if num != "end":
            num = int(num)
            list2.append(num)
    print("Thank you for completing te second list.")
    
    for i in range(len(list1)): #Went through each spot in list1 and list2 adding them together
        fullList.append(list1[i] + list2[i])
    print(fullList)             

main()
