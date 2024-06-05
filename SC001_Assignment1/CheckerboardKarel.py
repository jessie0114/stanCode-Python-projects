"""
File: CheckerboardKarel.py
Name: Jessie
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel fills lines with beepers with intervals.
    """
    if front_is_clear():
        while front_is_clear():
            fill_a_line()
            if right_is_clear():
                turn_right()
                move()
                turn_right()
                fill_b_line()
                if right_is_clear():
                    turn_right()
                    move()
                    turn_right()
    else:
        turn_left()
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()


def fill_a_line():
    """
    pre-condition: Karel is at the left of the street, facing east.
    post-condition: Karel is at the left of the street, facing west.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()


def fill_b_line():
    """
    pre-condition: Karel is at the left of the street, facing east.
    post-condition: Karel is at the left of the street, facing west.
    """
    move()
    while front_is_clear():
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
