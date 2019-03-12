# checkers by Andy B

from graphics import *

def draw_sq(sY, sX, sqSize, color, win):
    square = Rectangle(Point(sX, sY), Point(sX + sqSize, sY + sqSize))
    square.setFill(color)
    square.draw(win)

sqrSz = 50
sqCol = "red"

chkWin = GraphWin("Checkers", sqrSz * 10, sqrSz * 10)
chkWin.setCoords(0, 0, sqrSz * 10, sqrSz * 10)

for j in range(8):
    for i in range(8):
        if(i + j) % 2 == 0:
            sqCol = "red"
        else:
            sqCol = "black"
        draw_sq(sqrSz * (i + 1), sqrSz * (j + 1), sqrSz, sqCol, chkWin)

