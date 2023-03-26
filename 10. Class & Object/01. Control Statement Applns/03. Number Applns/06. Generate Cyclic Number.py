import os, math
os.system("cls")

class CyclicNumbers():
    def __init__(self, n):
        self.n = n

    def areSimilar(self, n1, n2):
        num = n1
        digLen = int(math.log10(n1))
        ''' The below algorithm is good but NEW... Kindly keep a note for the WORLD to understand.'''
        while True:
            rem = n1%10
            div = n1//10
            n1 = 10**(digLen) * rem + div
            if num==n1:
                break
            if n1==n2:
                return True
        return False

    def isCyclicNumber(self, num):
        for i in range(2, 7):
            if not self.areSimilar(num, num*i):
                return False
        return True

    def generate(self):
        start, end, cyclicNos = 10**(self.n - 1), (10**self.n), "" 
        for i in range(start, end+1):
            if self.isCyclicNumber(i):
                cyclicNos+=str(i) if cyclicNos=="" else ", "+str(i)
    
        if cyclicNos=="":
            print("\nNo ",self.n,"-digited Cyclic Numbers exist!\n", sep='')
        else:
            print("\n",self.n,"-digited Cyclic Numbers are:\n",cyclicNos,"\n", sep='')


print("To display all n-digited cyclic numbers: ")
n = int(input("Enter the value of 'n': "))

obj = CyclicNumbers(n)
obj.generate()