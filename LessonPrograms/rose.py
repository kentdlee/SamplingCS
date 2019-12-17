from xturtle import *
import math


t = Turtle()
t.setWorldCoordinates(-500,-500,500,500)

t.penup()
t.goto(100,0)
t.pendown()
t.ht()

for i in range(1000):

    theta = (i / 1000.0) * math.pi * 2
    r = 100 * math.cos(2 * theta)

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    t.goto(x,y)

t.exitOnClick()
