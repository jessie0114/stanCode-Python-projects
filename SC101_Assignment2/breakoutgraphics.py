"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window_width/2-ball_radius, y=self.window_height/2-ball_radius)

        # Default initial velocity for the ball
        self.dx = 0
        self.dy = 0
        self.ball_at_origin = True
        self.game_running = False

        # Initialize our mouse listeners
        onmouseclicked(self.drop_ball)
        onmousemoved(self.change_position)

        # Draw bricks
        for row in range(brick_rows):
            for col in range(brick_cols):
                self.brick_x = col * (brick_width+brick_spacing)
                self.brick_y = brick_offset + row * (brick_height+brick_spacing)
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                if row < 2:
                    self.brick.color = 'Red'
                    self.brick.fill_color = 'Red'
                elif 2 <= row <= 3:
                    self.brick.color = 'Orange'
                    self.brick.fill_color = 'Orange'
                elif 4 <= row <= 5:
                    self.brick.color = 'Yellow'
                    self.brick.fill_color = 'Yellow'
                elif 6 <= row <= 7:
                    self.brick.color = 'Green'
                    self.brick.fill_color = 'Green'
                else:
                    self.brick.color = 'Blue'
                    self.brick.fill_color = 'Blue'
                self.window.add(self.brick, x=self.brick_x, y=self.brick_y)

        # Create score panel
        self.live = 0
        self.live_panel = GLabel(f'Lives: {self.live}', x=0, y=self.window.height)
        self.live_panel.font = 'Calibri-20'
        self.window.add(self.live_panel)

    def change_position(self, event):
        new_x = event.x - PADDLE_WIDTH / 2
        if new_x < 0:
            new_x = 0
        elif new_x > self.window.width - PADDLE_WIDTH:
            new_x = self.window.width - PADDLE_WIDTH
        self.paddle.x = new_x

    def drop_ball(self, event):
        if self.ball_at_origin and not self.game_running:
            self.set_ball_velocity()
            self.game_running = True

    def set_ball_velocity(self):
        self.ball_at_origin = False
        self.dx = random.randint(1, MAX_X_SPEED)
        self.dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.dx = -self.dx

    def update_ball_position(self):
        if self.game_running:
            self.ball.move(self.dx, self.dy)
            # Check for collision with walls
            if self.ball.y <= 0:
                self.dy = -self.dy
            if self.ball.x + self.ball.width >= self.window.width or self.ball.x <= 0:
                self.dx = -self.dx
            # Check for collision with paddle
            if self.ball.y + self.ball.height >= self.paddle.y and self.ball.x + self.ball.width >= self.paddle.x and self.ball.x <= self.paddle.x + self.paddle.width:
                self.dy = -self.dy
            # Check for collision with bricks
            self.check_collisions()
            # Reset ball if it goes below the paddle -> Write in main function

    def game_over(self):
        game_over_label = GLabel('Game Over')
        game_over_label.font = 'Calibri-40'
        game_over_label.color = 'red'
        self.window.add(game_over_label, (self.window.width - game_over_label.width) / 2, self.window.height / 2)
        onmouseclicked(None)

    def check_collisions(self):
        for dx in [0, self.ball.width]:
            for dy in [0, self.ball.height]:
                corner_x = self.ball.x + dx
                corner_y = self.ball.y + dy
                obj = self.window.get_object_at(corner_x, corner_y)
                if obj is not None:
                    if obj is self.paddle:
                        if self.dy > 0:
                            self.dy = -self.dy
                    elif obj is not self.ball and obj is not self.live_panel:
                        self.window.remove(obj)
                        self.dy = -self.dy
                        if not self.has_bricks_left():
                            self.win_game()
                        return

    def reset_ball(self):
        self.ball.x = self.window_width / 2 - BALL_RADIUS
        self.ball.y = self.window_height / 2 - BALL_RADIUS
        self.dx = 0
        self.dy = 0
        self.ball_at_origin = True
        self.game_running = False

    def set_live(self, live):
        self.live = live
        self.live_panel.text = f'Lives: {self.live}'

    def has_bricks_left(self):
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                brick_x = col * (BRICK_WIDTH + BRICK_SPACING)
                brick_y = BRICK_OFFSET + row * (BRICK_HEIGHT + BRICK_SPACING)
                if self.window.get_object_at(brick_x, brick_y) is not None:
                    return True
        return False

    def win_game(self):
        win_label = GLabel('You Win!')
        win_label.font = 'Calibri-40'
        win_label.color = 'green'
        self.window.add(win_label, (self.window.width - win_label.width) / 2, self.window.height / 2)
        self.game_running = False
        onmouseclicked(None)
