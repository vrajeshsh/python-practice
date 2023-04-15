import os
os.system('cls')

class LatinSquare():
    def __init__(self, n):
        self.sqr = [[0]*n for i in range(n)]
        self.n = n

    def input(self):
        for i in range(self.n):
            for j in range(self.n):
                print("Enter element for position (",i+1,", ",j+1,"): ", sep='', end='')
                self.sqr[i][j] = int(input())

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.sqr[i][j]," ",end='')
            print()

    def get_column(self, c):
        return [col[c] for col in self.sqr]

    def has_all_values(self, list1D1, list1D2):
        return sorted(list1D1)==sorted(list1D2)

    def contains_duplicates(self, list1D):
        return len(list1D) != len(set(list1D))

    def is_latin_square(self):
        if self.contains_duplicates(self.sqr[0]):
            return False
        for i in range(self.n):
            if not self.has_all_values(self.sqr[0], self.sqr[i]):
                return False
            if not self.has_all_values(self.sqr[0], self.get_column(i)):
                return False
        return True

print("To check if the given matrix is a Latin Square: ")
n = int(input("Enter the number of rows/columns: "))
print()

obj = LatinSquare(n)
obj.input()
print("\nThe original matrix:")
obj.display()
if obj.is_latin_square():
    print("\nThe given 2D list is a Latin Square!\n")
else:
    print("\nThe given 2D list is NOT a Latin Square!\n")
