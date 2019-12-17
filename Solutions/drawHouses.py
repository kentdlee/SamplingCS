from xturtle import *
import random

def drawHouse(t,x,y,scale):

    t.ht()

    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.pendown()

    t.forward(200*scale)
    t.left(90)
    t.forward(200*scale)
    t.left(90)
    t.forward(200*scale)
    t.left(90)
    t.forward(200*scale)


    t.left(90)
    t.forward(170*scale)
    t.left(90)
    t.forward(148*scale)
    t.left(90)
    t.forward(66*scale)
    t.left(90)
    t.forward(148*scale)
    

    t.penup()
    t.left(90)
    t.forward(21*scale)
    t.left(90)
    t.forward(66*scale)
    t.pendown()
    t.circle(4*scale)
    t.penup()

    t.goto(x,y)
    t.right(90)
    t.forward(80*scale)
    t.left(90)
    t.forward(66*scale)


    t.pendown() 
    t.forward(66*scale)
    t.left(90)
    t.forward(66*scale)
    t.left(90)
    t.forward(66*scale)
    t.left(90)
    t.forward(66*scale)
    t.left(90)
    t.forward(33*scale)
    t.left(90)
    t.forward(66*scale)
    t.right(90)
    t.forward(33*scale)
    t.right(90)
    t.forward(33*scale)
    t.right(90)
    t.forward(66*scale)
    t.penup()

    t.goto(x,y)
    t.left(180)
    t.forward(200*scale)
    
    t.pendown()
    t.right(45)
    t.forward(142*scale)
    t.right(90)
    t.forward(141*scale)
    t.penup()


def main():
    global size
    size = 200
    t = Turtle()
    t.setWorldCoordinates(0,0,800,800)


    for k in range(10):
        x = random.random()*600
        y = random.random()*400
        scale = random.random()
        drawHouse(t,x,x,scale)

    t.exitOnClick()


main()

