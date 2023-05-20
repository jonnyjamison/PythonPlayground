from Spiro import Spiro 
import random
import turtle
from PIL import Image
from datetime import datetime

# a class for animating Spirographs
class SpiroAnimator:
    # constructor
    def __init__(self, N):
        # set the timer value in milliseconds
        self.deltaT = 10
        # get the window dimensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        # empty array into which Spiro objects will be placed 
        self.spiros = []
        for i in range(N):
            # generate random parameters
            rparams = self.genRandomParams() #call to method created below 
            # set the spiro parameters
            spiro = Spiro(*rparams) # *converts tuple into a list of arguements 
            self.spiros.append(spiro)

        # call timer
        turtle.ontimer(self.update, self.deltaT) # will call update every deltaT seconds
        
             
    def genRandomParams(self):
        # generate random parameters
        width, height = self.width, self.height
        R = random.randint(50, min(width, height)//2)
        r = random.randint(10, 9*R//10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width//2, width//2)
        yc = random.randint(-height//2, height//2)
        col = (random.random(),
            random.random(),
            random.random())
        return (xc, yc, col, R, r, l) # notice this is a TUPLE 
    
    
    def restart(self):
    # restart spiro drawing
        for spiro in self.spiros:
            # clear
            spiro.clear()
            # generate random parameters
            rparams = self.genRandomParams()
            # set the spiro parameters
            spiro.setparams(*rparams)
            # restart drawing
            spiro.restart()
            
            
    def update(self):
        # called by constructor
        nComplete = 0
        for spiro in self.spiros: # loops through all spiro objects
            # update
            spiro.update()
            # count completed spiros
            if spiro.drawingComplete:
                nComplete += 1
        # restart if all spiros are complete
        if nComplete == len(self.spiros): 
            self.restart()
        # call the timer
        turtle.ontimer(self.update, self.deltaT)
        
        
    def toggleTurtles(self):
        # toggle turtle cursor on and off
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()
                
                


    def saveDrawing():
        # hide the turtle cursor
        turtle.hideturtle()
        # generate unique filenames
        dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
        fileName = 'spiro-' + dateStr
        print('saving drawing to %s.eps/png' % fileName)
        # get the tkinter canvas
        canvas = turtle.getcanvas()
        # save the drawing as a postscipt image
        canvas.postscript(file = fileName + '.eps')
        # use the Pillow module to convert the poscript image file to PNG
        img = Image.open(fileName + '.eps')
        img.save(fileName + '.png', 'png')
        # show the turtle cursor
        turtle.showturtle()