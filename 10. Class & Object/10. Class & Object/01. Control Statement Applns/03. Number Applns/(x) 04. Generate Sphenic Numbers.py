import os
os.system("cls")

class SphenicNumber():
    def __init__(self, lim1, lim2):
        self.startlim = lim1
        self.endlim = lim2

    def isSphenic(self, n):
        facs, i = "", 2  
        # Kindly REMOVE the 1-D array that has been used here. For such trivial tasks WHY USE ARRAYS!!'''  
        while i<=n:
            if n%i==0:
# Use only ONE LOOP for this method. [TIP: Prime Factorization does not require a prime check.]'''
                for j in range(2, int(i**0.5)+1):
                    if i%j==0:
                        return False
                if i not in facs:
                    facs.append(i)
                    n//=i
                else:
                    return False
            else:
                i+=1
        return len(facs)==3

    def generate(self):
        isFound = False
        lim = self.startlim
        for i in range(self.startlim, self.endlim+1):
            if self.isSphenic(i):
                if not isFound:
                    print("\nSPHENIC NUMBERS BETWEEN ", lim, " AND ",self.endlim,":\n", sep='')
                isFound = True
                disp_facs, j, num = "", 2, i
                ''' The below loop must be REMOVED and the task done elsewhere. '''
                while j<=num:
                    if num%j==0:
                        disp_facs+= str(j) if disp_facs=="" else " x "+str(j)
                        num//=j
                    else:
                        j+=1
                print(i," = ", disp_facs, sep='')
        if not isFound:
            print("\nNo Sphenic Numbers found in the given range!")

print("To display Sphenic Numbers till a given limit: ")
lim1 = int(input("Enter the start limit: "))
lim2 = int(input("Enter the end limit: "))

obj = SphenicNumber(lim1, lim2)
obj.generate()
print()