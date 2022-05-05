class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius

circle1=circle(int(input("Enter 1st radius")))
a=circle1.area()
print("Area = ",a)
b=circle1.circumference()
print("Circumference = ",b)
