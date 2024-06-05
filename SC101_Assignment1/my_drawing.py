"""
File: my_drawing.py
Name: Jessie
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: My Favorite Character
    This is my favorite cartoon: The Powerpuff Girls.
    I hope that in the process of learning Python,
    I can be as smart and fearless as them, and move towards my goals.
    """
    window = GWindow(width=600, height=600, title='The Powerpuff Girls')

    knot = GPolygon()
    knot.add_vertex((230, 40))
    knot.add_vertex((200, 200))
    knot.add_vertex((350, 200))
    window.add(knot)
    knot.color = 'black'
    knot.filled = True
    knot.fill_color = ('red')

    knot2 = GPolygon()
    knot2.add_vertex((370, 40))
    knot2.add_vertex((260, 200))
    knot2.add_vertex((400, 200))
    window.add(knot2)
    knot2.color = 'black'
    knot2.filled = True
    knot2.fill_color = ('red')

    knot3 = GRect(65, 40, x=270, y=90)
    window.add(knot3)
    knot3.filled = True
    knot3.fill_color = 'red'

    longhair = GPolygon()
    longhair.add_vertex((295, 100))
    longhair.add_vertex((190, 470))
    longhair.add_vertex((420, 470))
    window.add(longhair)
    longhair.color = 'black'
    longhair.filled = True
    longhair.fill_color = ('darkorange')

    r_leg = GOval(35, 150, x=300, y=380)
    window.add(r_leg)
    r_leg.filled = True
    r_leg.fill_color = ('white')


    body = GRect(80, 150, x=260, y=310)
    window.add(body)
    body.filled = True
    body.fill_color = 'lightcoral'

    cloth = GRect(80, 40, x=260, y=390)
    window.add(cloth)
    cloth.filled = True
    cloth.fill_color = 'black'

    l_leg = GOval(33, 80, x=258, y=420)
    window.add(l_leg)
    l_leg.filled = True
    l_leg.fill_color = ('white')

    l_shoe = GRect(30, 7, x=260, y=470)
    window.add(l_shoe)
    l_shoe.filled = True
    l_shoe.fill_color = 'black'

    r_shoe = GRect(25, 7, x=305, y=500)
    window.add(r_shoe)
    r_shoe.filled = True
    r_shoe.fill_color = 'black'

    r_hand = GOval(25, 200, x=400, y=60)
    window.add(r_hand)
    r_hand.filled = True
    r_hand.fill_color = ('navajowhite')

    l_hand = GOval(200, 25, x=120, y=300)
    window.add(l_hand)
    l_hand.filled = True
    l_hand.fill_color = ('navajowhite')

    face = GOval(300, 270, x=150, y=100)
    window.add(face)
    face.filled = True
    face.fill_color = ('navajowhite')

    hair = GOval(275, 165, x=162, y=100)
    window.add(hair)
    hair.filled = True
    hair.fill_color = ('darkorange')

    cover_rect = GRect(hair.width, hair.height/1.5)
    cover_rect.color = 'navajowhite'
    cover_rect.filled = True
    cover_rect.fill_color = 'navajowhite'
    window.add(cover_rect, x=162, y=180)

    tri = GPolygon()
    tri.add_vertex((180, 200))
    tri.add_vertex((220, 150))
    tri.add_vertex((230, 200))
    window.add(tri)
    tri.color = 'navajowhite'
    tri.filled = True
    tri.fill_color = ('navajowhite')


    tri2 = GPolygon()
    tri2.add_vertex((265, 200))
    tri2.add_vertex((300, 145))
    tri2.add_vertex((330, 200))
    window.add(tri2)
    tri2.color = 'navajowhite'
    tri2.filled = True
    tri2.fill_color = ('navajowhite')

    tri3 = GPolygon()
    tri3.add_vertex((350, 200))
    tri3.add_vertex((370, 155))
    tri3.add_vertex((390, 200))
    window.add(tri3)
    tri3.color = 'navajowhite'
    tri3.filled = True
    tri3.fill_color = ('navajowhite')


    l1_eye = GOval(140, 140, x=150, y=175)
    window.add(l1_eye)
    l1_eye.filled = True
    l1_eye.fill_color = 'white'
    l2_eye = GOval(120, 120, x=170, y=185)
    window.add(l2_eye)
    l2_eye.filled = True
    l2_eye.fill_color = 'lightcoral'
    l3_eye = GOval(100, 100, x=190, y=195)
    window.add(l3_eye)
    l3_eye.filled = True
    l3_eye.fill_color = 'black'
    l4_eye = GOval(40, 40, x=220, y=225)
    window.add(l4_eye)
    l4_eye.filled = True
    l4_eye.fill_color = 'white'


    r1_eye = GOval(140, 140, x=310, y=175)
    window.add(r1_eye)
    r1_eye.filled = True
    r1_eye.fill_color = 'white'
    r2_eye = GOval(120, 120, x=310, y=185)
    window.add(r2_eye)
    r2_eye.filled = True
    r2_eye.fill_color = 'lightcoral'
    r3_eye = GOval(100, 100, x=310, y=195)
    window.add(r3_eye)
    r3_eye.filled = True
    r3_eye.fill_color = 'black'
    r4_eye = GOval(40, 40, x=330, y=225)
    window.add(r4_eye)
    r4_eye.filled = True
    r4_eye.fill_color = 'white'

    mouth = GArc(40, 80, 0, -180)
    window.add(mouth, x=280, y=300)

    label = GLabel('SC101')
    label.font = 'Courier-15-italic'
    label.color = 'white'
    window.add(label, x=270, y=423)




if __name__ == '__main__':
    main()
