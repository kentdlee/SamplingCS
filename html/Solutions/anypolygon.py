from xturtle import *

sides = 6
t = Turtle()
t.fillcolor("red")
t.begin_fill()
for k in range(sides):
  t.forward(100)
  t.left(360/sides)
t.end_fill()
t.exitOnClick()
