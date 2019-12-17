"""
image.py
This module provides a simple interface to create a window, load an image and experiment 
with image based algorithms.  Many of which require pixel-by-pixel manipulation.  This
is a educational module, its not intended to replace the excellent Python Image Library, in fact 
it uses PIL.

The module and its interface and some of the code were inspired/copied by/from John Zelle's graphics.py 
which serves a similar purpose in the graphics primitive world.
"""

# Release Notes:
# Version 1.0   Fall 2005
#
# Version 1.1   December 7, 2005
# Changes:
#   Modify class name for base image to be AbstractImage   This way we don't have a lower case
#      class name running around.  We still don't expect people to create an AbstractImage but
#      rather create an image through FileImage, ListImage, or EmptyImage.
#   Add ability to convert an image to a list
#   Add save function to write an image back to disk.
#


import Tkinter
import Image
import ImageTk


# Borrow some ideas from Zelle
# create an invisible global main root for all windows
tk = Tkinter
_imroot = tk.Tk()
_imroot.withdraw()


class ImageWin(tk.Canvas):
    """
    ImageWin:  Make a frame to display one or more images.
    """
    def __init__(self,title,width,height):        
        """
        Create a window with a title, width and height.
        """
        master = tk.Toplevel(_imroot)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master, width=width, height=height)
        self.master.title(title)
        self.pack()
        master.resizable(0,0)
        self.foreground = "black"
        self.items = []
        self.mouseX = None
        self.mouseY = None
        self.bind("<Button-1>", self._onClick)
        self.height = height
        self.width = width
        self._mouseCallback = None
        self.trans = None
        _imroot.update()

    def close(self):
        """Close the window"""
        self.master.destroy()
        self.quit()
        _imroot.update()
        
    def getMouse(self):
        """Wait for mouse click and return a tuple with x,y position in screen coordinates after
        the click"""
        self.mouseX = None
        self.mouseY = None
        while self.mouseX == None or self.mouseY == None:
            self.update()
        return ((self.mouseX,self.mouseY))

    def setMouseHandler(self, func):
        self._mouseCallback = func

    def _onClick(self, e):
        self.mouseX = e.x
        self.mouseY = e.y
        if self._mouseCallback:
            self._mouseCallback(Point(e.x, e.y)) 
    

class AbstractImage:
    """
    Create an image.  The image may be created in one of four ways:
    1. From an image file such as gif, jpg, png, ppm  for example: i = image('fname.jpb)
    2. From a list of lists
    3. From another image object
    4. By specifying the height and width to create a blank image.
    """
    imageCache = {} # tk photoimages go here to avoid GC while drawn 
    imageId = 1
    def __init__(self,fname=None,data=[],imobj=None,height=0,width=0):
        """
        An image can be created using any of the following keyword parameters. When image creation is 
        complete the image will be an rgb image.
        fname:  A filename containing an image.  Can be jpg, gif, and others
        data:  a list of lists representing the image.  This might be something you construct by
        reading an asii format ppm file, or an ascii art file and translate into rgb yourself.
        imobj:  Make a copy of another image.
        height:
        width: Create a blank image of a particular height and width.
        """
        if fname:
            self.im = Image.open(fname)
            self.imFileName = fname
            ni = self.im.convert("RGB")
            self.im = ni
        elif data:
            height = len(data)
            width = len(data[0])
            self.im = Image.new("RGB",(width,height))
            for row  in range(height):
                for col in range(width):
                    self.im.putpixel((col,row),data[row][col])
        elif height > 0 and width > 0:
            self.im = Image.new("RGB",(width,height))
        elif imobj:
            self.im = imobj.copy()
            
        self.width,self.height = self.im.size
        self.centerX = self.width/2
        self.centerY = self.height/2
        self.id = None

    def copy(self):
        """Return a copy of this image"""
        newI = AbstractImage(imobj=self.im)
        return newI


    def clone(self):
	     """Return a copy of this image"""
	     newI = AbstractImage(imobj=self.im)
	     return newI
        
    def getHeight(self):
        """Return the height of the image"""
        return self.height

    def getWidth(self):
        """Return the width of the iamge"""
        return self.width
        
    def getPixel(self,x,y):
        """Get a pixel at the given x,y coordinate.  The pixel is returned as an rgb color tuple
        for eaxamplle foo.getPixel(10,10) --> (10,200,156) """
        return self.im.getpixel((x,y))
        
    def setPixel(self,x,y,colorTuple):
        """Set the color of a pixel at position x,y.  The color must be specified as an rgb tuple (r,g,b) where 
        the rgb values are between 0 and 255."""
        self.im.putpixel((x,y),colorTuple)
    
    def setPosition(self,x,y):
        """Set the position in the window where the center of this image should be."""
        self.centerX = x
        self.centerY = y
        
    def draw(self,win):
        """Draw this image in the ImageWin window."""
        ig = ImageTk.PhotoImage(self.im)
        self.imageCache[self.imageId] = ig # save a reference else Tk loses it...
        AbstractImage.imageId = AbstractImage.imageId + 1
        self.canvas=win
        self.id = self.canvas.create_image(self.centerX,self.centerY,image=ig)
        _imroot.update()
        
    def save(self,fname=None,type='jpg'):
        if fname == None:
            fname = self.imFileName
        try:
            self.im.save(fname)            
        except:
            print "Error saving, Could Not open ", fname, " to write."

    def toList(self):
        """
        Convert the image to a List of Lists representation
        """
        res = []
        for i in range(self.height):
            res.append([])
            for j in range(self.width):
                res[i].append(self.getPixel(j,i))
        return res


class FileImage(AbstractImage):
	def __init__(self,thefile):
		AbstractImage.__init__(self,fname = thefile)


class EmptyImage(AbstractImage):
	def __init__(self,cols,rows):
		AbstractImage.__init__(self,height = rows, width = cols)
		
class ListImage(AbstractImage):
	def __init__(self,thelist):
		AbstractImage.__init__(self,data=thelist)

# Example program  Read in an image and calulate the negative.
if __name__ == '__main__':
    oImage = FileImage('dog.JPG')
    win = ImageWin("My Window",oImage.getWidth(),oImage.getHeight())
    oImage.draw(win)
    myImage = oImage.copy()

    for row in range(myImage.getHeight()):
        for col in range(myImage.getWidth()):
             v = myImage.getPixel(col,row)
             x = map(lambda x: 255-x, v)
             myImage.setPixel(col,row,tuple(x))
    myImage.setPosition(oImage.getWidth()/2.0,oImage.getHeight()/2.0)         
    myImage.draw(win)
    win.getMouse()
    myImage.save('/Users/leekent/testfoo.jpg')
    #print myImage.toList()
    win.close()


