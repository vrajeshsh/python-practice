import os, math
os.system("cls")

class EquivalentNumbers():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.baseX = self.baseY = 0

    def display(self):
        if self.baseX==0 and self.baseY==0:
            print("\n",self.x," is NOT equal to ", self.y," in any base from 2 - 10!\n", sep='')
        else:
            print("\n",self.x," (Base ",self.baseX,") = ", self.y," (Base ",self.baseY,")\n", sep='')

    def minimumBase(self, n):
        minBase = 0
        while n>0:
            dig = n%10
            if dig>minBase:
                minBase = dig
            n//=10
        return minBase+1
        
    def toBase10(self, num, base):
        i, dec = 0, 0
        while num>0:
            dec+= num%10*pow(base, i)
            i+=1
            num//=10
        return dec

    ''' Below method tends to drown a person in the flood of 'self' just like the beauty of the
    Roman princess Cleopatra drowned so many eminent Roman Empires of that time... '''
    
    def find(self):
        startBaseX, startBaseY = self.minimumBase(self.x), self.minimumBase(self.y)
        for i in range(startBaseX, 11):
            numX = self.toBase10(self.x, i)
            for j in range(startBaseY, 11):
                if  numX == self.toBase10(self.y, j):
                    self.baseX, self.baseY = i, j
                    return 
        
print("To check if two numbers in different number systems converted to Base 10 are equal:")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

num = EquivalentNumbers(x, y)
num.find()
num.display()
            
''' You never have TRULY UNDERSTOOD what this program is all about. Kindly try to understand it NOW.
Two numbers are given which are assumably in two different bases. E.g. 27 and 36. These two numbers
are in two DIFFERENT BASES (between 2 - 10). You need to find out:

Converted from their own respective bases down till 10 in which smallest number systems the two
numbers will be numerically (i.e. converted valuewise) equal to each other.

Since the numbers are supposed to be equal when converted to base 10, the toBase10() method is given.
Since the bases of the two numbers are not given, therefore it is required to know their optimum
bases to start with, hence the minimumBase() method is given.
And to find the two bases... 'loop-woop chalake' in which the two numbers become equal that the find()
method is given.

May be not completely clear, (as I know you) but still you are slightly in a better position now.
At least you now have a little understanding what needs to be done in each method at least.
'''