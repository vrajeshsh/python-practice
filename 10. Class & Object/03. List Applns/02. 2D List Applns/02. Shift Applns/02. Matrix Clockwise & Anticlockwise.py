import os
os.system('cls')

class ListRotator():
    def __init__(self, n):
        self.list2D = [[0]*n for i in range(n)]
        self.n = n

    def fill_list(self):
        for i in range(self.n):
            for j in range(self.n):
                print("Enter element for position (", i+1, ", ", j+1, "): ", sep='', end='')
                self.list2D[i][j] = int(input())
                
    ''' And as a TIP (you'll be surprised!) -- it's possible to SHORTEN the below code also
    using utter innovation! '''

    def show_list(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.list2D[i][j], "\t", end='')
            print()
        print()

    def get_copy(self):
        copy = ListRotator(self.n)
        copy.list2D = [row[:] for row in self.list2D]
        return copy
    
    ''' This way people used to code in Python when it was just develoved around 2000.
    But if possible with all that I have aready taught/shown you, try in your leisure time to 
    SHORTEN FURTHER the below two method codes obviously if possible through yiur own efforts. '''
    
    def rotate90_clockwise(self):
        for i in range(self.n):
            for j in range(i, self.n):
                self.list2D[i][j], self.list2D[j][i] = self.list2D[j][i], self.list2D[i][j]
        for i in range(self.n):
            self.list2D[i] = self.list2D[i][::-1] 
        return self.list2D

    def rotate90_anticlockwise(self):
        for row in self.list2D:
            row.reverse()
        for i in range(self.n):
            for j in range(i, self.n):
                self.list2D[i][j], self.list2D[j][i] = self.list2D[j][i], self.list2D[i][j]
        return self.list2D

print("To rotate a matrix by 90",chr(176)," in clockwise and anticlockwise directions:", sep='')
n = int(input("Enter number of rows/columns: "))
print()

obj = ListRotator(n)
obj.fill_list()
print("\nThe original list:", sep='')
obj.show_list()

copy = obj.get_copy()
copy.rotate90_clockwise()
print("Matrix after rotating 90",chr(176)," clockwise:", sep='')
copy.show_list()

copy = obj.get_copy()
copy.rotate90_anticlockwise()
print("Matrix after rotating 90",chr(176)," anticlockwise:", sep='')
copy.show_list()
