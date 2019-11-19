
import tkinter as tk

class MyGame:
    def __init__(self, master):
        """
        This is the constructor MyGame() that takes a single tk window as
        parameter. (We do not pass in a parameter for self, Python
        does that.) It builds a MyGame object that has a title, two
        button widgets, and a canvas widget. Identify those four
        pieces in the code of the method and show your partners before you proceed.

        """
        self.master = master
        master.title("Game")

        self.my_print_button = tk.Button(master, text="Print Rude", command=self.myPrintRude)
        self.my_print_button.pack() #pack() places the button on the Canvas
        
        self.my_printt_button = tk.Button(master, text="Print Spam", command=self.myPrintSpam)
        self.my_printt_button.pack() 
        
        canvas_width = 600
        canvas_height = 400
        
        self.canvas = tk.Canvas(master, width = canvas_width, height = canvas_height)
        
        self.square_button = tk.Button(master, text="Square", command = self.squareOnButton)
        self.square_button.pack()

        self.canvas.create_line(0,100,canvas_width,100)

        self.canvas.create_line(0, 0, canvas_width, canvas_height)
        self.canvas.create_line(0, canvas_height, canvas_width, 0)
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.squareOnClick)
        
        self.close_button = tk.Button(master, text="Close", command=master.destroy)
        self.close_button.pack()
        
    def squareOnButton(self):
        """
        Creates a square on button click
        """
        self.canvas.create_rectangle(275, 175, 325, 225)
      
    def squareOnClick(self, event):
        """
        Creates a square on mouse click
        """
        self.canvas.create_rectangle(event.x+25, event.y+25, event.x-25, event.y-25)
        print(event)
        
    def myPrintRude(self):
        """
        Prints something very rude
        """
        for x in range(1,9999):
            print("something very rude")
        
    def myPrintSpam(self):
        """
        Prints "Spam!"
        """
        print("Spam!")

root_window = tk.Tk()
my_gui = MyGame(root_window)
root_window.mainloop() #starts listening for events

#Objects have attributes and behaviors