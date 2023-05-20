import math
import turtle

# draw the circle using turtle
def drawCircleTurtle(x, y, r):
    # move to the start of circle
    turtle.up() #"takes pen off virtual paper" i.e. so it doesnt draw whilst pen is moved
    turtle.setpos(x + r, y)
    turtle.down() #puts "pen" down again 
    
    # draw the circle
    for i in range(0, 365, 5): #0 to 360 in steps of 5
        #i will be the angle parameter passed to parametric equation
        a = math.radians(i) #convert from degrees to radians
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a)) #will draw line from old to new position
    
drawCircleTurtle(100, 100, 50)
 #keeps the tkinter window open so can see the circle
 #tkinter is the default GUI library used by python 
turtle.mainloop()