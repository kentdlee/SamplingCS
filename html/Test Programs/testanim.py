from xturtle import *

running = True
turtle = Turtle()

def f():
    if True:
        turtle.fd(50)
        turtle.lt(60)
        turtle.onTimer(f, 250)

f()   ### makes the turtle marching around
turtle.exitOnClick()
mainloop()
