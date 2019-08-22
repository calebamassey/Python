#File: HW3 hw3_part1.py
#Author: Caleb Massey
#Date: 9/16/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: Read in three floats from the user (you may assume the user will 
# actually enter numbers). Print out the average of these numbers.

def main():
#Variables num1, num2, and num3, are used to store floats input by user.
    num1 = float(input("Please enter a float point number: "))
    num2 = float(input("Please enter a float point number: "))
    num3 = float(input("Please enter a float point number: "))
#This is the equation to find the average of the floats and store it in avg.
    avg = float(num1 + num2 + num3)/3
#This is where the code prints out the avg of the floats.
    print("The average of the three floats is:", avg)
main()
