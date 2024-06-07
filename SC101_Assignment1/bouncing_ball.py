"""
File: bouncing_ball.py
Name: Jessie
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
MAX_BOUNCES = 3

window = GWindow(800, 500, title='bouncing_ball.py')

ball = GOval(SIZE, SIZE)
ball.filled = True

ball.x = START_X
ball.y = START_Y
vx = VX
vy = GRAVITY
bounces = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball)
    onmouseclicked(drop_ball)

ball_at_origin = True

def drop_ball(event):
    """
    This function starts the bouncing process if the mouse
    is clicked for the 1st time and the process is executed
    less than or equal three times.
    """
    global bounces, ball_at_origin
    if ball_at_origin and bounces < MAX_BOUNCES:
        animate_ball()


def reset_ball():
    global bounces, vx, vy, ball_at_origin
    ball.x = START_X
    ball.y = START_Y
    vx = VX
    vy = GRAVITY
    ball_at_origin = True


def animate_ball():
    """
    This function stimulates the bouncing process of the ball.
    """
    global vx, vy, bounces, ball_at_origin
    ball_at_origin = False
    while True:
        vy += GRAVITY
        ball.move(vx, vy)
        if ball.y + SIZE >= window.height:
            vy = -vy * REDUCE
            ball.y = window.height - SIZE
        if ball.x + SIZE >= window.width:
            reset_ball()
            bounces += 1
            return
        pause(DELAY)


if __name__ == "__main__":
    main()
