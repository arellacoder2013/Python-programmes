class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
    def perimeter(self):
        return 2*3.14*self.r
circ1 = Circle(5)
print("Area :",circ1.area())
print("perimeter :",circ1.perimeter())