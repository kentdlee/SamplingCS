from xturtle import *

t = Turtle()
t.fillcolor("red")
t.begin_fill()
for k in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()
t.exitOnClick()

