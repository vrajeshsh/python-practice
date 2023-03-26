import os
os.system("cls")

class Equation():
    def __init__(self, a, b, c, d, m, n):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.m = m
        self.n = n

    def denominator(self):
        return self.a*self.d - self.c*self.b

    def solution(self):
        denom = self.denominator()
        if denom!=0:
            x= (self.m*self.d - self.b*self.n)/denom
            y= (self.n*self.a - self.m*self.c)/denom
            print("\nThe solutions to the given pair of equations are:",
            "\nx= ", x,
            "\ny= ", y, "\n",sep='')
        else:
            print("\nSolutions are NOT POSSIBLE with the given coefficients!\n")
    
    def display(self):
        print("\nThe coefficients are: ",self.a,", ",self.b,", ", 
            self.c,", and ", self.d, sep='')
        self.solution()

print("To find the solution to a pair of simultaneous equations: ")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
m = float(input("m: "))
n = float(input("n: "))

obj = Equation(a, b, c, d, m, n)
obj.display()