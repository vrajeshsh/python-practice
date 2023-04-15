import os
os.system('cls')

class List2DSorter():
    def __init__(self, r, c):
        self.list2D = [[0]*c for i in range(r)]
        self.r = r
        self.c = c

    def fill_list(self):
        for i in range(self.r):
            for j in range(self.c):
                print("Enter number for position (",i+1,", ",j+1,"): ", end='', sep='')
                self.list2D[i][j] = int(input())

    def show_list(self):
        for i in range(self.r):
            for j in range(self.c):
                print(self.list2D[i][j], "\t", sep='', end='')
            print()
''' The below method is supposed to return an object, but at present it is returning a 
    list Fix this method also. '''
    def get_sorted(self):
        return sorted([self.list2D[i][j] for i in range(self.r) for j in range(self.c)])

    def find_median(self):
        rearranged = self.get_sorted()
        mid = len(rearranged)//2
        return rearranged[mid] if len(rearranged)%2!=0 else round(((rearranged[mid - 1]+rearranged[mid])/2), 2)
            
print("To sort elements of a matrix in ascending and descending order and also find it's median: ")
dim = input("Enter matrix dimensions: ")
print()

obj = List2DSorter(int(dim[0]), int(dim[-1]))
obj.fill_list()

print("\nThe original list:")
obj.show_list()

print("\nThe 2-D list after sorting in ascending order:")
obj.get_sorted().show_list()

print("\nThe median of the list: ", sep='', end='')
print(obj.find_median())