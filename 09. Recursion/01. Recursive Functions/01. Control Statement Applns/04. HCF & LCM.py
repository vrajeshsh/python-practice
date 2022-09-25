import os
os.system("cls")

def hcf(x, y):
    return y if x==0 else hcf(y%x, x)

def lcm(x, y):
    lcm.multiple+= y
    return lcm.multiple if lcm.multiple%x==0 and lcm.multiple%y==0 else lcm(x, y)

print("To calculate the HCF and LCM of a set of integers:")
n, Hcf, Lcm = int(input("Enter the no. of numbers: ")), 0, 1

for i in range(n):
    print("Enter integer #",(i+1),": ", sep='', end='')
    num= int(input())
    Hcf= hcf(Hcf, num)  # cyclic call of function
    lcm.multiple= 0
    Lcm= lcm(Lcm, num)

print("\nHCF of ", n," numbers: ",Hcf,
    "\nLCM of ", n," numbers: ",Lcm, "\n", sep='')