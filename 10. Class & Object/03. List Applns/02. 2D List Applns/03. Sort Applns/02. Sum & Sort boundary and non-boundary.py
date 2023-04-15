import os
os.system('cls')

class BoundarySorter():
    def __init__(self, r, c):
        self.list2D = [[0]*c for i in range(c)]
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
    ''' Very Well done considering the 'difficulty level' of this program! 
    Just the below method has some tiny faults which I hope you will surely be able to 
    fix yourself. Do keep it fixed. Will check the final version on Saturday. '''
    def boundary_sorted(self):
        dup = BoundarySorter(self.r, self.c)
        dup.list2D, k = [row[:] for row in self.list2D], 0
        boundary_sort = sorted([self.list2D[i][j] for i in range(self.r) for j in range(self.c) if i==self.r-1 or i==0 or j==0 or j==self.c-1])
        for i in range(self.r):
            for j in range(self.c):
                if i==self.r-1 or i==0 or j==0 or j==self.c-1:
                    dup.list2D[i][j] = boundary_sort[k]
                    k+=1
        return dup

    def non_boundary_sorted(self):
        dup = BoundarySorter(self.r, self.c)
        dup.list2D, k = [row[:] for row in self.list2D], 0
        non_boundary_sort = sorted([self.list2D[i][j] for i in range(self.r) for j in range(self.c) if i!=self.r-1 and i!=0 and j!=0 and j!=self.c-1])
        for i in range(self.r):
            for j in range(self.c):
                if i!=self.r-1 and i!=0 and j!=0 and j!=self.c-1:
                    dup.list2D[i][j] = non_boundary_sort[k]
                    k+=1
        return dup

    def show_boundary(self, flag):
        boundary_sum, non_boundary_sum = 0, 0
        print("\nThe ", "non-" if not flag else "", "boundary elements of the 2-D list:", sep='')
        for i in range(self.r):
            for j in range(self.c):
                if flag and (i==self.r-1 or i==0 or j==0 or j==self.c-1):
                    boundary_sum+= self.list2D[i][j]
                    print(self.list2D[i][j],"\t", end='')
                elif not flag and (i!=self.r-1 and i!=0 and j!=0 and j!=self.c-1):
                    non_boundary_sum+=self.list2D[i][j]
                    print(self.list2D[i][j],"\t", end='')
                else:
                    print("\t", end='')
            print()
        if flag:
            print("\nSum of boundary elements: ", boundary_sum,"\n",sep='')
        else:
            print("\nSum of non-boundary elements: ", non_boundary_sum,"\n",sep='')          

print("To sort the boundary and non-boundary elements of a matrix and find their sum:")
dim = input("Enter matrix dimensions: ")
print()

obj = BoundarySorter(int(dim[0]), int(dim[-1]))
obj.fill_list()
print("\nThe original list:")
obj.show_list()
print("\nThe 2-D list after sorting boundary elements:")
obj.boundary_sorted().show_list()
print("\nThe 2-D list after sorting non-boundary elements:")
obj.non_boundary_sorted().show_list()
obj.show_boundary(True)
obj.show_boundary(False)