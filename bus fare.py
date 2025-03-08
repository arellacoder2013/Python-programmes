class Vehicle:
    def __init__(self,name):
        self.name=name
class Bus(Vehicle):
    def __init__(self,name,km):
        Vehicle.__init__(self,name)
        self.km = km
    def cal_fare(self):
        print(self.km*26)
obj1 = Bus(".volvo",3)
obj1.cal_fare()