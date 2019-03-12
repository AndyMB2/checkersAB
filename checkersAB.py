# checkers by Andy B

from graphics import *

def draw_sq(sY, sX, sqSize, color, win):
    square = Rectangle(Point(sX, sY), Point(sX + sqSize, sY + sqSize))
    square.setFill(color)
    square.draw(win)

  
