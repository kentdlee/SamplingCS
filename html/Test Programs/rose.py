import graphics
import math

def main():

    win = graphics.GraphWin("My Window", 500, 500)

    win.setCoords(-250,-250,250,250)

    x = 5
    
    for i in range(1000):

        theta = (i / 1000.0) * math.pi * 2
        r = 100 * math.cos(2 * theta)

        x = r * math.cos(theta)
        y = r * math.sin(theta)

        win.plot(x,y)

main()

        
