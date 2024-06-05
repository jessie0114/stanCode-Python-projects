"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3           # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.set_live(lives)
    while True:
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            graphics.set_live(lives)
            if lives > 0:
                graphics.reset_ball()
            else:
                graphics.game_over()
                break
        pause(FRAME_RATE)
        graphics.ball.move(graphics.dx, graphics.dy)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.dx = -graphics.dx
        if graphics.ball.y <= 0:
            graphics.dy = -graphics.dy
        graphics.update_ball_position()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
