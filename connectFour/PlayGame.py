
# PlayGame.py
# Author: Aaiz N Ahmed
# Data: Feb 24, 2017
#
# Description: This file plays a  game of connec four.

from connectFour import ConnectFourBoard

def main():

    # First message
    print("Welcome to Connect Four!")

    print("Do you want to load a saved game?")
    ans = input()

    if ans == 'y':

        # load from file later
        print()

    again = ""

    while (again != 'n'):
    # else:
        global rows, cols

        # Get rows from user
        print("Please enter the number of rows. Minimum accepted value is 5: ")
        rows = int( input() )

        while (rows < 5):

            print("Rows can not be less than 5.")
            print("Please enter the number of rows. Minimum accepted value is 5: ")
            rows = int( input() )

        print("Please enter the number of columns. Minimum accepted value is 5: ")
        cols = int( input() )

        while (cols < 5):

            print("Columns can not be less than 5.")
            print("Please enter the number of Columns. Minimum accepted value is 5: ")
            cols = int( input() )

        # Done getting input from the user

        startGame(rows, cols)

        print("Do you want to play again? (y/n): ")
        again = input()


def startGame(rows, cols):
    # Instantiate a connect four board
    board = ConnectFourBoard.ConnectFourBoard(rows, cols)

    for i in range(rows * cols):

        if i % 2 == 0:

            print("Player 1: Please enter the column number. What is your choice?")
            colNum = int(input())

            board.makeMove(0, colNum)
            board.printBoard()

            # print( board.winAll() )

            if board.winAll() is True:
                print("Player 1: Congratulations!! You won!")
                return

        else:

            print("Player 2: Please enter the column number. What is your choice?")
            colNum = int(input())

            board.makeMove(1, colNum)
            board.printBoard()

            if board.winAll() is True:
                print("Player 2: Congratulations!! You won!")
                return


main()