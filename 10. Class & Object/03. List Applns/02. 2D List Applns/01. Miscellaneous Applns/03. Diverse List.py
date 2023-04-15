import os
os.system('cls')

class DiverseList():
    def __init__(self, r, c):
        self.list = [[0]*c for i in range(r)]
        self.row, self.col = r, c

    def input(self):
        for i in range(self.row):
            for j in range(self.col):
                print("Enter element for position (",i+1,", ",j+1,"): ", sep='', end='')
                self.list[i][j] = int(input())

    def display(self):
        print("Given array elements:\tRow Sums\n")
        for i in range(self.row):
            for j in range(self.col):
                print(self.list[i][j]," ", sep='', end='')
            print("\t\t", self.getSum(self.list[i]), sep='')
            
    def getSum(self, list1D):
        return sum(list1D)

    def getRowSums(self):
        return [self.getSum(row) for row in self.list] 
        
    def is_diverse(self):
        if len(set(self.getRowSums()))==len(self.getRowSums()):
            print("\nRow sums are all different!\nThe array is Diverse!\n")
        else:
            print("\nRow sums are not different!\nThe array is not Diverse!\n")

print("To check if the sums of rows are unique or not:")
dim = input("Enter dimensions: ")
print()

obj = DiverseList(int(dim[0]), int(dim[-1]))
obj.input()
obj.display()
obj.is_diverse()