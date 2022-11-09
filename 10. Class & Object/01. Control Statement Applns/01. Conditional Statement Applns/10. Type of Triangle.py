import os
os.system("cls")

class TriSide():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    
    def type(self):

        if self.a**2==self.b**2+self.c**2 or self.b**2==self.c**2+self.a**2 or self.c**2==self.a**2+self.b**2:
            type="Right-angled "
        elif self.a**2>self.b**2+self.c**2 or self.b**2>self.c**2+self.a**2 or self.c**2>self.a**2+self.b**2:
            type="Obtuse-angled "
        elif self.a**2<self.b**2+self.c**2 or self.b**2<self.c**2+self.a**2 or self.c**2<self.a**2+self.b**2:
            type="Acute-angled "
        if self.a==self.b==self.c:
            type+="Equilateral"
        elif self.a==self.b or self.b==self.c or self.c==self.a:
            type+="Isosceles"
        else:
            type+="Scalene"

        return type

    def display(self):
        if self.a+self.b>self.c and self.b+self.c>self.a and self.c+self.a>self.b:
            print("\nTriangle formed: ",self.type(), 
                "\nArea: ",round(self.area(),3), "\n",sep='')
        else:
            print("\nThe given sides DO NOT make a valid triangle!\n")

print("To find the type of triangle formed using the given sides:")
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

obj = TriSide(a,b,c)
obj.display()