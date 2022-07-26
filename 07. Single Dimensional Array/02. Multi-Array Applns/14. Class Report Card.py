import os
os.system("cls")

print("To display the report card of the class:")
n = int(input("Enter number of setudents: "))
print()

names, avgmks, ranks = [], [], []
for i in range(n):
    print("\nEnter following details for student #",i+1,": ", sep='')
    #names.append(input("Name: "))
    avgmks.append(float(input("Avg Marks: ")))
    
# You do not need to sort to get the ranks...
# Assign the ranks and then sort in alphabetical order of names
# okay sir
actual_rank, rank, curr = 0, 0, 0
for i in avgmks:
    rank+=1
    if i!=curr:
        curr = i
        actual_rank = rank
    print(curr, actual_rank)


print(ranks)
'''
Set a loop to traverse the marks...
Find out how many students have obtained more than the current student's marks.
Rank will be the count + 1. (may take the count directly as rank too)
Now proceed...
Say if 98 is the higeshtmarks. On scanning we will find that its more than none
That is the count will be 0. So the rank is 0+1 = 1.
'''