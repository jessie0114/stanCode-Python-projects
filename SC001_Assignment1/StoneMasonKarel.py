"""
File: StoneMasonKarel.py
Name: Jessie
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel fills in the pillar.
    """
    while front_is_clear():
        up()
        move()
        move()
        move()
        move()
        down()


def up():
    """
    pre-condition: Karel is at the bottom of pillar, facing east.
    post-condition: Karel is at the top of pillar, facing east.
    """
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if on_beeper():
        turn_right()
    else:
        put_beeper()
        turn_right()


def down():
    """
    pre-condition: Karel is at the top of pillar, facing east.
    post-condition: Karel is at the bottom of pillar, facing east.
    """
    turn_right()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
