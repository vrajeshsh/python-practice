import os
os.system('cls')

class Circle:
    def __init__(self, rad):
        self.radius = rad

    def circumference(self):
        return  2*3.14*self.radius

    def area(self):
        return 3.14*self.radius**2

    def display(self):
        print("Radius: ", self.radius, 
            "\nCircumference: ", round(self.circumference(), 3),
            "\nArea: ", round(self.area(), 3), sep='')

class Cylinder(Circle):
    def __init__(self, rad, hgt):
        super().__init__(rad)
        self.height = hgt
    
    def surface_area(self):
        return super().circumference() * (self.height+rad)

    def volume(self):
        return super().area()*self.height

    def display(self):
        super().display()
        print("Height: ", self.height,
            "\nSurface Area: ", round(self.surface_area(), 3),
            "\nVolume: ", round(self.volume(), 3), sep='')

print("To display the properties of Circle and Cylinder:")
rad = float(input("Enter radius of the Circle: "))
hgt = float(input("Enter height of the Cyclinder: "))

obj1, obj2 = Circle(rad), Cylinder(rad, hgt)

print("\nThe properties of the Circle are:")
obj1.display()
print("\nThe properties of Cylinder are:")
obj2.display()
print()

'''
Properties include:
1. The basic measurement of the figure viz. length, breadth etc.
2. Measurements of SA, V, Circumferance etc. as given/required.
Work accordingly.
'''