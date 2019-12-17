from xturtle import *
import math

def f(x):
    return 2 * math.sin(x)

def main():
    t = Turtle()
    t.setWorldCoordinates(-10,-10,10,10)

    t.penup()
    t.goto(-10,0)
    t.pendown()
    t.goto(10,0)
    t.penup()
    t.goto(0,10)
    t.pendown()
    t.goto(0,-10)
    t.penup()
    t.goto(-10,f(-10))
    t.pendown()
    
    for k in range(-1000,1000):
        x = k / 100.0
        t.goto(x,f(x))

    t.exitOnClick()

main()
