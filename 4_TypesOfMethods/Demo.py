
class Student:

    school="Telusko"

    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1          #accessors

    def set_m1(self,value):     #mutators
        self.m1=value

    @classmethod        # --> Decorator
    def getSchool(cls):      #cls = Class   --> Class variable
        return cls.school

    @staticmethod       #--->Decorator
    def info():                 # --> Static method
        print("This is Student class.. in abc module")



s1=Student(34,67,32)
s2=Student(89,102,369)


print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()
