from xturtle import *
import math

def f(x):
    return x**4/4.0 - x**3/3.0 - 3 * x**2

def main():
    t = Turtle()
    t.setWorldCoordinates(-20,-20,20,20)

    t.penup()
    t.goto(-20,0)
    t.pendown()
    t.goto(20,0)
    t.penup()
    t.goto(0,20)
    t.pendown()
    t.goto(0,-20)
    t.penup()
    t.goto(-10,f(-10))
    t.pendown()
    
    for k in range(-1000,1000):
        x = k / 100.0
        t.goto(x,f(x))

    t.exitOnClick()

main()
