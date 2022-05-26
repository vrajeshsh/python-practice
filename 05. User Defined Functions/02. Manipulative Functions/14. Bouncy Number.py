import os, math
os.system("cls")

def isBouncy(num):
    asc = 0
    asc, desc = True, True
    dig = num%10
    num//=10
    while num>0:
        dig2 = num%10
        if dig==dig2:
            dig=dig2
            num//=10
        elif dig2>dig:
            desc = False
        else:
            asc = False
        dig=dig2
        num//=10
    
    return not (asc or desc)
        
bouncy=""
start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))

for i in range(start, end+1):
    if isBouncy(i):
        bouncy+=str(i) if bouncy=="" else ", "+str(i)

if bouncy=="":
    print("\nNo Bouncy numbers found in the given range.\n")
else:
    print("\nBouncy number between", start,"and",end,"are:\n",bouncy,"\n", sep='')
        