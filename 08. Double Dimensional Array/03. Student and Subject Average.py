import os
os.system("cls")

n = int(input("Enter number of students: "))

mks = []
for i in range(n):
    _ = []
    for j in range(3):
        elem = int(input("Enter for Student #"+str(i+1)+
            " and subject #"+str(j+1)+": "))
        _.append(elem)
    mks.append(_)

sub_avg = ""
print("\nThe marks and average of class:\n\nStudent#\tSub1\tSub2\tSub3\tAvg Marks")
for i in range(n):
    ssum, sub_sum = 0, 0
    print(i+1,"\t\t", end='')
    for j in range(3):
        ssum+= mks[i][j]
        sub_sum+= mks[j][i]
        print(mks[i][j],"\t",end='')
    print(round(ssum/3, 3))
    sub_avg+=str(sub_sum/n)+"\t"
print("\nSubject Avg\t",sub_avg,"\n",sep='')
