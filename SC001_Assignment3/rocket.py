"""
File: rocket.py
Name: Jessie
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    The rocket will separate into 6 part: head, belt, upper, lower, belt , head.
    It is suitable for any size.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print('')


def belt():
    print('+', end='')
    for i in range(SIZE*2):
        print('=', end='')
    print('+')


def upper():
    for i in range(SIZE):
        print('|', end='')
        for j in range(SIZE-1-i):
            print('.', end='')
        for j in range(i+1):
            print('/\\', end='')
        for j in range(SIZE-1-i):
            print('.', end='')
        print('|')


def lower():
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE-i):
            print('\/', end='')
        for j in range(i):
            print('.', end='')
        print('|')


if __name__ == "__main__":
    main()
