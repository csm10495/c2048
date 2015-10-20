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
    
    try:
        #Windows
        import msvcrt
        msvcrt.getch()
    except:
        #Linux
        import sys, tty, termios
        fd = sys.stdin.fileno()
        save = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            #reset terminal
            termios.tcsetattr(fd, termios.TCSADRAIN, save)

    clearScreen()

if __name__ == "__main__":
    main()
    a = Board()
    a.setRandomEmptySquareValue(999999)

    while True:
        input()
        a.setRandomEmptySquareValue(999999)
        print(a)