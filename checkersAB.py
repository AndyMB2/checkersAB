# checkers by Andy B

from graphics import *

sqrSz = 50

chkWin = GraphWin("Checkers", sqrSz * 10, sqrSz * 10)
chkWin.setCoords(0, 0, sqrSz * 10, sqrSz * 10)

for j in range(8):
    for i in range(8):
        sqr = Rectangle(Point(sqrSz * (i + 1), sqrSz * (j + 1)),
                        Point(sqrSz * (i + 2), sqrSz * (j + 2)))
        sqr.draw(chkWin)
