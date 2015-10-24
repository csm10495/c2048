"""
This file is part of c2048 - a Python object-oriented implementation of 2048
(C) - Charles Machalow - MIT License
"""

from square import Square
import random
import copy

class Board():
    """
    Brief:
        This class represents the game board for c2048
    """

    def __init__(self, width=4, height=4, squareValue=0):
        """
        Brief:
            Constructor for the Board class
        """
        self.__width = width
        self.__height = height
        self.__squares = []

        for i in range(self.getNumSquares()):
            self.__squares.append(Square(value=squareValue))

    def __str__(self):
        """
        Brief:
            Return a string representation of this board
        """
        retLst = []
        output = ""

        for i in range(self.getSquareWidth() + 2):
            retLst.append("")

        squaresPrinted = 0
        while squaresPrinted != self.getNumSquares():
            for i in range(self.getWidth()):
                c = 0
                for j in str(self.__squares[squaresPrinted]).splitlines():
                    retLst[c] += j
                    if c == 0 or c == len(retLst) - 1:
                        retLst[c] += " "
                    c += 1
                squaresPrinted += 1

            output += '\n'.join(retLst) + "\n"

            retLst.clear()
            for i in range(self.getSquareWidth() + 2):
                retLst.append("")

        return output

    def __eq__(self, other):
        """
        Brief:
            Compare equality of this Board object and another
        """
        selfList = []
        otherList = []

        for i in self.__squares:
            selfList.append(i.getValue())

        for i in other.__squares:
            otherList.append(i.getValue())

        return selfList == otherList and self.getHeight() == other.getHeight() and self.getWidth() == other.getWidth()

    def getWidth(self):
        """
        Brief:
            Return the number of squares on the width of the board
        """
        return self.__width

    def getHeight(self):
        """
        Brief:
            Return the number of squares on the height of the board
        """
        return self.__height

    def getNumSquares(self):
        """
        Brief:
            Returns the number of squares on the board
        """
        return self.getHeight() * self.getWidth()

    def getSquareWidth(self):
        """
        Brief:
            Returns the width for each sqaure
        """
        biggestWidth = 0
        for i in self.__squares:
            biggestWidth = max(biggestWidth, i.getWidth())
        return biggestWidth

    def setSquareWidth(self, width):
        """
        Brief:
            Iterates over each square and sets the width
        """
        for i in self.__squares:
            i.setWidth(width)

    def setSquareBordersToNormal(self):
        """
        Brief:
            Sets all square's borders to normal chars
        """
        for i in self.__squares:
            i.setBorderToNormal()

    def setRandomEmptySquareValue(self, value):
        """
        Brief:
           Picks a random square that doesn't have a value and set it.
           Returns a Square on success
           Returns False if there are no empty squares
        """
        emptySquares = []
        for i in self.__squares:
            if i.getValue() == 0:
                emptySquares.append(i)

        if len(emptySquares) == 0:
            return False

        self.setSquareBordersToNormal()

        square = (random.choice(emptySquares))
        square.setValue(value)
        square.setBorderToStars()

        self.setSquareWidth(self.getSquareWidth())

        return square

    def getRows(self):
        """
        Brief:
            Returns a list of lists. The inner lists correspond to rows of squares on the board
        """
        retList = []
        for i, item in enumerate(self.__squares):
            if i % self.getWidth() == 0:
                retList.append([])
            retList[-1].append(item)

        return retList

    def setRow(self, rowNum, values):
        """
        Brief:
            Sets a specific row's (0 indexed) values
            Returns True on success, False on failure
        """
        squareNum = rowNum * self.getWidth()

        if squareNum > self.getNumSquares() - self.getWidth():
            return False

        for i in values:
            self.__squares[squareNum] = i
            squareNum += 1

        return True

    def setColumn(self, colNum, values):
        """
        Brief:
            Sets a specific column's (0 indexed) values
            Returns True on success, False on failure
        """
        squareNum = colNum

        for i in values:
            self.__squares[squareNum] = i
            squareNum += self.getWidth()

        return True

    def getColumns(self):
        """
        Brief:
            Returns a list of lists. The inner lists correspond to columns of squares on the board
        """
        retList = []

        for i in range(self.getWidth()):
            retList.append([])

        for i, item in enumerate(self.__squares):
            retList[i % self.getWidth()].append(item)

        return retList

    def getMaxSquareValue(self):
        """
        Brief:
            Returns the maximum square value on the board
        """
        maxValue = 0
        for i in self.__squares:
            if i.getValue() > maxValue:
                maxValue = i.getValue()
        return maxValue

    def removeEmptySquares(self, row):
        """
        Brief:
            Returns a list derived from the given one with all empty squares removed
        """
        newRow = []
        for i in row:
            if i.getValue() != 0:
                newRow.append(i)
        return newRow

    def moveLeft(self):
        """
        Brief:
            Moves all squares on the given board left
        """
        rows = self.getRows()

        for count, row in enumerate(rows):
            newRow = self.removeEmptySquares(row)

            for i in range(len(newRow)-1):
                if newRow[i] == newRow[i+1]:
                    newRow[i].setValue(newRow[i].getValue() * 2)
                    newRow[i+1].setValue(0)
            newRow = self.removeEmptySquares(row)

            while len(newRow) < len(row):
                newRow.append(Square(value=0))

            self.setRow(count, newRow)

    def moveRight(self):
        """
        Brief:
            Moves all squares on the given board right
        """
        rows = self.getRows()

        for count, row in enumerate(rows):
            newRow = self.removeEmptySquares(row)

            for i in range(1, len(newRow)):
                if newRow[i] == newRow[i-1]:
                    newRow[i].setValue(newRow[i].getValue() * 2)
                    newRow[i-1].setValue(0)
            newRow = self.removeEmptySquares(row)

            while len(newRow) < len(row):
                newRow.insert(0,Square(value=0))

            self.setRow(count, newRow)

    def moveUp(self):
        """
        Brief:
            Moves all squares on the given board up
        """
        cols = self.getColumns()

        for count, col in enumerate(cols):
            newCol = self.removeEmptySquares(col)

            for i in range(len(newCol)-1):
                if newCol[i] == newCol[i+1]:
                    newCol[i].setValue(newCol[i].getValue() * 2)
                    newCol[i+1].setValue(0)
            newCol = self.removeEmptySquares(col)

            while len(newCol) < len(col):
                newCol.append(Square(value=0))

            self.setColumn(count, newCol)

    def moveDown(self):
        """
        Brief:
            Moves all squares on the given board down
        """
        cols = self.getColumns()

        for count, col in enumerate(cols):
            newCol = self.removeEmptySquares(col)

            for i in range(1, len(newCol)):
                if newCol[i] == newCol[i-1]:
                    newCol[i].setValue(newCol[i].getValue() * 2)
                    newCol[i-1].setValue(0)
            newCol = self.removeEmptySquares(col)

            while len(newCol) < len(col):
                newCol.insert(0, Square(value=0))

            self.setColumn(count, newCol)

    def validMovesExist(self):
        """
        Brief:
            Returns True if there is at least one move that can change the board
        """
        testBoard = copy.deepcopy(self)
        testBoard.moveLeft()
        if testBoard != self:
            return True

        testBoard = copy.deepcopy(self)
        testBoard.moveRight()
        if testBoard != self:
            return True

        testBoard = copy.deepcopy(self)
        testBoard.moveUp()
        if testBoard != self:
            return True

        testBoard = copy.deepcopy(self)
        testBoard.moveDown()
        if testBoard != self:
            return True

        return False

    def moveValid(self, moveStr):
        """
        Brief:
            Returns true if the move is valid
        """
        testBoard = copy.deepcopy(self)
        testBoard.DIRECTIONS[moveStr][1](testBoard)
        return testBoard != self

    DIRECTIONS = {
    b'a' : ('LEFT', moveLeft),
    b'd' : ('RIGHT', moveRight),
    b'w' : ('UP', moveUp),
    b's' : ('DOWN', moveDown),
    b'K' : ('LEFT', moveLeft),
    b'M' : ('RIGHT', moveRight),
    b'H' : ('UP', moveUp),
    b'P' : ('DOWN', moveDown),
    }