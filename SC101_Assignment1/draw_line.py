"""
File: draw_line.py
Name: Jessie
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
click_count = 0
start_x = 0
start_y = 0
circle = None  # The hollow circle indicating the first click.

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    """
    This function draws a hollow circle centered the mouse at odd
    click, and it draws a line starting with the odd click mouse
    and ending with the next click mouse at even click.
    """
    global click_count, circle, start_x, start_y
    if click_count % 2 == 0:
        if circle is not None:
            window.remove(circle)
        circle = GOval(10, 10)
        circle.filled = False
        window.add(circle, x=event.x-5, y=event.y-5)
        start_x = event.x
        start_y = event.y
    else:
        line = GLine(start_x, start_y, event.x, event.y)
        window.add(line)
        window.remove(circle)
    click_count += 1


if __name__ == "__main__":
    main()
