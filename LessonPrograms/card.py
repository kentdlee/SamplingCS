from xturtle import *
from random import *

               
class Card(Turtle):
    def __init__(self,val,img,back):
        Turtle.__init__(self)
        self.ht()
        self.val = val
        self.addshape(img)
        self.face = img
        self.addshape(back)
        self.back = back
        self.shape(back)
        self.penup()
        self.faceDown = True
        self.setx(250)
        self.sety(250)
        self.st()

    def getBlackJackRank(self):
        rank = 14 - self.val / 4
        if 10 <= rank <= 13:
            rank = 10
        if rank == 14:
            rank = 11


        return rank

    def getRank(self):
        rank = 14 - self.val / 4 
        if rank == 14:
            rank = 1

        return rank

    def getColor(self):
        suit = self.val % 4

        if suit < 2:
            return "black"
        else:
            return "red"

    def goto(self,x,y):
        if self.faceDown:
            self.shape(self.back)
        else:
            self.shape(self.face)
        Turtle.goto(self,x,y)
        
    def isFaceDown(self):
        return self.faceDown

    def setFaceDown(self):
        self.shape(self.back)
        self.faceDown = True

    def setFaceUp(self):
        self.shape(self.face)
        self.faceDown = False
        

def shuffle(cards):

    for k in range(len(cards)):
        j = randrange(len(cards))

        i = cards[k]
        cards[k] = cards[j]
        cards[j] = i
     


    

    
