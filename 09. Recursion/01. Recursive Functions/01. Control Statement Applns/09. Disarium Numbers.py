import os
os.system("cls")

def power(x, y):
    return 1 if y==0 else x*power(x, y-1)

def digitcount(n):
    return 0 if n==0 else 1+digitcount(n//10)

print("To check if a number is Disarium number or not")
temp = n = int(input("Enter the number: "))

cnt, ssum = digitcount(n), 0

while temp>0:
    dig = temp%10
    ssum+= power(dig, cnt)
    cnt-=1
    temp//=10

print("\n",n," is ", "" if ssum==n else "NOT ", "a Disarium number.\n", sep='')