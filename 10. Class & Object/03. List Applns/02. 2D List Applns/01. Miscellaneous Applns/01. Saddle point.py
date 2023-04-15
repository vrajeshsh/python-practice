import os
os.system('cls')

class SaddlePoint():
    def __init__(self, n):
        self.mat = [[0]*n for i in range(n)]
        self.n = n

    def fill_matrix(self):
        for i in range(self.n):
            for j in range(self.n):
                print("Enter element for position (",i+1,", ",j+1,"): ", sep='', end='')
                self.mat[i][j] = int(input())

    def show_matrix(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.mat[i][j]," ",end='')
            print()

    def sort_diagonal(self):
        diag = sorted([self.mat[i][i] for i in range(self.n)])
        for i in range(self.n):
            self.mat[i][i] = diag[i]
            
        ''' Vrajes's Java-oriented code of 1987:
        for i in range(self.n):
            for j in range(self.n):
                if self.mat[i][i]<self.mat[j][j]:
                    self.mat[i][i], self.mat[j][j] = self.mat[j][j], self.mat[i][i]
        '''

    def find_saddle_points(self):
        sp, pos = -1, ""
        for i in range(self.n):
            for j in range(self.n): # This being a SQUARE 2D LIST, is the 2nd loop necessary?
                mini, maxi = min(self.mat[i]), max([col[j] for col in self.mat])
                if mini==maxi:
                    sp = mini
                    pos+=("(" if pos=="" else ", (")+str(i+1)+", "+str(j+1)+")"
        if sp!=-1:
            print("\nSaddle point(s) ",sp ," was found at location(s): ",pos,"\n",sep='' )
        else:
            print("\nNo Saddle Points exist in the matrix!\n")

print("To display the saddle point in a matrix and also sort along principle diagonal:")
n = int(input("Enter number of rows/columns: "))
print()

obj = SaddlePoint(n)
obj.fill_matrix()
print("\nThe original matrix:")
obj.show_matrix()
obj.find_saddle_points()
obj.sort_diagonal()
print("The matrix after sorting along the principle diagonal:")
obj.show_matrix()
print()