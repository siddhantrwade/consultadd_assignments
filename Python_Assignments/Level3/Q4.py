class Shape:

    def __init__(self):
        pass # nothing to add here

    def area(self): #default area 0, unless square has area
        return 0
    
class square(Shape):

    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2 #area of sqaure
        

if __name__ == "__main__":

    # instance of parent
    shape = Shape()
    print("Area of Shape:", shape.area())

    # child instance
    square = square(10)
    print("Area of square: ", square.area())