import os
os.system("cls")

class FrequencyPattern():
    def __init__(self):
        self.intgr = []

    def input(self):
        i = 0
        while True:
            print("Enter number for element #", i+1, ": ", sep='', end='')
            n = int(input())
            if n==-1:
                break
            self.intgr.append(n)
            i+=1
            
    def show(self):
        print("\nThe given list: ", self.intgr, sep='')

    def frequency(self, x):
        return self.intgr.count(x)

    def showPattern(self):
        newlist = ""
        for i in range(len(self.intgr)):
            ele = (str(self.frequency(self.intgr[i]))+"*"+str(self.intgr[i]))
            if self.frequency(self.intgr[i])>1 and ele not in newlist:
                newlist+= ele if newlist=="" else ", "+ele
        if newlist=="":
            print("\nNo duplicates prest in the list!\n")
        else:
            print("\nThe new list: ", newlist, ".\n", sep='')

print("To replace succeeding repeating numbers by their count:")

obj = FrequencyPattern()
obj.input()
obj.show()
obj.showPattern()

# Taking guidelines from the program already done. Kindly FIX the last one.abs(The first one is very very simple
# and does not have any depth.)