import os
os.system('cls')

class MirrorList():
    def __init__(self, n):
        self.list2D = [[0]*n for i in range(n)]
        self.n = n

    def fill_list(self):
        for i in range(self.n):
            for j in range(self.n):
                print("Enter element for position (", i+1, ", ", j+1, "): ", sep='', end='')
                self.list2D[i][j] = int(input())

    def show_list(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.list2D[i][j], "\t", end='')
            print()
        print()

    def get_copy(self):
        copy = MirrorList(self.n)
        copy.list2D = [row[:] for row in self.list2D]
        return copy
    
    def mirror_horizontally(self):
        self.list2D = [row[::-1] for row in self.list2D]
    
    def mirror_vertically(self):
        self.list2D = [row for row in self.list2D[::-1]]
    
print("To mirror a square matrix horizontally and vertically:")
n = int(input("Enter number of rows/columns: "))
print()

obj = MirrorList(n)
obj.fill_list()

print("\nThe original list:", sep='')
obj.show_list()

copy = obj.get_copy()
copy.mirror_horizontally()
print("\nMirror image by inverting horizontally:", sep='')
copy.show_list()

copy = obj.get_copy()
copy.mirror_vertically()
print("Mirror image by inverting vertically:", sep='')
copy.show_list() 
