import os
os.system("cls")

class PerniciousNumber():
    def __init__(self, lim1, lim2):
        self.startlim = lim1
        self.endlim = lim2

    def denaryToBinary(Self, n):
        bin = 0
        while n>0:
            bin = n%2+bin*10
            '''  Formation of Binary integer done WRONGLY!! Needs to be FIXED!! '''
            n//=2
        return bin

    def isPrime(self, n):
        if n<2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def isPernicious(self, n):
        bin, count = self.denaryToBinary(n), 0
        ''' The below loop should be REMOVED and the task done elsewhere. '''
        while bin>0:
            if bin%10==1:
                count+=1
            bin//=10
        return self.isPrime(count)
        
    # Use string for presentation AGAIN. Had to teach you the algo of working without it. Have done.
    # So now come back to string storage as it makes the code MORE EFFICIENT. The below code with 
    # checks in the loop is S L O W!!

    def generate(self):
        isFound = False
        for i in range(self.startlim, self.endlim+1):
            if self.isPernicious(i):
                if not isFound:
                    print("\nPERNICIOUS NUMBER\tBINARY EQUIVALENT")
                isFound = True
                print(i, "\t\t\t", self.denaryToBinary(i))
        if not isFound:
            print("\nNo Pernicious Numbers found in the given range!")

print("To display Pernicious number till a given range:")
lim1 = int(input("Enter the start limit: "))
lim2 = int(input("Enter the end limit: "))

obj = PerniciousNumber(lim1, lim2)
obj.generate()
print()