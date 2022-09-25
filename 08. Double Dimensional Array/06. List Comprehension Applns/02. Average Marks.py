import os
os.system("cls")

print("To find the average marks of each student and class average in each subject:")
n = int(input("Enter number of sudents: "))

mks = [[0]*3 for i in range(n)]
for i in range(n):
    for j in range(3):
        print("Enter marks for student #",i+1," in subject #",j+1,": ", sep='', end = '')
        mks[i][j] = int(input())

print("\nThe Marks of",n,"students and average of class:\n\nStudent #\tSub 1\tSub 2\tSub 3\tAvg Marks")

for i in range(n):
    print(i+1,"\t\t", end='') 
    for j in range(3):
        print(mks[i][j],"\t",sep='', end='')
    print(round(sum(mks[i])/3,2))
print("Class Avg\t", sep='', end='')
for i in range(3):
    sub_sum = [mark[i] for mark in mks]
    print(sum(sub_sum)/n,"\t", sep='', end='')

print()