import os
os.system("cls")

def isPerfect(num):
    ssum = 0
    global facs
    facs= ""
    for i in range(1, num//2+1):
        if num%i==0:
            facs+= str(i) if i==1 else "+"+str(i)
            ssum+=i
    return ssum==num

start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))

perfectNos= ""

for i in range(start, end+1):
    if isPerfect(i):
        perfectNos+= "\n"+str(i)+" = "+facs
    
if perfectNos == "":
    print("\nNo Perfect number exists between", start,"and", end,"!\n")
else:
    print("\nPerfect numbers present between",start,"and",end,"are:",
        perfectNos,"\n")
