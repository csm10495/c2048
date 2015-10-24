"""
This file is part of c2048 - a Python object-oriented implementation of 2048
(C) - Charles Machalow - MIT License
"""

class Square():
    """
        Brief:
            This class represents a piece on the game board for c2048
    """

    def __init__(self, value=None, width=None, horizontalChar="-", verticalChar="|"):
        """
        Brief:
            Constructor for the Square class
        """
        self.__value = value

        self.__horizontalChar = horizontalChar
        self.__verticalChar = verticalChar

        if value is None:
            self.__width = None
        else:
            self.__width = 0
            if value == 0:
                self.__width = 1
            else:
                while value != 0:
                    self.__width += 1
                    value //= 10

        if width is not None and value is not None:
            self.__width = width

    def __str__(self):
        """
        Brief:
            Return a string representation of this square
        """

        correctedValue = self.getValue()
        if correctedValue == 0:
            correctedValue = ""
        numstr = str.center(str(correctedValue), self.getWidth())

        retstr = " " + (self.__horizontalChar * self.getWidth())
        for i in range(self.getWidth()):
            retstr += "\n" + self.__verticalChar
            for j in range(self.getWidth()):
                if i == (self.getWidth() // 2):
                    retstr += numstr[j]
                else:
                    retstr += " "
            retstr += self.__verticalChar

        retstr += "\n " + (self.__horizontalChar * self.getWidth())
        return retstr

    def __eq__(self, other):
        """
        Brief:
            Used for checking the equality of two Square objects
        """
        return self.getValue() == other.getValue()

    def setBorderToNormal(self):
        """
        Brief:
            Resets both horizontal and vertical border chars to their default values
        """
        self.__horizontalChar = "-"
        self.__verticalChar = "|"

    def setBorderToStars(self):
        """
        Brief:
            Resets both horizontal and vertical border chars to stars
        """
        self.__horizontalChar = "*"
        self.__verticalChar = "*"

    def getEmptySquare(self):
        """
        Brief:
            Return a string representation of this square without a value
        """
        retstr = " " + ("-" * self.getWidth())
        for i in range(self.getWidth()):
            retstr += "\n|"
            for j in range(self.getWidth()):
                retstr += " "
            retstr += "|"

        retstr += "\n " + ("-" * self.getWidth())
        return retstr

    def getValue(self):
        """
        Brief:
            Return the square's value
        """
        return self.__value

    def setValue(self, value):
        """
        Brief:
            Set the square's value, also updates width
        """
        self.__value = value

        self.__width = 0
        while value != 0:
            self.__width += 1
            value //= 10

    def getWidth(self):
        """
        Brief:
            Get the width of this square
        """
        return self.__width

    def setWidth(self, width):
        """
        Brief:
            Set the width of this square
        """
        self.__width = width
