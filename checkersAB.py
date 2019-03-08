# checkers by Andy B

from graphics import *

sqrSz = 50

chkWin = GraphWin("Checkers", sqrSz * 10, sqrSz * 10)
chkWin.setCoords(0, 0, sqrSz * 10, sqrSz * 10)

for i in range(8):
    sqr = Rectangle(Point(sqrSz * (i + 1), sqrSz * 1), Point(sqrSz * (i + 2), sqrSz * 2))
    sqr.draw(chkWin)
