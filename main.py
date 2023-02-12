class vehicle():
    wheels=4
    color=None
    doors=0
    def __init__(self,color,doors):
        self.color=color
        self.doors=doors
        


class car(vehicle):
    speed=0
    cc=2.0
    def setSpeed(self):
        self.speed=60

Opel=car('Blue',4)
print(Opel.color)
print(Opel.doors)
print(Opel.wheels)
print (Opel.speed)
print(Opel.cc)
Opel.setSpeed()
print(Opel.speed)

