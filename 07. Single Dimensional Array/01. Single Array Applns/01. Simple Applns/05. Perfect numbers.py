import os
os.system("cls")

def isPerfect(num):
    ssum = 0
    for i in range(1, num//2+1):
        if num%i==0:
            ssum+=i
    return ssum==num

nums, prfct = [], ""
print("To display perfect numbers present in an array:")
n = int(input("Enter number of elements: "))

print()
for i in range(n):
    print("Enter element #",i+1,": ",sep='', end='')
    nums.append(int(input()))
    if isPerfect(nums[i]):
        prfct+= str(nums[i]) if prfct=="" else ", "+str(nums[i])

print("\nThe array:\n",nums,sep='')

if prfct=="":
    print("\nNo perfect numbers exist in the array!\n")
else:
    print("\nThe Perfect numbers present in the array are:\n",
         prfct,"\n", sep='')
