import os
os.system('cls')

class D2Point:
    def __init__(self, xx = 0, yy = 0):
        self.x = xx
        self.y = yy

    def display(self):
        print(self.x,", ",self.y, sep='', end='')

    def distance2D(self, d2point):
        return round(((d2point.x - self.x)**2 + (d2point.y - self.y)**2)**0.5, 6)

class D3Point(D2Point):
    def __init__(self, xx = 0, yy = 0, zz = 0):
        super().__init__(xx, yy)
        self.z = zz

    def display(self):
        print("(", end='')
        super().display()
        print(", ", self.z,")", sep='')

    def distance3D(self, d3point):
        return round((self.distance2D(d3point) + ((self.z - d3point.z)**2)**0.5), 6)

print("To display the distance between points on a plane and in space:")
print("\nEnter the coordinates for Point 1:")
x1 = float(input("x: "))
y1 = float(input("y: "))
z1 = float(input("z: "))
print("\nEnter the coordinates for Point 2:")
x2 = float(input("x: "))
y2 = float(input("y: "))
z2 = float(input("z: "))

obj1, obj2 = D3Point(x1, y1, z1), D3Point(x2, y2, z2)

print("\nPoint #1: ", sep='', end='')
obj1.display()
print("Point #2: ", sep='', end='')
obj2.display()
print("\nDistance between the points on a Plane: ", obj1.distance2D(obj2), 
    "\nDistance between the points in Space: ", obj1.distance3D(obj2), sep='')
print()
