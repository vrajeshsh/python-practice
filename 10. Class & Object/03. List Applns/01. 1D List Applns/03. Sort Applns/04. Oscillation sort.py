import os
os.system('cls')

class OscillationSort():
    def __init__(self, n):
        self.num = []
        self.n = n

    def input(self):
        for i in range(self.n):
            print("Enter number for element #", i+1, ": ", sep='', end='')
            self.num.append(int(input()))

    def display(self):
        print("\nThe given list: ", self.num, sep='')

    def swap(self, p1, p2):
        self.num[p1], self.num[p2] = self.num[p2], self.num[p1]
        
    def indexofnthmax(self, n):
        return sorted(self.num)[-n]

    def arrange(self):
        

print("To arrange list such that highest element in place at the center, the 2nd highest to its right and 3rd highest to its left and so on:")
n = int(input("Enter the number of elements: "))

obj = OscillationSort(n)
obj.input()
obj.display()
obj.arrange()