import os
os.system("cls")

print("To find the median of a given list of numbers:")
n = int(input("Enter the number of marks: "))
print()

nums = []
for i in range(n):
    print("Enter marks #",i+1,": ",sep='', end='')
    nums.append(int(input()))

print("\nThe marks:\n",nums,sep='')
nums.sort()
mid = (nums[n//2-1] + nums[n//2])/2 if n%2==0 else nums[n//2]

print("\nSorted Marks:\n",nums,
        "\n\nThe median of marks: ",mid,"\n",sep='')

'''
I: 12 23 45 67 89 100
O: (45+67)/2 = 56

I: 12 23 45 67 100
O: 45
'''