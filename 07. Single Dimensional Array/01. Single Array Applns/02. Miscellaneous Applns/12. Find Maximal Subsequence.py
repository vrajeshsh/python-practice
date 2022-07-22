import os
os.system("cls")

print("To calculate the maximum subsequence in an array:")
n = int(input("Enter number of elements: "))
print()

nums = []
for i in range(n):
    print("Enter element #", i+1,": ", sep='', end='')
    nums.append(int(input()))

maxsum, maxseq, startpos, endpos = 0, "", 0, 0
for i in range(n):
    subsum, subseq = 0, ""
    for j in range(i, n):
        subsum+= nums[j]
        subseq+= str(nums[j])+" "
        if maxsum < subsum:
            maxsum, maxseq, start, end = subsum, subseq, i+1, j+1
            
print("\nMaximal subsequence:",maxseq,
    "\nSum:", maxsum,
    "\nStart index:", start,
    "\nEnd index:", end)
