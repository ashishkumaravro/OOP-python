class Shape:  ## class as a template
    def __init__(self, dim1, dim2):  # parent class
        self.dim1 = dim1  # dim1 and dim2 are common attributes
        self.dim2 = dim2

    def area(self):
        print("I am area method of shape class")


class Triangle(Shape):  # inherite shape class
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of triangle: ", area)


class Reactangle(Shape):  # inherite shape class
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Reactangle: ", area)


value1 = int(input("first input for : "))
value2 = int(input("last Input for : "))
t1 = Triangle(value1, value2)
t1.area()

r1 = Reactangle(value1, value2)
r1.area()