class circ:
    def __init__(self,r):
        self.radius=r
    def calculate_area(self):
        return 3.14*self.radius*self.radius
    def calculate_perimeter(self):
        return 2*self.radius+self.radius
mycircle=circ(6)
print("The radius of mycircle object is:",mycircle.radius)
print("The area of mycircle object is:",mycircle.calculate_area)
print("The perimeter of mycircle object is:",mycircle.calculate_perimeter)