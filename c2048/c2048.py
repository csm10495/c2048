"""
This file is part of c2048 - a Python object-oriented implementation of 2048
(C) - Charles Machalow - MIT License
"""

from board import *
import os
import copy

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

def startUp():
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
    startUp()
    thisBoard = Board()
    thisBoard.setRandomEmptySquareValue(2)
    print(thisBoard)

    while thisBoard.validMovesExist():
        char = getch()
        clearScreen()

        if char in thisBoard.DIRECTIONS:
            print("Recv'd command: " + thisBoard.DIRECTIONS[char][0])
            if thisBoard.moveValid(char):
                thisBoard.DIRECTIONS[char][1](thisBoard)
                thisBoard.setRandomEmptySquareValue(2)
            else:
                print("Move is not valid")
        else:
            print("Unknown command: " + str(char))

        print(thisBoard)
