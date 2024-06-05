"""
File: hailstone.py
Name: Jessie
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program will use two ways to turn any positive integer into 1.
    """
    print('This program computes Hailstone sequences.')
    print('')
    n = int(input('Enter a number: '))
    hailstone = my_hailstone(n)
    print(hailstone)

def my_hailstone(n):
    steps = 0
    while n != 1:
        print(n, end = '')
        if n % 2 == 0:
            n = n // 2
            print(' is even, so I take half: ', n)
        else:
            n = 3 * n + 1
            print(' is odd, so I make 3n+1: ', n)
        steps += 1
    print('It took',  steps, 'steps to reach 1.')





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
