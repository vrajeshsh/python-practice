import os
os.system("cls")

class ShiftSorter():
    def __init__(self, n):
        self.arr = []
        self.n = n

    def input(self):
        for i in range(self.n):
            print("Enter number of element #",i+1,": ", sep='', end='')
            self.arr.append(int(input()))

    def display(self):
        print("\nThe original list:\n", self.arr, sep='')
        self.shift_sort()
        print("\nThe numbers in the list after arranging as per requirement:\n",
         self.arr, "\n", sep='')

    def shift_sort(self):
        for i in range(n-1):
            for j in range(n-1-i):
                if ((self.arr[j]%2==0 and self.arr[j+1]%2==0 and self.arr[j] < self.arr[j+1]) or
                (self.arr[j]%2==1 and self.arr[j+1]%2==1 and self.arr[j] > self.arr[j+1]) or
                (self.arr[j]%2==0 and self.arr[j+1]%2==1)):
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

print("To display the even numbers of a list in ascending order at the front end, and odds in the rear end in descending order:")
n = int(input("Enter the number of elements: "))

obj = ShiftSorter(n)
obj.input()
print("\nThe numbers in the list before arranging:")
obj.display()