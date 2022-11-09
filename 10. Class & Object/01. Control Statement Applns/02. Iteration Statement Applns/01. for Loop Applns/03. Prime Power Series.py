import os
os.system("cls")

class MySeries():
    def __init__(self, x, n):
        self.x= x
        self.n = n

    def factorial(self, n):
        fact = 1
        for i in range(1, n+1):
            fact*=i
        return fact

    def generateSeries(self):
        ssum, cnt, p = 0, 0, -1
        print("\nThe Prime Exponential Series:")
        while cnt < self.n:             # setting the loop as per the no. of terms here
            p+= 1                       # counter for the power set here
            isPrime= True
            for i in range(2, p//2+1):  # loop to check for the prime powers
                if p%i == 0:
                    isPrime= False
                    break
            if p<2 or isPrime:          # if the power is < 2 or prime
                cnt+= 1
                fact= 1
                for i in range(1, p+1):
                    fact*= i            # calculating the factorial of the power here    
                term= x**p/fact
                ssum+= term
                print(round(term,3), " + ", sep= '', end='')
        print("\nSum of the series: ", round(ssum, 5),"\n", sep='')

print("To generate a given series: ")
x = int(input("Enter the value of 'x': "))
n = int(input("Enter the value of 'n': "))

obj = MySeries(x, n)
obj.generateSeries()