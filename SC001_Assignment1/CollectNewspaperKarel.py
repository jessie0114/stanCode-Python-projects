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
    pre-condition: Karel is at the upper left corner of its house.
    post-condition: Karel is at the upper left corner of its house with a beeper.

    This program is decomposed of two function, for the purpose of moving out to
    collect the newspaper, which is represented by a beeper, and returning to its
    initial position putting down the newspaper.
    """
    move_out_and_pick()
    go_home_and_put()


def move_out_and_pick():
    """
    pre-condition: Karel is at the upper left corner of its house.
    post-condition: Karel stands at where the newspaper is and pick up the newspaper.

    The purpose of this function is to let Karel move out and go collect the newspaper,
    which is represented by a beeper.
    """
    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()
    pick_beeper()


def go_home_and_put():
    """
    pre-condition: Karel is at where the newspaper is, carrying a beeper with it.
    post-condition: Karel is at the upper left corner of its house with a beeper put down.

    After collecting the newspaper, Karel returning to its initial position and put down
    the newspaper that it just collected.
    """
    turn_around()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_around():
    """
    Karel make a 180 degrees turn.
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Karel turns to its right side.
    """
    for i in range(3):
        turn_left()
        

if __name__ == '__main__':
    execute_karel_task(main)
