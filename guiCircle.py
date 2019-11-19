from tkinter import *
import time




def start():
    """
    Create a new window, and run the function "movingCircle" when return is pressed.
    """
    def movingCircle(Event):
        r1 = create_circle(50, 25, 87.5, 'red')
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
    root.bind("<Return>", movingCircle)
    root.mainloop()
    
def create_circle(x, y, r, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return myCanvas.create_oval(x0, y0, x1, y1, fill="color") 

start()
