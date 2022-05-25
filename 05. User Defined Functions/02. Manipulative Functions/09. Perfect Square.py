import os
os.system("cls")

def isPerfectSquare(num): #Can you make the below code wind up in ONE LINE? Try once. okay sir
    return (int(num**0.5))**2==num and num>0

count, i, squares = 0, 0, ""
n = int(input("Enter the value of 'n' to find the first 'n' Perfect Squares: "))
while count < n:
    i+=1
    if isPerfectSquare(i):
        count+=1
        squares+=str(i) if squares=="" else ", "+str(i)

print("\nThe first ",count," Perfect Square(s) are:\n",squares,"\n",sep='')