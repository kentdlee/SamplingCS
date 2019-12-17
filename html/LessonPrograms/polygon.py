from xturtle import *

sides = 6
t = Turtle()
t.fillcolor("red")
t.begin_fill()
for k in range(3):
  t.forward(100)
  t.left(120)
t.end_fill()
t.exitOnClick()
