class Rectangle():
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def rectangle__area(self):
        return self.length*self.width
newRectangle =Rectangle(12,10)
print("Dimension of Rectangle - Length : %d Width : %d"% (newRectangle.length,newRectangle.width))
print("Area of Rectangle :",newRectangle.rectangle__area())