import os
os.system("cls")

print("To find lucky numbers:")
n = int(input("Enter a number: "))

nums = []
for i in range(1, n+1):
    nums.append(i)

print("\nThe original array:\n", nums,sep='')

pos, sufx = 2, ""

while pos <= len(nums):
    i = pos-1
    while i< len(nums):
        nums.pop(i)
        i+= pos-1
    sufx = "st" if pos%10==1 and pos!=11 else "nd" if pos%10==2 and pos!=12 \
        else "rd" if pos%10==3 and pos!=13 else "th"
    print("\nPhase #", (pos-1)," After deleting every ", pos, sufx, " element:\n",
    nums, sep='')
    pos+= 1

print("\nHence the Lucky Numbers saved from deletion are:\n", nums, "\n", sep='')
