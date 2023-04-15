import os
os.system("cls")

class Duplicates():
    def __init__(self, n):
        self.num = []
        self.n = n

    def input(self):
        for i in range(self.n):
            print("Enter number for element #", i+1, ": ", sep='', end='')
            self.num.append(int(input()))

    def display(self):
        print("\nThe given list:\n", self.num, sep='')

    def frequency(self, x, n):
        freq= 0
        for i in range(n):
            if self.num[i] == x:
                freq+= 1
        return freq

    def find(self):
        cnt= 0
        for i in range(self.n):
            if self.frequency(self.num[i], self.n)>1 and self.frequency(self.num[i], i) == 0:
                cnt+= 1
                if cnt == 1:
                    print("\nDuplicates present in the list are:")
                print(self.num[i],",", end='', sep='')
        if cnt == 0:
            print("\nNo duplicates found in the list!\n", sep='')
        else:
            print("\n\n(",cnt,"duplicates found.)")

print("To check for duplicates in a list and display if present:")
n = int(input("Enter the number of elements: "))
