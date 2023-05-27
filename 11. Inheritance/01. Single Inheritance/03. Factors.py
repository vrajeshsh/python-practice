import os
os.system('cls')

class Number:
    def __init__(self, n):
        self.n = n
        self.num = []

    def read_values(self):
        for i in range(self.n):
            print("Enter the value for number #", i+1, ": ", sep='', end='')
            self.num.append(int(input()))

class Factors(Number):
    def __init__(self, n):
        super().__init__(n)
        self.fac = []

    def count_factors(self):
        for num in self.num:
            count = 0
            for j in range(1, num+1):
                if num%j==0:
                    count+=1
            self.fac.append(count)

    def display(self):
        print("\nInteger\t\tFactors\t\tStatus", sep='')
        for i in range(self.n):
            f = self.fac[i]
            status = "Composite" if f>2 else "Prime" if f==2 else "Neither Prime/Composite"
            print(self.num[i],"\t\t", self.fac[i],"\t\t",status,sep='')
        print("\n")
        
print("To display factors of integers and their status:")
n = int(input("Enter number of integers: "))
print()

obj= Factors(n)
obj.read_values()
obj.count_factors()
obj.display()
