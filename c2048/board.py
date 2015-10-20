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

        for i in range(self.__width * self.__height):
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
        while squaresPrinted != self.__height * self.__width:
            for i in range(self.__width):
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
            if i.getValue() == "":
                emptySquares.append(i)

        if len(emptySquares) == 0:
            return False

        (random.choice(emptySquares)).setValue(value)

        w = self.getSquareWidth()
        self.setSquareWidth(w)

        return True
