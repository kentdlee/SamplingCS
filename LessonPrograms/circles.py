from xturtle import *
from math import *

t = Turtle()
sides = 100
radius = 40
circumference = 2 * pi * radius
sideLength = circumference / sides
t.fillcolor("red")
t.begin_fill()
for k in range(sides):
  t.forward(sideLength)
  t.left(360.0/sides)
t.end_fill()
t.exitOnClick()
