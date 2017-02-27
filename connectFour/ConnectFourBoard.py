
# ConnectFourBoard.py
# Author: Aaiz N Ahmed
# Data: Feb 24, 2017
#
# Description: This file set up a connect four board

class ConnectFourBoard:

    ##
    # Constructor: Instantiates a Connect Board
    # @:param     number of rows
    # @:param     number of columns
    #
    def __init__(self, rowNum = 5, colNum = 5):

        if rowNum < 5:
            rowNum = 5

        if colNum < 5:
            colNum = 5

        # Assign row and col values to global variables for future use
        self.row = rowNum
        self.col = colNum

        # Fill in the board with "-" char
        self.board = [ [ '-' for i in range(colNum) ] for j in range(rowNum) ]


    ##
    #  This method set up the board and assign rows, cols in case the player loads a saved game form a file.
    #  @:param   lines ==> an array containing stored game data
    #  @:param     number of rows
    #  @:param     number of cols
    #
    def setBoard(self, lines, rowNum, colNum):

        self.row = rowNum
        self.col = colNum

        # Reassign the board to the provided dimensions
        self.board = [['-' for i in range(colNum)] for j in range(rowNum)]

        # Change the board elements to match the old game board
        for i in range(1, rowNum + 1, +1):
            for j in range (colNum):
                self.board[i-1][j] = lines[i][j]


    #
    # Print the board to see the current state of the game
    #
    def printBoard(self):

        board = ""

        for x in range(self.row):
            for y in range(self.col):
                board += self.board[x][y]
            board += '\n'

        print(board)

    ##
    # This method makes a valid move
    # @:param   player: Player 0 or 1
    # @:param   colNum: Column number
    #
    def makeMove(self, player, colNum):

        if 0 < colNum <= self.col:

            # number of rows and columns to be accessed
            row = self.row - 1
            col = colNum - 1

            # Going in reverse order because the columns should be filled bottom up
            for x in range(row, -1, -1):

                if self.board[x][col] == '-':

                    if player == 0:
                        self.board[x][col] = 'X'
                    elif player == 1:
                        self.board[x][col] = 'O'

                    return   # return beacuse we do not want loop to fill rest of the columns
    #   End of function

    ##
    # This method check if the given column is already full
    # @:param   column number to be checked
    #
    def columnCheck(self, colNum):

        if 0 < colNum <= self.col:

            col = colNum - 1

            # Only check row Zero because that is the top row
            if self.board[0][col] == 'X' or self.board[0][col] == 'O':

                return True

        return False

    ##
    #  A win occurs in Connect Four if 4 symbols are side by side.
    #  This can happen vertically, horizontally and diagonally.
    #  This method checks for the horizontal win condition.
    # @:return    True or False
    #

    def horizontalWin(self):

        for i in range(self.row):

            # Col - 3 will ensure that we don't go out of index while checking the win condition
            for j in range(self.col - 3):

                if self.board[i][j] == 'X':

                    # Check if next 3 elements are the same symbol as this one.
                    if self.board[i][j+1] == 'X' and self.board[i][j+2] == 'X' and self.board[i][j+3] == 'X':
                        return True

                elif self.board[i][j] == 'O':

                    if self.board[i][j+1] == 'O' and self.board[i][j+2] == 'O' and self.board[i][j+3] == 'O':
                        return True

        return False

    ##
    # This method checks for the vertical win condition
    # @:return   True or False
    #
    def verticalWin(self):

        for i in range(self.col):

            for j in range(self.row - 3):

                if self.board[j][i] == 'X':

                    if self.board[j+1][i] == 'X' and self.board[j+2][i] == 'X' and self.board[j+3][i] == 'X':
                        return True

                elif self.board[j][i] == 'O':

                    if self.board[j+1][i] == 'O' and self.board[j+2][i] == 'O' and self.board[j+3][i] == 'O':
                        return True

        return False

    ##
    # This method checks diagonal win condition from top left to bottom right
    # @:return True or False
    #
    def diagonallWinOne(self):

        for i in range(self.row - 3):

            for j in range(self.col - 3):

                if self.board[i][j] == 'X':

                    if self.board[i+1][j+1] == 'X' and self.board[i+2][j+2] == 'X' and self.board[i+3][j+3] == 'X':
                        return True

                elif self.board[i][j] == 'O':

                    if self.board[i+1][j+1] == 'O' and self.board[i+2][j+2] == 'O' and self.board[i+3][j+3] == 'O':
                        return True

        return False

    ##
    # This method checks diagonal win condition from bottom left to top right
    # @:return True or False
    #
    def diagonallWinTwo(self):

        for i in range(self.row - 1, 3, -1):

            for j in range(self.col - 3):

                if self.board[i][j] == 'X':

                    if self.board[i-1][j+1] == 'X' and self.board[i-2][j+2] == 'X' and self.board[i-3][j+3] == 'X':
                        return True

                elif self.board[i][j] == 'O':

                    if self.board[i-1][j+1] == 'O' and self.board[i-2][j+2] == 'O' and self.board[i-3][j+3] == 'O':
                        return True

        return False

    ##
    # This method checks all 4 win conditions
    # @:return True or False
    #
    def winAll(self):

        if self.verticalWin() is True or self.horizontalWin() is True or \
           self.diagonallWinOne() is True or self.diagonallWinTwo() is True:
            return True

        return False

# Unit Testing
def main():

    # x = ConnectFourBoard(8, 8)
    #
    # print( x.columnCheck(8) )
    #
    # x.makeMove(0, 8)
    # x.makeMove(1, 8)
    # x.makeMove(0, 8)
    # x.makeMove(1, 8)
    # x.makeMove(0, 8)
    # x.makeMove(1, 8)
    # x.makeMove(0, 8)
    # x.makeMove(1, 8)
    #
    # print( x.columnCheck(8) )
    #
    # x.printBoard()

    z = "Rows: 60 Cols: 64 Turn: 8"

    x = re.compile('\d+')
    y = x.findall(z)

    print( y )

# Run the program by calling the main
# main()
