#File: HW3 hw3_part2.py
#Author: Caleb Massey
#Date: 9/16/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program is a grade calculator that calculates grades
# based on specific inputs from user and outputs grade on a A-F scale.

def main():
# This is where the inputs by the user are stored into variables.
# All weights should add up to 1
    hwWeight = float(input("Please Enter Weight of Homework: "))
    hwGrade = float(input("Please Enter Grade of Homework: "))
    examWeight = float(input("Please Enter Weight of Exam: "))
    examGrade = float(input("Please Enter Grade of Exam: "))
    discWeight = float(input("Please Enter Weight of Discussion: "))
    discGrade = float(input("Please Enter Grade of Discussion: "))

# This is finding the total grade and prints final numerical grade.
    total = (hwWeight * hwGrade) + (examWeight * examGrade) + (discWeight * discGrade) 
    print("The final numerical grade is: ", total)
# Finds the letter grade based on the total grade.
    if total >= 90:
        print("You have an A in the class.")
    elif total >= 80 and total < 90:
        print("You have a B in the class.")
    elif total >= 70 and total < 80:
        print("You have a C in the class.")
    elif total >= 60 and total < 70:
        print("You have a D in the class.")
    else:
        print("You have a F in the class.")
main()
