import os, math
os.system("cls")

def digitCount(num):
    return int(math.log10(num)+1)

def isDeserium(num):
    temp, ssum, count = num, 0, digitCount(num)
    while(temp>0):
        ssum+=(temp%10)**count
        count-=1
        temp//=10
    return ssum == num

num = int(input("Enter ending limit: "))

print("\nDeserium numbers from 1 to",num,":\n")
for i in range(1, num+1):
    if(isDeserium(i)):
        print(i," ",end='')
