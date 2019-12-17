from xturtle import *
import random
from card import *

screenMaxX = 500
screenMaxY = 500
screenMinX = 0
screenMinY = 0

# This is the class Button. The comments below will tell you how a class
# is written. Classes contain both data and functions. Functions are often
# called methods when they are part of a class. Each of the methods of a 
# class operate on the data of one of the objects in the class. 

class Button:
      # Everything indented inside the class is part of the class. A 
      # class definition consists of the methods of the class. Each method 
      # in a class operates on the data of the class. 

      # The __init__ method is called the CONSTRUCTOR. The constructor
      # is responsible for initializing the object's data. The object is 
      # pointed to by the self reference. So, data is put in the object by 
      # writing 
      #   self.variable = value
      # Each time you see a line like that below a value is being 
      # stored in the object. In this case a Button object stores quite 
      # a bit of information including the button's text, its location on the
      # screen, the width and height of the button, and a reference to the
      # handler. The handler is called when the button was pressed. 

      def __init__(self, turtle, text, x, y, width, height, handler):
            self.turtle = turtle
            self.text = text
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.handler = handler
            self.__draw__()

      # This is a special method because the name begins with a underscore. 
      # Names that begin with underscores are generally not suppose to be 
      # called from outside the class. This method is called by __init__ only.
      def __draw__(self):
            # To access the data in the button object, the self reference
            # is used. So, self.turtle refers to the turtle that was stored
            # in the object in the constructor above.
            self.turtle.penup()
            self.turtle.goto(self.x, self.y)
            self.turtle.setheading(0)
            self.turtle.pendown()
            self.turtle.forward(self.width)
            self.turtle.left(90)
            self.turtle.forward(self.height)
            self.turtle.left(90)
            self.turtle.forward(self.width)
            self.turtle.left(90)
            self.turtle.forward(self.height)
            self.turtle.left(90)
            self.turtle.penup()
            self.turtle.forward(self.width/2)
            self.turtle.pendown()
            self.turtle.write(self.text,align="center",font=('Arial',24,"bold"))
         

   
      # The isInside method checks that the x and y passed to the method
      # are inside the button. If they are, then true is returned. False 
      # otherwise. x and y are checked against the x,y,width, and height
      # that are stored in the object. Everytime you see self.x or 
      # self.width it is the value that was stored in the object at some
      # earlier time. The isInside method is an accessor method. It 
      # accesses the data of the button object and tells us something 
      # about it.
      def isInside(self,x,y):
            return self.x <= x <= self.x+self.width and \
               self.y <= y <= self.y+self.height
               
      # wasPressed is the method that is called when it is determined that
      # a previous mouse click was inside the button. It responds by 
      # doing a callback to the button handler. A callback is a function
      # that is waiting to be called until later. The callback called 
      # handler was passed in on the constructor to the object.
      def wasPressed(self):
            self.handler()    

class ColorButton(Button):
      def __init__(self, turtle, text, x, y, width, height, handler, fgcolor, bgcolor):
            self.bgcolor = bgcolor
            self.fgcolor = fgcolor
            Button.__init__(self, turtle, text, x, y, width, height, handler)

      def __draw__(self):
            self.turtle.penup()
            self.turtle.color(self.fgcolor)
            self.turtle.goto(self.x, self.y)
            self.turtle.setheading(0)
            self.turtle.pendown()
            self.turtle.fillcolor(self.bgcolor)
            self.turtle.begin_fill()
            self.turtle.forward(self.width)
            self.turtle.left(90)
            self.turtle.forward(self.height)
            self.turtle.left(90)
            self.turtle.forward(self.width)
            self.turtle.left(90)
            self.turtle.forward(self.height)
            self.turtle.left(90)
            self.turtle.end_fill()
            self.turtle.penup()
            self.turtle.forward(self.width/2)
            self.turtle.pendown()
            self.turtle.write(self.text,align="center",font=('Arial',24,"bold"))

def shuffle(cards):

      for k in range(len(cards)):
            j = randrange(len(cards))
            
            i = cards[k]
            #i.goto(100,300)
            cards[k] = cards[j]
            cards[j] = i
            
def deal(cards,piles):
      start = 0
      for k in range(7):
            for m in range(k,7):
                  card = cards.pop()
                  card.goto(100+100*m,600-start*20)
                  if m == k:
                        card.setFaceUp()

                  piles[m].append(card)

            start = start + 1

def drawPile(piles,pileIndex):
      for k in range(len(piles[pileIndex])):
            card = piles[pileIndex][k]
            card.goto(100+100*pileIndex,600-k*20)

