
import turtle
import time

pointer =turtle.Turtle();
pointer.forward(160)
def tri ():
   for i in range(3):
      pointer.left(120)
      pointer.forward(160)

tri()
pointer.left(120)
pointer.forward(120)
pointer.left(60)
pointer.forward(100)
tri()



turtle.done()