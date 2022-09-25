import os
os.system("cls")

n = int(input("Enter number of students: "))
print()
arr=[[0]*12 for i in range(n)]

for i in range(n):
    print("Enter details for participant ",i+1,":", sep='')
    arr[i] = (input().split(", "))

key = input("\nEnter the key: ")
key = key.split(", ")
scores = []
for i in range(n):
    score = 0
    for j in range(10):
        if arr[i][j+2]==key[j]:
            score+=2
        else:
            score-=1
    scores.append(score)

print("\nSTUDENT#\tREGN NO.\tNAME\t\tSCORE")
for i in range(n):
    print(i+1,"\t\t",arr[i][0],"\t",arr[i][1],"\t",scores[i], sep='')

print("\nSTUDENT#\tREGN NO.\tNAME\t\tSCORE\tRANK")
for i in range(n):
    rank = 1
    for j in range(n):
        if scores[i] < scores[j]:
            rank+=1
    rank= "N/A" if scores[i]<1 else rank
    print(i+1,"\t\t",arr[i][0],"\t",arr[i][1],"\t",scores[i],"\t", rank, sep='')

print("\nDetails of the highest scorer(s):",
    "\nSTUDENT#\tREGN NO.\tNAME\t\tSCORE")
for i in range(n):
    if scores[i]==max(scores):
        print(i+1,"\t\t",arr[i][0],"\t",arr[i][1],"\t",scores[i], sep= '')

print()
'''
The SIMPLE RANKING algorithm is explained below;
1. Traverse the array (could be a row/col of a 2-D array also) with an outer loop.  
2. Set the rank counter to 1.
3. With an inner loop check how many times the first element is lesser than any of the other  
   elemets of that same array. Each time it finds one increment the rank counter.
3. At the end of the inner loop you may assign or print (as required) the first element's TRUE RANK  
   through the rank counter.
4. This way the ranks of the rest of the elements can be ascertained.
Now implement this algorithm to your code above.
'''

