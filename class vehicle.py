class Vehicle:
    #create init method
    def __init__(self, max_speed,mileage):
           #bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage
#object creation
modelX = Vehicle(240,18)
modelY = Vehicle(90,345)
#access the variables inside init method
print("Model Max Speed:",modelX.max_speed)
print("Model Mileage:",modelX.mileage)
print("Model Max Speed:",modelY.max_speed)
print("Model Mileage:",modelY.mileage)
    