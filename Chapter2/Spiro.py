import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime
from math import gcd 

class Spiro:
    # a class that draws a Spirograph

    # constructor
    def __init__(self, xc, yc, col, R, r, l):
        # create the turtle object
        self.t = turtle.Turtle() #this is used so that multiple spiros can be drawn at once 
        # set the cursor shape to a turtle (other choices are available)
        self.t.shape('turtle') 
        # set the step in degrees
        self.step = 5
        # set the drawing complete flag
        self.drawingComplete = False
        # set the parameters - used in other methods 
        self.setparams(xc, yc, col, R, r, l)
        # initialize the drawing
        self.restart()
        
    # set the parameters
    def setparams(self, xc, yc, col, R, r, l):
        # the Spirograph parameters
        # coords of center of curve
        self.xc = xc 
        self.yc = yc
        # convert to integers
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        # reduce r/R to its smallest form by dividing with the GCD
        # gcd = greatest common denominator
        gcdVal = gcd(self.r, self.R)
        # periodicity of curve
        self.nRot = self.r//gcdVal
        # get ratio of radii
        self.k = r/float(R)
        # set the color
        self.t.color(*col)
        # store the current angle
        self.a = 0
        
        
    # restart the drawing
    def restart(self):
        # set the flag
        self.drawingComplete = False #allows to keep track of multiple spiros
        # show the turtle
        self.t.showturtle() # in case it is hidden 
        # go to the first point
        self.t.up()
        R, k, l = self.R, self.k, self.l
        a = 0.0 # to compute starting position with an angle of 0 
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down() # puts pen down again 
        
    # draw the whole thing
    def draw(self):
        # draw the rest of the points
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360*self.nRot + 1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc + x, self.yc + y)
        # drawing is now done so hide the turtle cursor
        self.t.hideturtle()
        
        
    # update by one step
    def update(self):
        # skip the rest of the steps if done
        if self.drawingComplete:
            return

        # increment the angle
        self.a += self.step
        # draw a step
        R, k, l = self.R, self.k, self.l
        # set the angle
        a = math.radians(self.a)
        x = self.R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = self.R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
        # if drawing is complete, set the flag
        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            # drawing is now done so hide the turtle cursor
            self.t.hideturtle()