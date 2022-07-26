import os
os.system("cls")

def factorCount(n):
    if n < 1:
        return 0
    facCnt = 1
    for i in range(1, n//2+1):
        if n%i==0:
            facCnt+=1
    return facCnt

print("To check whether number is Prime, Composite or neither based on number of factors")
n = int(input("Enter number of elements: "))
print()

nums, facs = [], []
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))
    facs.append(factorCount(nums[i]))

print("\nThe original array:\n", nums,
    "\n\nFac[]:\n", facs,"\n", sep='')
print("INTEGER\t\tFACTORS\t\tSTATUS")
for i in range(n):
    status = "Prime number" if facs[i] == 2 else \
        "Neither Prime nor Composite number" if facs[i]<2 else "Composite number"
    print(nums[i],"\t\t",facs[i],"\t\t", status, sep='')

print()