"""
File: MidpointKarel.py
Name: Jessie
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will find midpoint.
    """
    if not front_is_clear():
        put_beeper()
    else:
        fill_a_line()
        turn_arround()
        while front_is_clear():
            move()
        turn_arround()
        fill_b_line()
        turn_arround()
        while front_is_clear():
            move()
        turn_arround()
        pick_one_beeper()
        Karel_goes_to_midpoint()


def Karel_goes_to_midpoint():
    """
    pre-condition: Karel is at upper left, facing west.
    post-condition: Karel is at midpoint, facing south.
    """
    turn_arround()
    while not on_beeper():
        move()
        turn_right()
        move()
        turn_left()
    pick_beeper()
    turn_right()
    while front_is_clear():
        move()
    put_beeper()


def fill_a_line():
    """
    pre-condition:Karel is at lower left, facing east.
    post-condition:Karel is at upper right, facing east.
    """
    put_beeper()
    while front_is_clear():
        move()
        turn_left()
        move()
        put_beeper()
        turn_right()


def fill_b_line():
    """
    pre-condition: Karel is at upper left, facing east.
    post-condition: Karel is at lower right, facing east.
    """
    put_beeper()
    while front_is_clear():
        move()
        turn_right()
        move()
        put_beeper()
        turn_left()


def clean_a_line():
    """
    pre-condition: Karel is at lower right, facing west.
    post-condition: Karel is at lower left, facing west.
    """
    while front_is_clear():
        if on_beeper():
            pick_beeper()
            move()
        else:
            move()
    if on_beeper():
        pick_beeper()
        turn_arround()
    else:
        turn_arround()
    while front_is_clear():
        move()



def pick_one_beeper():
    """
    pre-condition: Karel is at lower right, facing west.
    post-condition: Karel is at upper left, facing west.
    """
    while front_is_clear():
        clean_a_line()
        if right_is_clear():
            turn_right()
            move()
            turn_right()



def turn_arround():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()




# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
