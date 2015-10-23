"""
This file is part of c2048 - a Python object-oriented implementation of 2048
(C) - Charles Machalow - MIT License
"""

from board import *
import os
import copy

def removeEmptySquares(row):
    """
    Brief:
        Returns a list derived from the given one with all empty squares removed
    """
    newRow = []
    for i in row:
        if i.getValue() != 0:
            newRow.append(i)
    return newRow

def moveLeft(thisBoard):
    """
    Brief:
        Moves all squares on the given board left
    """
    rows = thisBoard.getRows()

    for count, row in enumerate(rows):
        newRow = removeEmptySquares(row)

        for i in range(len(newRow)-1):
            if newRow[i].getValue() == newRow[i+1].getValue():
                newRow[i].setValue(newRow[i].getValue() * 2)
                newRow[i+1].setValue(0)
        newRow = removeEmptySquares(row)

        while len(newRow) < len(row):
            newRow.append(Square(value=0))

        thisBoard.setRow(count, newRow)

def moveRight(thisBoard):
    """
    Brief:
        Moves all squares on the given board right
    """
    rows = thisBoard.getRows()

    for count, row in enumerate(rows):
        newRow = removeEmptySquares(row)

        for i in range(1, len(newRow)):
            if newRow[i].getValue() == newRow[i-1].getValue():
                newRow[i].setValue(newRow[i].getValue() * 2)
                newRow[i-1].setValue(0)
        newRow = removeEmptySquares(row)

        while len(newRow) < len(row):
            newRow.insert(0,Square(value=0))

        thisBoard.setRow(count, newRow)

def moveUp(thisBoard):
    """
    Brief:
        Moves all squares on the given board up
    """
    cols = thisBoard.getColumns()

    for count, col in enumerate(cols):
        newCol = removeEmptySquares(col)

        for i in range(len(newCol)-1):
            if newCol[i].getValue() == newCol[i+1].getValue():
                newCol[i].setValue(newCol[i].getValue() * 2)
                newCol[i+1].setValue(0)
        newCol = removeEmptySquares(col)

        while len(newCol) < len(col):
            newCol.append(Square(value=0))

        thisBoard.setColumn(count, newCol)

def moveDown(thisBoard):
    """
    Brief:
        Moves all squares on the given board down
    """
    cols = thisBoard.getColumns()

    for count, col in enumerate(cols):
        newCol = removeEmptySquares(col)

        for i in range(1, len(newCol)):
            if newCol[i].getValue() == newCol[i-1].getValue():
                newCol[i].setValue(newCol[i].getValue() * 2)
                newCol[i-1].setValue(0)
        newCol = removeEmptySquares(col)

        while len(newCol) < len(col):
            newCol.insert(0, Square(value=0))

        thisBoard.setColumn(count, newCol)

def validMovesExist(thisBoard):
    """
    Brief:
        Returns True if there is at least one move that can change the board
    """
    testBoard = copy.deepcopy(thisBoard)
    moveLeft(testBoard)
    if testBoard != thisBoard:
        return True

    testBoard = copy.deepcopy(thisBoard)
    moveRight(testBoard)
    if testBoard != thisBoard:
        return True

    testBoard = copy.deepcopy(thisBoard)
    moveUp(testBoard)
    if testBoard != thisBoard:
        return True

    testBoard = copy.deepcopy(thisBoard)
    moveDown(testBoard)
    if testBoard != thisBoard:
        return True

    return False

DIRECTIONS = {
b'a' : ('LEFT', moveLeft),
b'd' : ('RIGHT', moveRight),
b'w' : ('UP', moveUp),
b's' : ('DOWN', moveDown),
}

def clearScreen():
    """
    Brief:
        Clears the terminal window
    """
    if 'win32' in os.sys.platform:
        t = os.system('cls')
    else:
        t = os.system('clear')

def getch():
    """
    Brief:
        Get one character from stdin and return it.
        Returned as a byte string (eg: b'a')
    """
    try:
        #Windows
        import msvcrt
        char = msvcrt.getch()
    except:
        #Linux
        import sys, tty, termios
        fd = sys.stdin.fileno()
        save = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            #reset terminal
            termios.tcsetattr(fd, termios.TCSADRAIN, save)

    return char

def main():
    """
    Brief:
        Function called on application run
    """
    print("#################################".center(80))
    print("#-------Welcome to c2048!-------#".center(80))
    print("#===============================#".center(80))
    print("# Use the WSAD keys to move the #".center(80))
    print("#      pieces on the board      #".center(80))
    print("#      press any key to go      #".center(80))
    print("#################################".center(80))
    
    getch()
    clearScreen()

if __name__ == "__main__":
    main()
    thisBoard = Board()

    while True:
        char = getch()
        clearScreen()

        if char in DIRECTIONS:
            print("Recv'd command: " + DIRECTIONS[char][0])
            DIRECTIONS[char][1](thisBoard)
        else:
            print("Unknown command: " + str(char))
            continue

        thisBoard.setRandomEmptySquareValue(2)
        #print(validMovesExist(thisBoard))
        print(thisBoard)