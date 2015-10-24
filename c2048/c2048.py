"""
This file is part of c2048 - a Python object-oriented implementation of 2048
(C) - Charles Machalow - MIT License
"""

from board import *
import os

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
        If the char is equivalent to Ctrl+C, exit application
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
    
    #Ctrl + C
    if char == b'\x03':
        os.sys.exit(0)
    return char

def startUp(height=4, width=4):
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

    heightWidthStr = "Height: %d # Width: %d"  % (height, width)
    addLeft = False
    while len(heightWidthStr) < 31:
        addLeft = not addLeft
        if addLeft:
            heightWidthStr = " " + heightWidthStr
        else:
            heightWidthStr += " "

    print(("#" + heightWidthStr + "#").center(80))

    print("#################################".center(80))
    getch()
    clearScreen()

if __name__ == "__main__":
    """
    Brief:
        Main entry point to application when ran directly and not imported
    """
    if len(os.sys.argv) >= 3:
        startUp(height=int(os.sys.argv[1]), width=int(os.sys.argv[2]))
        thisBoard = Board(height=int(os.sys.argv[1]), width=int(os.sys.argv[2]))
    elif len(os.sys.argv) == 1:
        print("No args, defaulting to 4x4 c2048...")
        startUp(height=4, width=4)
        thisBoard = Board(height=4, width=4)
    elif len(os.sys.argv) == 2 and os.sys.argv[1] == "?" or os.sys.argv[1] == "help":
        print("Usage: python3 c2048.py height width. Providing no args will do 4x4 c2048")
        os.sys.exit(0)
    else:
        startUp()
        thisBoard = Board(height=4, width=4)

    thisBoard.setRandomEmptySquareValue(2)
    print(thisBoard)

    turnCount = 0
    while thisBoard.validMovesExist():
        char = getch()
        clearScreen()

        if char in thisBoard.DIRECTIONS:
            print("Recv'd command: " + thisBoard.DIRECTIONS[char][0].title())
            if thisBoard.moveValid(char):
                thisBoard.DIRECTIONS[char][1](thisBoard)
                thisBoard.setRandomEmptySquareValue(2)
                turnCount += 1
            else:
                print("Move is not valid because no square will move as a result.")
        else:
            print("Unknown command: " + str(char))
        print(thisBoard)

    print("Game Over! No Valid Moves Exist!")
    print("Number of Turns: %d" % turnCount)
    print("Largest Tile: %d" % thisBoard.getMaxSquareValue())
    input("Press Enter to Exit The Game")

