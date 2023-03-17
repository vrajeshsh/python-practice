import os
os.system("cls")

class KeithNumber():
    def __init__(self, n):
        self.n = n

    def isKeith(self, n):
        nums, temp, cnt = [], n, 0
        while temp>0:
            nums.append(temp%10)
            cnt+=1
            temp//=10
        nums.reverse()
        nxt, i = 0, cnt
        while nxt<n:
            nxt = 0
            for j in range(1, cnt+1):
                nxt+=nums[i-j]
            nums.append(nxt)
            i+=1
        return nxt==n


    def generate(self):
        keiths = ""
        for i in range(10, self.n+1):
            if self.isKeith(i):
                keiths+=str(i) if keiths=="" else ", "+str(i)
            
        if keiths=="":
            print("\nNo Keith Numbers found in the given range!\n")
        else:
            print("\nThe Keith numbers present between 1 and ", self.n," are:\n",keiths,"\n", sep='')

print("To display Keiths numbers till a given limit:")
n = int(input("Enter the limit: "))

obj = KeithNumber(n)
obj.generate()

'''
197 = 1 + 9 + 7 = 17,
9 + 7 + 17 = 33,
7 + 17 + 33 = 57,
17 + 33 + 57 = 107,
33 + 57 + 107 = 197 (Keith).
The first few are 14, 19, 28, 47, 61, 75, 197, 742, 1104, 1537, 2208, 2580, 3684, 4788, 7385, 7647, 
7909, …, …
'''