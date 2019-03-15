# checkers by Andy B

from graphics import *

print("""In order to create a checker board please enter a squre size.
This will make the window as big as you set it to be.""")


try:
    sqSz = int(input("Square Sizes: "))
except ValueError:
    sqSz = 50

def draw_tile(tR, tC, color):
    global sqSz
    sqr = Rectangle(Point(sqSz * (tR + 1), sqSz * (tC + 1)),
                   Point(sqSz * (tR + 2), sqSz * (tC + 2)))
    sqr.setFill(color)
    sqr.draw(chWin)

print (""" Please input what color you would like the checkerboard to be.
Your input must be all lower case and no spaces.
Black and Red is the standard color""")

C1 = input ("Color 1: ")
if C1 != "":
    C2 = input ("Color 2: ")
else:
    C1 = "red"
    C2 = "black"

    
chWin = GraphWin ("Checkers", sqSz * 10, sqSz * 10)
chWin.setCoords(0, 0, sqSz * 10, sqSz * 10)

for j in range (8):
    for i in range(8):
        if j % 2 == 0 :
            if i % 2 == 0 :
                sqCol = C1
            else:
                sqCol = C2
        else:
            if i %  2 == 1:
                sqCol = C1
            else:
                sqCol = C2
        draw_tile(i, j, sqCol)
  
chWin.getMouse()
chWin.close()


