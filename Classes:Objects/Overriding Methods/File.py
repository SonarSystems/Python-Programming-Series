class Vehicle:#(object):
    speed = 0

    #def __new__(cls):
    #  return object.__new__(cls)

    def __init__(self, speed = 0):
      self.speed = speed

    def IncreaseSpeed(self, increaseAmount):
        self.speed += increaseAmount

    def __del__(self):
      print("Object has been destroyed")

class Car(Vehicle):
  weight = 10

  def IncreaseWeight(self, weight):
    self.weight += weight

  def IncreaseSpeed(self, increaseAmount):
        self.speed *= increaseAmount

car1 = Vehicle()
car2 = Vehicle(89)
childCar = Car(5)

print(childCar.weight)
childCar.IncreaseWeight(9)
print(childCar.weight)
childCar.IncreaseSpeed(5)
print(childCar.speed)

print("Speed for car 1: %i" % car1.speed)
print("Speed for car 2: %i" % car2.speed)
car1.IncreaseSpeed(5)
print("Speed for car 1: %i" % car1.speed)
print("Speed for car 2: %i" % car2.speed)

del car1
