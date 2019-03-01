# checkers by Andy B

from graphics import *

sqrSz = 70
sqr = Rectangle(Point(sqrSz * 1, sqrSz * 1), Point(sqrSz * 2, sqrSz * 2))

chkWin = GraphWin("Checkers", sqrSz * 10, sqrSz * 10)
chkWin.setCoords(0, 0, sqrSz * 10, sqrSz * 10) 
sqr.draw(chkWin)
