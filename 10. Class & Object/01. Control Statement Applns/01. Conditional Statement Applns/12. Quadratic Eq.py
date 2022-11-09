import os
os.system("cls")

class QuadRoots():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return self.b**2 - 4*self.a*self.c
        
    def roots(self):
        disc, r1, r2 = self.discriminant(), 0, 0
        if disc==0:
            r1= r2= -self.b/(2*self.a)
        else:
            r1= (-self.b+(disc**0.5))/2*self.a 
            r2= (-self.b-(disc**0.5))/2*self.a
        return r1, r2

    def display(self):
        disc = self.discriminant()
        r1, r2= self.roots()
        print("\nThe three coefficients are: ",self.a,", ",self.b,", and ",self.c, sep='')
        if disc<0:
            print("\nRoots are Imaginary!\n")
        else:
            print("\nRoots are ", ("Equal." if disc==0 else "Real and Distinct."),
                "\nRoots are: ", round(r1,3), round(r2,3), "\n")

print("To find the roots of a Quadratic equation: ")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

obj = QuadRoots(a, b, c)
obj.display()

''' I feel really GUILTY TODAY!!! I only presented to you problem after problem where the programs 
    had NICELY DESIGNED classes in them!!
    And see today?
    You cannot handle the designing only!! In each and every program you are failing to LIVE UP
    to the expectation of output requirement of the problems!!! 
'''