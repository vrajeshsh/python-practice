import os, math
from tracemalloc import start
os.system("cls")

class fasciNoscinatingNumber():
    def __init__(self, n):
        self.n = n

    def isfasciNoscinating(self, num):
        count, count2, count3 = int(math.log10(num))+1, int(math.log10(num*2))+1, int(math.log10(num*3))+1
        if count<3:
            return False
        bigNum = (num*(10**count2)+num*2)*(10**count3)+num*3
        for i in range(1, 10):
            newNum, cnt = bigNum, 0
            while newNum>0:
                if newNum%10==i:
                    cnt+=1
                newNum//=10
            if cnt!=1:
                return False
        return True

    def generate(self):
        startLim, endLim, fasciNos = 10**(self.n -1), 10**self.n, ""
        for i in range(startLim, endLim+1):
            if self.isfasciNoscinating(i):
                fasciNos+= str(i) if fasciNos=="" else ", "+str(i)
        if fasciNos=="":
            print("\nNo ",self.n,"-digited Fascinating Numbers exist!\n", sep='')
        else:
            print("\n",self.n,"-digited Fascinating Numbers are:\n",fasciNos,"\n", sep='')

print("To display n-digit Fascinating numbers:")
n = int(input("Enter the value of 'n': "))

obj = fasciNoscinatingNumber(n)
obj.generate()