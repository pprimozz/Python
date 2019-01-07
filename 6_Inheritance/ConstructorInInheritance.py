class A:

    def __init__(self):
        print("In A init")

    def feature(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):
    def __init__(self):
        super().__init__()     #parent class
        print("In B init")

    def feature1(self):
        print("Feature 1 working")

    def feature4(self):
        print("Feature 4 working")


a1=B()      #pokliče konstruktor od A