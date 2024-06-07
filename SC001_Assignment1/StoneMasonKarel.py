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
    pre-condition: Karel is at the lower left corner of the world, and there are
                   several broken pillars that are needed to be repaired.
    post-condition: Karel is at the lower right corner of world, facing east, and
                    the pillars have been repaired.

    This program makes Karel to repair all the broken pillars in the world, with three
    steps, which is represented by three functions.
    """
    while front_is_clear():
        climb_up_and_repair()
        go_back()
        cross()
    climb_up_and_repair()  # prevent the OBOB error
    go_back()


def climb_up_and_repair():
    """
    pre-condition: Karel is at the bottom of a broken pillar, facing east.
    post-condition: Karel is at the top of a pillar which is just repaired.

    Karel climbs up the pillar, and repair with beepers.
    """
    turn_left()
    while front_is_clear():
        put_beeper_safely()
        move()
    put_beeper_safely()  # prevent the OBOB error


def go_back():
    """
    pre-condition: Karel is at the top of a pillar which is just repaired.
    post-condition: Karel is at the bottom of a pillar which is just repaired,
                    facing east.

    After fixing a pillar, Karel climbs down the pillar, turns to the its left
    side, is ready to move to another pillar.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def cross():
    """
    pre-condition: Karel is at the bottom of a pillar which is just repaired.
    post-condition: Karel is at the bottom of another broken pillar.

    Karel moves four steps to arrive the bottom of another broken pillar, facing east.
    """
    for i in range(4):
        move()


def put_beeper_safely():
    """
    In order to prevent that there are more than one beepers at a position, check whether
    there is a beeper before putting down one.
    """
    if not on_beeper():
        put_beeper()


def turn_around():
    """
    Karel makes a 180 degrees turn.
    """
    turn_left()
    turn_left()
    

if __name__ == '__main__':
    execute_karel_task(main)
