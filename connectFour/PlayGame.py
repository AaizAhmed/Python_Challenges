
# PlayGame.py
# Author: Aaiz N Ahmed
# Data: Feb 24, 2017
#
# Description: This file plays a  game of connec four.

from connectFour import ConnectFourBoard
import re

def main():

    # Global variables for storing game state
    global rows, cols, turn, board, firstRun, loadFailed
    turn = 0
    board = ConnectFourBoard.ConnectFourBoard()
    firstRun = True
    loadFailed = False

    # First message
    print("Welcome to Connect Four!")
    ans = ""

    while True:

        # Run till user gives correct input i.e. y or n

        print("Do you want to load a saved game? y/n: ")
        ans = input()

        if ans == "y" or ans == "n":
            break

    if ans == 'y':

        print("Enter the file name: ")
        name = input()

        # Read from the file in the try/expect block
        try:

            with open(name) as f:
                lines = f.read().splitlines()

            # Use regex to get rows, cols and turn
            x = re.findall('\d+', lines[0])

            rows = int(x[0])
            cols = int(x[1])
            turn = int(x[2])

            board.setBoard(lines, rows, cols)
            board.printBoard()

        except IOError:
            print("Error: Can not find the file or the file does not exist\n")
            loadFailed = True

    again = ""
    while again != 'n':

        # If the user did not load a game from file get the rows and columns
        # If this file loading failed get rows and cols
        # If user loaded the file, finished the game and wanted to play again, get rows and cols

        if ans == "n" or firstRun is False or loadFailed is True:

            while True:
                # Get rows from user
                print("Please enter the number of rows. Minimum accepted value is 5: ")
                rows = input()

                if rows.isdigit() and int(rows) >= 5:
                    break

            while True:
                print("Please enter the number of columns. Minimum accepted value is 5: ")
                cols = input()

                if cols.isdigit() and int(cols) >= 5:
                    break
            # Done getting input from the user

            rows = int(rows)
            cols = int(cols)
            turn = 0

            # Instantiate a connect four board
            board = ConnectFourBoard.ConnectFourBoard(rows, cols)
            board.printBoard()

        if ans == 'y':
            firstRun = False

        startGame()

        while True:
            print("Do you want to play again? (y/n): ")
            again = input()

            if again == 'n' or again == 'y':
                break


def startGame():

    for i in range(turn, rows*cols, +1):

        if i % 2 == 0:

            print("Player 1: What is your choice?")
            colNum = isValid(1, i)

            board.makeMove(0, colNum)
            board.printBoard()

            if board.winAll() is True:
                print("Player 1: Congratulations!! You won!")
                return

        else:

            print("Player 2: What is your choice?")
            colNum = isValid(2, i)

            board.makeMove(1, colNum)
            board.printBoard()

            if board.winAll() is True:
                print("Player 2: Congratulations!! You won!")
                return

    print("There was a draw!")

##
# Check if the column entered by the player is valid or not
# Additionally, save the game if user types s
# @:return  A valid column number given by the user
#
def isValid(player, moveNum):

    while True:

        print("Please enter a valid column number: 1 to %d or s to save the game" % cols)
        colNum = input()

        if colNum.isdigit():

            colNum = int(colNum)

            if board.columnCheck(colNum) is True:
                print("The column you entered is already full.")

            # Check if column is already full
            if board.columnCheck(colNum) is False and (0 < colNum <= cols):
                return colNum

        if colNum == 's':

            print("Enter the file name in which you want to save the game: ")
            name = input()
            file = open(name, "w")

            file.write("Rows: %d Cols: %d Turn: %d\n" % (rows, cols, moveNum))

            for i in range(rows):
                for j in range(cols):
                    file.write(board.board[i][j])
                file.write("\n")

            file.close()
            print("File saved")
            print("Player %d: What is your choice?" % player)

# -------------------------------------------------

# Run the game
main()

# -------------------------------------------------
