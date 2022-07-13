import os
os.system("cls")

nums, even, odd = [], 0, 0
print("To find the difference between sum of even and odd elements of an array:")
n = int(input("Enter number of elements: "))

print()
for i in range(n):
    print("Enter element #", i+1, ": ", sep='', end='')
    nums.append(int(input()))

for num in nums:
    if num%2 == 1:
        odd+=num
    else:
        even+=num
diff = even-odd

print("\nThe array:\n", nums,
        "\n\nDifference between even and odd elements: ",diff,"\n", sep='')