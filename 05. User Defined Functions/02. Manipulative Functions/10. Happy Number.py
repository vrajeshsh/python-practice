import os
os.system("cls")

def isHappyNumber(num):
    ssum=10
    while ssum>9:
        ssum=0
        while num>0:
            ssum+=(num%10)**2
            num//=10
        num=ssum
    return ssum==1

i, nums = 0, ""
start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))

for i in range(start, end+1):
    if isHappyNumber(i):
        nums+=str(i) if nums=="" else ", "+str(i)

print("\nHappy numbers found between ",start," and ",end," are:\n",
    "NONE" if nums=="" else nums,"\n",sep='')