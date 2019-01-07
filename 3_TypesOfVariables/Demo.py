
class Car:

    wheels = 4          #Class variable


    def __init__(self):
        self.mil=10         #obe
        self.com="BMW"      #instance variables


c1=Car()
c2=Car()

c1.mil=0

Car.wheels=5        # spremeni vrednost vsem objektom!

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)