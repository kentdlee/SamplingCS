from xturtle import *
import random

def drawSquare(t,x,y,scale,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    t.forward(100*scale)
    t.left(90)
    t.forward(100*scale)
    t.left(90)
    t.forward(100*scale)
    t.left(90)
    t.forward(100*scale)
    t.end_fill()

def main():
    turtle = Turtle()
    turtle.setWorldCoordinates(0,0,800,800)
    
    for k in range(100):
        x = random.random() * 600
        y = random.random() * 600
        s = random.random()

        drawSquare(turtle,x,y,s,"red")

    turtle.exitOnClick()

main()
