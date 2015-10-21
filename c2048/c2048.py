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
    a = Board()

    count = 2
    while True:
        b = getch()
        clearScreen()
        print(b)
        print(a.setRandomEmptySquareValue(count))
        print(a)
        count *= 32