def moveCards(fromPile,toPile,piles):
      print "In move cards"
      toRank = piles[toPile][-1].getRank()
      print toRank
      toColor = piles[toPile][-1].getColor()
      print toColor
      for k in range(len(piles[fromPile])):
            if not piles[fromPile][k].isFaceDown():
                  print "considering"
                  print piles[fromPile][k].getRank()
                  print piles[fromPile][k].getColor()
                  if piles[fromPile][k].getRank() == toRank - 1 and piles[fromPile][k].getColor() <> toColor:
                        print "found spot to move to"
                        print "fromIndex is",k

                        lst = piles[fromPile][k:]
                        del piles[fromPile][k:]
                        piles[toPile].extend(lst)
                        drawPile(piles,toPile)
                        if len(piles[fromPile]) > 0:
                              piles[fromPile][-1].setFaceUp()
                        return


def main():
      global fromClicked, fromPile
    
      t = Turtle()
      t.ht()
      t.setWorldCoordinates(0,0,800,800)
      t.winsize(850,650,20,20)
      t.tracer(10)

      buttonList = []
      
      def quitHandler():
            print "Good Bye"
            t.bye()

      quitButton = Button(t,"Quit",360,20,80,40,quitHandler)
      buttonList.append(quitButton)

      fromClicked = False
      fromPile = 0

      def pile0Handler():
            global fromClicked, fromPile
            print "Pile 0"
            if not fromClicked:
                  fromClicked = True
                  fromPile = 0
            else:
                  fromClicked = False
                  moveCards(fromPile,0,piles)

      def pile1Handler():
            global fromClicked, fromPile
            print "Pile 1"
            if not fromClicked:
                  fromClicked = True
                  fromPile = 1
            else:
                  fromClicked = False
                  moveCards(fromPile,1,piles)

      def pile2Handler():
            global fromClicked, fromPile
            print "Pile 2"
            if not fromClicked:
                  fromClicked = True
                  fromPile = 2
            else:
                  fromClicked = False
                  moveCards(fromPile,2,piles)

      def pile3Handler():
            global fromClicked, fromPile
            print "Pile 3"
            if not fromClicked:
                  fromClicked = True
                  fromPile = 3
            else:
                  fromClicked = False
                  moveCards(fromPile,3,piles)

      def pile4Handler():
            global fromClicked, fromPile
            print "Pile 4"
            if not fromClicked:
                  fromClicked = True
                  fromPile = 4
            else:
                  fromClicked = False
                  moveCards(fromPile,4,piles)

      def pile5Handler():
            global fromClicked, fromPile
            print "Pile 5"
            if not fromClicked:
                  fromClicked = True
                  fromPile = 5
            else:
                  fromClicked = False
                  moveCards(fromPile,5,piles)

      def pile6Handler():
            global fromClicked, fromPile
            print "Pile 6"
            if not fromClicked:
                  fromClicked = True
                  fromPile = 6
            else:
                  fromClicked = False
                  moveCards(fromPile,6,piles)

      pile1Button = ColorButton(t,"Pile0",50,375,100,300,pile0Handler,"white","white")
      buttonList.append(pile1Button)

      pile1Button = ColorButton(t,"Pile1",150,375,100,300,pile1Handler,"white","white")
      buttonList.append(pile1Button)

      pile1Button = ColorButton(t,"Pile2",250,375,100,300,pile2Handler,"white","white")
      buttonList.append(pile1Button)

      pile1Button = ColorButton(t,"Pile3",350,375,100,300,pile3Handler,"white","white")
      buttonList.append(pile1Button)

      pile1Button = ColorButton(t,"Pile4",450,375,100,300,pile4Handler,"white","white")
      buttonList.append(pile1Button)

      pile1Button = ColorButton(t,"Pile5",550,375,100,300,pile5Handler,"white","white")
      buttonList.append(pile1Button)

      pile1Button = ColorButton(t,"Pile6",650,375,100,300,pile6Handler,"white","white")
      buttonList.append(pile1Button)

      cards = [] 

      for k in range(52):
            aCard = Card(k,"cards/"+str(k+1)+".gif","cards/back.gif")
            aCard.speed(0)
            aCard.delay(3)
            aCard.goto(100,750)
            cards.append(aCard)

      shuffle(cards)

      piles = [[],[],[],[],[],[],[]]

      t.tracer(1)

      deal(cards,piles)

      # Finally, this mouseHandler is needed by Turtle graphics
      # to respond to mouse clicks. 
      def mouseHandler(x,y):
            # Each time the mouse is clicked, the click is 
            # checked to see if it was inside the button. If so,
            # then the wasPressed method is called. To call a method
            # on an object we write
            # objectReference.method(<Parameters to Method>)
            for button in buttonList:
                  if button.isInside(x,y):
                        button.wasPressed()


      t.onClick(mouseHandler)

 
main()
mainloop()

      
    
