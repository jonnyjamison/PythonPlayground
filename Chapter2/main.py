import sys, random, argparse
import turtle
from Spiro import Spiro
from SpiroAnimator import SpiroAnimator


#def main():
# main() function
# use sys.argv if needed
print('generating spirograph...')
# create parser
descStr = """This program draws Spirographs using the Turtle module.
When run with no arguments, this program draws random Spirographs.

Terminology:
R: radius of outer circle
r: radius of inner circle
l: ratio of hole distance to r
"""
parser = argparse.ArgumentParser(description=descStr)

# add expected arguments
parser.add_argument('--sparams', nargs=3, dest='sparams', required=False,
    help="The three arguments in sparams: R, r, l.")

# parse args
args = parser.parse_args()

# set the width of the drawing window to 80 percent of the screen width
turtle.setup(width=0.8)

# set the cursor shape to turtle
turtle.shape('turtle')

# set the title to Spirographs!
turtle.title("Spirographs!")
# add the key handler to save our drawings
#turtle.onkey(SpiroAnimator.saveDrawing(), "s")
# start listening
turtle.listen()

# hide the main turtle cursor
turtle.hideturtle()

# check for any arguments sent to --sparams and draw the Spirograph
if args.sparams:
    params = [float(x) for x in args.sparams]
    # draw the Spirograph with the given parameters
    col = (0.0, 0.0, 0.0)
    spiro = Spiro(0, 0, col, *params)
    spiro.draw()
else:
    # create the animator object
    spiroAnim = SpiroAnimator(4)
    # add a key handler to toggle the turtle cursor
    turtle.onkey(spiroAnim.toggleTurtles, "t")
    # add a key handler to restart the animation
    turtle.onkey(spiroAnim.restart, "space")

# start the turtle main loop
turtle.mainloop()
    
# call main
#if __name__ == '__main__':
    #main()