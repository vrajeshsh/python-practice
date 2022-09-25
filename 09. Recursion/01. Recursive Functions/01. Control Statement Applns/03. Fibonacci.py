import os
os.system("cls")

def getFibo(n):
    return 0 if n==1 else 1 if n==2 else getFibo(n-2)+getFibo(n-1)

print("To display Fibonacci numbers till a particular limit:")
n = int(input("Enter the limit: "))

ssum = 0
print("\nThe Fibonacci series till",n,":")
for i in range(1, n+1):
    term = getFibo(i)
    if term <= n:
        ssum+= term
        print(term if i==1 else " + "+str(term),sep='', end='')
    else:
        break

print("\nSum: ", ssum,"\n", sep='')
