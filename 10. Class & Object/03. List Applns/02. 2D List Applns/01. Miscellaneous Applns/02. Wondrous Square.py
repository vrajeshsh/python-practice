import os
os.system('cls')

class WondrousSquare():
    def __init__(self, n):
        self.sqr = [[0]*n for i in range(n)]
        self.n = n

    def fill_square(self):
        for i in range(self.n):
            for j in range(self.n):
                print("Enter element for position (",i+1,", ",j+1,"): ", sep='', end='')
                self.sqr[i][j] = int(input())

    def show_square(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.sqr[i][j]," ",end='')
            print()

    def frequency(self, num):
        return self.sqr.count(num)

        ''' Vrajesh's Java-oriented code of 1987:
        freq = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.sqr[i][j]==num:
                    freq+=1
        return freq '''

    def is_wondrous_square(self):
        sum_val = 0.5*self.n*(self.n**2+1)
        for i in range(self.n):
            sqr_row = self.sqr[i]
            sqr_col = [col[i] for col in self.sqr]
            if sum(sqr_row) != sum_val or sum(sqr_col) != sum_val:
                return False
            for j in range(self.n):
                curr_val = self.sqr[i][j]
                if curr_val < 1 or curr_val > self.n**2:
                    return False
                if self.frequency(curr_val) > 1:
                    return False
        return True        

    def primes_in_order(self):
        prime = []
        print("\nPrime\tRow\tColumn", sep='')
        for i in range(self.n):
            for j in range(self.n):
                curr = self.sqr[i][j]
                if curr>=2:
                    for k in range(2, curr//2+1):
                        if curr%k==0:
                            break
                    else:
                        prime.append((curr, i+1, j+1))
        prime.sort()
        for i in prime:
            print(i[0],"\t",i[1],"\t",i[2], sep='')

print("To check if the matrix is a wondrous square and display primes along with their positions:")
n = int(input("Enter the number of rows/columns: "))
print()

obj = WondrousSquare(n)
obj.fill_square()

print("\nThe original matrix:")
obj.show_square()
if obj.is_wondrous_square():
    print("\nYes, the matrix represents a Wondrous Square!")
else:
    print("\nNo, the matrix doesn't represent a wondrous square!")
obj.primes_in_order()
print()