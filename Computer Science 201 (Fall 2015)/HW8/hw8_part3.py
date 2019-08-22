#File: HW8 hw8_part3.py
#Author: Caleb Massey
#Date: 11/20/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program uses recursive functions to find the Greatest Common
# Denominator of two numbers input by user.

def gcd(num1, num2, count):
    if num1 % count == 0 and num2 % count == 0:
        print("The GCD of", num1, "and", num2, "is", count)
    else:
        count = count - 1
        gcd(num1, num2, count)

def main():
    num1 = 0
    num2 = 0

    while num1 < 1:
        num1 = int(input("Enter your first number: "))
        if num1 < 1:
            print("Invalid Input: Number Must Be Greater Than 0")
    while num2 < 1:
        num2 = int(input("Enter your second number: "))
        if num2 < 1:
            print("Invalid Input: Number Must Be Greater Than 0")

    if num1 > num2:
        count = num2
        gcd(num1, num2, count)
    else:
        count = num1
        gcd(num2, num1, count)
main()
