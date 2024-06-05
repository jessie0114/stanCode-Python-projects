"""
File: CollectNewspaperKarel.py
Name: Jessie
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel picks up the newspaper.
    """
    go_out()
    go_in()


def go_out():
    """
    pre-condition: Karel is in the upper left corner of the house, facing East.
    post-condition: Karel is on the beeper, facing East.
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()


def go_in():
    """
    pre-condition: Karel is on the beeper, facing East.
    post-condition: Karel is in the upper left corner of the house, facing East.
    """
    pick_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
