#File: hw6 hw6_part3.py
#Author: Caleb Massey
#Date: 10/19/15
#Section: 23
#Email: cmassey1@umbc.edu
#Description: This program opens a file prompted by user and tells user total 
# number of words in file, as well a average word length.

def main():
    wordCount = 0
    totalLet = 0
    valid = False

    #While loop that checks if file is valid.
    while valid == False:
        files = input("Please enter name of file: ")
        if str(files[-4:]) != ".txt":
            if str(files[-4:]) != ".dat":
                print("The file must end in .txt or .dat to be valid.")
            else:
                valid = True #Makes while loop end.
        else:
            valid = True #Makes while loop end.

    #Opens file.
    myFile = open(files, "r")

    #Checks the words in each line.
    for lines in myFile:
        words = lines.split()
        #Checks the characters in each word.
        for letter in words:
            totalLet = totalLet + len(letter) #Adds up for total character count.
        wordCount = wordCount + len(words) #Adds up for total word count.

    #Prints out the results.
    print("The file", files, "has", wordCount, "words in it.")
    print("On average, each word is", totalLet/wordCount, "characters long.")
main()
