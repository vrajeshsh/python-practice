import os
os.system("cls")

def naturalsum(n):
    if n==1:
        return 1
    return n+naturalsum(n-1)

print("To display the Triangular number series and its sum:")
n = int(input("Enter the number of terms: "))

ssum = 0
print("\nTriangular number series uptil ",n," terms:", sep='')
for i in range(1, n+1):
    term = naturalsum(i)
    ssum+=term
    print(term if i==1 else " + "+str(term), sep='', end = '')

print("\nSum: ",ssum,"\n", sep='')