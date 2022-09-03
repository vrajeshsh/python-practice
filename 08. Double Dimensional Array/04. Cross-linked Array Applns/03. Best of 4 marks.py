import os
os.system("cls")


subjects = [[""]*3 for i in range(6)]  # Wouldn't have developed this habit if you had only continued... the 2-D classes...
# Lost total track... almost like sinking in the mid-sea and catching this style as the last straw!!

for i in range(6):
    print("\nEnter the details for subject #",(i+1),":", sep='')
    # subjects[i][0] = input("Enter code: ")
    # subjects[i][1] = input("Enter name: ")
    subjects[i][2] = int(input("Enter marks: "))

print("\nThe details of the subjects as given by the user:\n\nSUBJECT #\t\tSUBJECT CODE\t\tSUBJECT NAME\t\tMARKS SCORED")
for i in range(6):
    print(i+1,"\t\t\t",subjects[i][0],"\t\t\t",subjects[i][1],"\t\t\t", subjects[i][2],sep='')

sec_min, mini, min_loc, sec_min_loc = 101, 101, 0, 0
for i in range(6):
    if subjects[i][2]<mini:
        sec_min = mini
        mini = subjects[i][2]
        sec_min_loc = min_loc
        min_loc = i
        
        
    if i!=min_loc and sec_min>subjects[i][2]:
        sec_min = subjects[i][2] 
        sec_min_loc = i

print("\nThe details of the best 4 subjects of the candidate:\n\nSUBJECT #\tSUBJECT CODE\t\tSUBJECT NAME\t\tMARKS SCORED")
for i in range(6):
    if i!=min_loc and i!=sec_min_loc:
        print(i+1,"\t\t",subjects[i][0],"\t\t",subjects[i][1],"\t\t", subjects[i][2],sep='')

'''
Pretty dangerous algorithm used above!! 
Suppose a poor fellow (but extremely studious and intelligent student) obtained marks as 100 and 99
in all the 6 subjects e.g. 100, 100, 100, 100, 99, 99
Your code is powerful enough to send him to Ranchi Asylum straight!!
Understand what bright dreams he had about his life!! All becoming shattered, he will loose his mind
and will definitely land up in the asylum only...
And the saddest part is he will stay there life long... because he has no one to cure him or take
care of him!!
'''        