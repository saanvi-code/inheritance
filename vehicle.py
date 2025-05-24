class Vehicle:
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage

class bus(Vehicle):
    pass

school=bus("school bus",89,564)
print("vehicle name:",school.name,"speed: ",school.speed,"mileage is: ",school.mileage)