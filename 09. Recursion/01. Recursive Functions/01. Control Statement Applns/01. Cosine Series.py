import os
os.system("cls")

def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def power(x, n):
    return 1 if n==0 else x*power(x, n-1)

print("To find the generate the Cosine series \"1-x^2/2!+x^4/4!-x^6/6!...\"")
x = int(input("Enter the value of x: "))
n = int(input("Enter limit: "))

ssum, sign= -1, 1
print("\nThe series till limiting index",n,":")
for i in range(0, n, 2):
    term = power(x, i)/factorial(i)
    sign*= -1
    ssum+= term*sign
    print(term if i==0 else " - "+str(round(term, 3)) if sign<0 else " + "+str(round(term, 3)), end='')
 
print("\nSum: ",round(ssum, 3),"\n", sep='')
