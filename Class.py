class desk: #creates template for a class
    def __init__(self, mass): #method
        self.mass = mass #assigns mass that is passed in to the mass of the item
        
    
#d1 = Desk() (this is a method)
#d2 = Desk()
#not the same desk
#d1 = Desk(30)
#d1.mass returns as 30
#d2 = Desk(40)
#d2.mass returns as 40

#a method is a function inside a class
#a constructor is a method whose name is capitalized that makes an instance of a class