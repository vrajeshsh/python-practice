import os
os.system("cls")

i, apcnt, acnt, bcnt, ccnt, dcnt, ecnt, fcnt,grade = 0, 0, 0, 0, 0, 0, 0, 0,''
print("Go on entering the students' marks... Hit the 'Enter; key for name to STOP.")
while True:
    i+= 1
    print("\nEnter the details of Student #",i,": ", sep='')
    name = input("Enter name of student: ")
    if name=="":
        break
    marks1 = int(input("Enter marks obtained in subject 1: "))
    marks2 = int(input("Enter marks obtained in subject 2: "))
    marks3 = int(input("Enter marks obtained in subject 3: "))
    
    avg = (marks1+marks2+marks3)/3
    
    if avg>=90:
        grade = 'A+'
        apcnt+=1   
    elif avg>=80:
        grade = 'A'
        acnt+=1
    elif avg>=70:
        grade = 'B'
        bcnt+=1
    elif avg>=60:
        grade = 'C'
        ccnt+=1
    elif avg>=50:
        grade = 'D'
        dcnt+=1
    elif avg>=40:
        grade = 'E'
        ecnt+=1
    else:
        grade = 'F'
        fcnt+=1
    print("\nRESULT:\nName:\t",name,"\nAverage:\t",avg,"\nGrade:\t",grade)

print("\n\nCLASS STATISTICS\nGRADE\t\tCOUNT\n90 - 100\t",apcnt,
"\n80 - 89\t\t",acnt,"\n70 - 79\t\t",bcnt,"\n60 - 69\t\t",ccnt,"\n50 - 59\t\t",dcnt,
"\n40 - 49\t\t",ecnt,"\nBelow 40\t",fcnt,sep='')
