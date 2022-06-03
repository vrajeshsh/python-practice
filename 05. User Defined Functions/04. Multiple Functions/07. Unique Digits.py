import os
os.system("cls")

def freqOf(dig, num):
    count = 0
    while num>0:
        if num%10==dig:
            count+=1
        num//=10
    return count

def isUnique(num):
    temp = num
    while num>0:
        if freqOf(num%10, temp)>1:
            return False
        num//=10
    return True

unique, count="", 0
start = int(input("Enter the starting limit: "))
end = int(input("Enter the ending limit: "))

for i in range(start, end+1):
    if isUnique(i):
        count+=1
        unique+=str(i) if unique=="" else ", "+str(i)

if count==0:
    print("\nNo unique-digit numbers exist in the given range!!\n")
else:
    print("\nThe unique-digit numbers between", start, "and", end, "are:\n",
        unique,"\n",count,"unique numbers present!\n")