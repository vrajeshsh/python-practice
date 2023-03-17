import os
os.system("cls")

class EquivalentNos():
    def __init__(self, lim):
        self.lim = lim

    def sumOfAliquots(self, n):
        ssum = 0
        for i in range(1, n//2+1):
            if n%i==0:
                ssum+=i
        return ssum

    def generate(self):
        print("\nEQUIVALENT NUMBERS\tALIQUOT SUM")
        for i in range(4, self.lim):
            nums, aliSum = "", self.sumOfAliquots(i)
            for j in range(i+1, self.lim+1):
                if aliSum == self.sumOfAliquots(j):
                    nums+=", "+str(j)
            if nums!="" and aliSum > 1:
                nums=str(i)+nums
                print(nums,"\t\t\t",aliSum,sep='')

print("To display Equivalent no.s upto a given limit:")
lim = int(input("Enter the limit: "))

obj = EquivalentNos(lim)
obj.generate()
print()