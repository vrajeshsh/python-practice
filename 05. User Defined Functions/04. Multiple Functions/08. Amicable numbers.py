import os
os.system("cls")

def aliquotSum(n):
    ssum = 0
    for i in range(1, n//2+1):
        if n%i==0:
            ssum+=i
    return ssum

def areAmicable(n1, n2):
    return (aliquotSum(n1)==n2 and aliquotSum(n2)==n1)

ami=""
begin = start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))

while start<=end:
    if areAmicable(aliquotSum(start), start) and aliquotSum(start)!=start:
        ami+="("+str(start)+", "+str(aliquotSum(start))+")\n"
        start = aliquotSum(start)+1
    else:
        start+=1

if ami=="":
    print("\nNo Amicable pairs exist in the given range!!\n")
else:
    print("\nThe amicable pairs between ", begin, " and ", end," are:\n", ami, sep='')
