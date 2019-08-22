import random

def setupGame():
    gameBoard = [[]]
    gameSize = selectGame()
    if (gameSize == '1'):
        gameBoard = Three_in_a_Row()
    elif (gameSize == '2'):
        gameBoard = Four_in_a_Row()
    elif (gameSize == '3'):
        gameBoard = Five_in_a_Row()
    elif (gameSize != '1', '2', '3'):
        print ("Not a correct game selection")
    for row in gameBoard:
        print (row)

    player1, player2 = selectSymbols()

    startGame(player1, player2, gameBoard)

def selectGame():
    print ("Select what size game to play: \n\t 1: Three in a Row \n\t 2: Four in a Row \n\t 3: Five in a Row")
    return (input("Enter your selection 1, 2, or 3: "))

def selectSymbols():
    player_1_symbol = input("Player 1 Enter Your Symbol (A Single Character): ")
    player_2_symbol = input("Player 2 Enter Your Symbol (A Single Character): ")
    return player_1_symbol, player_2_symbol

def Three_in_a_Row():
    board = [['0','0','0'], ['0','0','0'], ['0','0','0']]
    return (board)

def Four_in_a_Row():
    board =  [['0','0','0','0','0','0','0', '0'], ['0','0','0','0','0','0','0', '0'], ['0','0','0','0','0','0','0', '0'], ['0','0','0','0','0','0','0', '0'], ['0','0','0','0','0','0','0', '0'], ['0','0','0','0','0','0','0', '0'], ['0','0','0','0','0','0','0', '0'], ['0','0','0','0','0','0','0', '0']]
    return (board)

def Five_in_a_Row():
    board =  [['0','0','0','0','0','0','0', '0', '0', '0'], ['0','0','0','0','0','0','0', '0', '0', '0'], ['0','0','0','0','0','0','0', '0', '0', '0'], ['0','0','0','0','0','0','0', '0', '0', '0'], ['0','0','0','0','0','0','0', '0', '0', '0'], ['0','0','0','0','0','0','0', '0', '0', '0'], ['0','0','0','0','0','0','0', '0', '0', '0'], ['0','0','0','0','0','0','0', '0', '0', '0'], ['0','0','0','0','0','0','0', '0', '0', '0'], ['0','0','0','0','0','0','0', '0', '0', '0']]
    return (board)

def startGame(player1, player2, gameBoard):
    print ("Game has started")
    startPlayer = random.randint(0,1)
    if (startPlayer == 0):
        player = player1
        while (noWinner(player1, player2, gameBoard) == True):
            col = input("Player with symbol " + player + " select column (starts at 0): ")
            if (checkValid(col, gameBoard) == True):
                print ("Valid Column")
            else:
                print ("Invalid Column Input")

    else:
        player = player2
        while (noWinner(player1, player2, gameBoard) == True):
            col = input("Player with symbol " + player + " select column (starts at 0): ")
            if (checkValid(col, gameBoard) == True):
                print ("Valid Column")
            else:
                print ("Invalid Column Input")


def checkValid(column, gameBoard):
    if (int(column) < len(gameBoard)):
        return True
    else:
        return False

def noWinner(player1, player2, gameBoard):
    return True

setupGame()
