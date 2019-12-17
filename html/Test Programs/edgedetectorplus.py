from image import *

def negative(myImage):
    newImage = EmptyImage(myImage.getWidth(), myImage.getHeight())

    for row in range(myImage.getHeight()):
      for col in range(myImage.getWidth()):
        r,g,b = myImage.getPixel(col,row)
        r = 255-r
        g = 255-g
        b = 255-b
        newImage.setPixel(col,row,(r,g,b))
	         
    return newImage

def convolve(myImage, row, col,M):
    numRows = len(M)
    numCols = len(M[0])
    
    halfMHeight = numRows/2
    halfMWidth = numCols/2
    
    if row < halfMHeight:
        return 0
    if myImage.getHeight()-row-1 < halfMHeight:
        return 0
    if col < halfMWidth:
        return 0
    if myImage.getWidth()-col-1 < halfMWidth:
        return 0

    val = 0
    
    for y in range(numRows):
        for x in range(numCols):
           r,g,b = myImage.getPixel(col-halfMWidth+x,row-halfMHeight+y)
           avg = (r+g+b)/3.0
           val = val + avg * M[y][x]

    return int(val)
    

def edgeDetect(myImage):
    Gx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    Gy = [[1,2,1],[0,0,0],[-1,-2,-1]]
    
    newImage = EmptyImage(myImage.getWidth(), myImage.getHeight())
    for row in range(myImage.getHeight()):
      for col in range(myImage.getWidth()):
        xGradient = convolve(myImage,row,col,Gx)
        yGradient = convolve(myImage,row,col,Gy)

        val = abs(xGradient) + abs(yGradient)

        if val > 255:
            val = 255

        if val < 0:
            val = 0

        newImage.setPixel(col,row,(val,val,val))
	         
    return negative(newImage)

def laplacian(myImage):
    L = [[-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1],
         [-1,-1,24,-1,-1],
         [-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1]]
    
    newImage = EmptyImage(myImage.getWidth(), myImage.getHeight())
    for row in range(myImage.getHeight()):
      for col in range(myImage.getWidth()):
        val = abs(convolve(myImage,row,col,L))

        if val > 255:
            val = 255

        if val < 0:
            val = 0

        newImage.setPixel(col,row,(val,val,val))
	         
    return negative(newImage)

def main():
    print "This is the image transformation program."
    
    filename = raw_input("Please enter the name of an image:")
  
    myImage = FileImage(filename)
	
    choice = 0
	
    while choice <> 5:
	  
        win = ImageWin("Image Transformer",myImage.getWidth(),myImage.getHeight())
        myImage.draw(win)

        print "Pick from the following menu:"
        print "1) Convert to Negative"
        print "2) Sobel Edge Detect"
        print "3) Laplacian Edge Detect"
        print "4) Save Image"
        print "5) Quit"
      
        choice = input("Please enter your choice: ")
      
        if choice == 1:
            myImage = negative(myImage)
        elif choice == 2:
            myImage = edgeDetect(myImage)
        elif choice == 3:
            myImage = laplacian(myImage)
        elif choice == 4:
            filename = raw_input("Please enter the name to save it as:")
            myImage.save(filename)

        win.close()

main()
