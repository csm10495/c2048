"""
This file is part of c2048 - a Python object-oriented implementation of 2048
(C) - Charles Machalow - MIT License
"""

class Square():
    """
        Brief:
            This class represents a piece on the game board for c2048
    """

    def __init__(self, value=None, width=None):
        """
        Brief:
            Constructor for the Square class
        """
        self.__value = value

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
        numstr = str.center(str(self.getValue()), self.getWidth())

        retstr = " " + ("-" * self.getWidth())
        for i in range(self.getWidth()):
            retstr += "\n|"
            for j in range(self.getWidth()):
                if i == (self.getWidth() // 2):
                    retstr += numstr[j]
                else:
                    retstr += " "
            retstr += "|"

        retstr += "\n " + ("-" * self.getWidth())
        return retstr

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
        if self.__value == 0:
            return ""
        else:
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
