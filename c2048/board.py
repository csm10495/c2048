"""
This file is part of c2048 - a Python object-oriented implementation of 2048
(C) - Charles Machalow - MIT License
"""

from square import Square
import random

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
            Compare equality of this object and another
        """
        selfList = []
        otherList = []

        for i in self.__squares:
            selfList.append(i.getValue())

        for i in other.__squares:
            otherList.append(i.getValue())

        return selfList == otherList

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

    def setRandomEmptySquareValue(self, value):
        """
        Brief:
           Picks a random square that doesn't have a value and set it.
           Returns True on success
           Returns False if there are no empty squares
        """
        emptySquares = []
        for i in self.__squares:
            if i.getValue() == 0:
                emptySquares.append(i)

        if len(emptySquares) == 0:
            return False

        (random.choice(emptySquares)).setValue(value)

        w = self.getSquareWidth()
        self.setSquareWidth(w)

        return True

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
