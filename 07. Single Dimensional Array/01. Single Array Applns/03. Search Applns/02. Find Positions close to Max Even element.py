import os
os.system("cls")

print("To display the position of largest even integer and also previous and next occurances of even integers:")
n = int(input("Enter the number of elements: "))
print()

nums, isPresent, max_pos, max_even, prev_pos, next_pos = [], False, -1, -1, -1, -1
for i in range(n):
    print("Enter the element #",i+1,": ",sep='',end='')
    nums.append(int(input()))
    if nums[i]%2==0 and nums[i]>max_even:
        prev_pos = max_pos
        max_pos = i
        max_even = nums[i]
    elif nums[i]%2==0 and i>max_pos:
        next_pos = i

print("\nThe array:\n",nums,sep='')
if max_pos!=-1 and next_pos!=-1 and prev_pos!=-1:
    print("\nPosition of the largest even integer: ",max_pos+1,
    "\nPosition of the previous even integer: ",prev_pos+1,
    "\nPosition of the next even integer: ",next_pos+1,"\n",sep='')
else:
    print("\nPosition of the largest even integer: ",max_pos+1,
    "\nNo even integer exists before or after position",max_pos+1,"\n")
