from tkinter import *
import time

"""
Python has various graphics libraries. You can only use one at a time. Canopy by default uses PyLab. Go into Canopy preferences->Python and UNclick PyLab so this program can work.

This program can always be run in a terminal/command window by saying "python thisFileName.py"
"""


def start():
    """
    Create a new window, and run the function "movingSquare" when return is pressed.
    """

    #movingSquare is defined inside start so that it can see
    # start's variables - what are they?
    def movingSquare(Event):
        r1 = myCanvas.create_rectangle(50, 25, 175, 175, fill="yellow")
        for i in range(38):
            myCanvas.move(r1,2,0)
            time.sleep(.01)
            myCanvas.update()
        for i in range(51):
            myCanvas.move(r1,0,2)
            time.sleep(.01)
            myCanvas.update()
        for i in range(38):
            myCanvas.move(r1,-2,0)
            time.sleep(.01)
            myCanvas.update()
        for i in range(51):
            myCanvas.move(r1,0,-2)
            time.sleep(.01)
            myCanvas.update()

    root = Tk()
    myCanvas = Canvas(root, height=300, width=300, bg="white")
    myCanvas.pack()
    root.bind("<Return>",movingSquare)#go to the displayed window and 
                              #hit return to run the function named movingSquare
    root.mainloop() 

start()
