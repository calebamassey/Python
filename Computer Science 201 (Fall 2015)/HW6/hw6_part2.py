#File: hw6 hw6_part2.py
#Author: Caleb Massey
#Date: 10/19/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program takes in a file from user and then calculates the 
# grade by the information in the file.

def main():
    total = 0
    #prompts user for file name and opens file.
    files = str(input("Please enter file that contaions the grades: ")) 
    grade = open(files, "r")
    #for each line in file it makes a list of all numbers.
    for line in grade:
       percents =  line.split()
       weight = float(percents[0]) #takes first spot in the line.
       avg = 0 #Resets the avg for each line.
       #takes the average for each line
       for i in range(1, len(percents)):
           avg = avg + float(percents[i])
       avg = avg/(len(percents) - 1)
       
       avg = avg * weight #takes weighted average of line

       total = total + avg #adds all the avg from each line together.
    print ("Your final weighted score is ", total)
main()
