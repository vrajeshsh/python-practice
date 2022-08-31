import os
os.system("cls")

def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print("To form a matrix using prime numbers in reverse order:")
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix, num = [[0]*c for i in range(r)], 2

for i in range(r-1, -1, -1):
    for j in range(c-1, -1, -1):
        matrix[i][j] = num
        num+=1
        while not isPrime(num):
            num+=1

print("\nThe natural Prime numbers as filled in 2-D array are:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],"\t", end='')
    print()
print()