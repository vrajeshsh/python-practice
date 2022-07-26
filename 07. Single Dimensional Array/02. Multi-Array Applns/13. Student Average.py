import os
os.system("cls")

print("To display a class's report card:")
n = int(input("Enter number of students: "))

rolls, names, sem1mks, sem2mks, sem3mks, avg = [], [], [], [], [], []
for i in range(n):
    print("\nEnter following details for student #",i+1,": ", sep='')
    rolls.append(int(input("Roll No.: ")))
    names.append(input("Name: "))
    sem1mks.append(float(input("Marks in Semester 1: ")))
    sem2mks.append(float(input("Marks in Semester 2: ")))
    sem3mks.append(float(input("Marks in Semester 3: ")))
    avg.append(round((sem1mks[i]+sem2mks[i])*0.3+sem3mks[i]*0.4),3)
    
print("\n#\tROLL NO.\tNAME\t\tSEM 1\tSEM 2\tSEM 3\tAVG(%)")
for i in range(n):
    print(i+1,".","\t",rolls[i],"\t\t", names[i],"\t",\
        sem1mks[i],"\t",sem3mks[i],"\t",sem3mks[i],"\t",avg[i], sep='')
print("\nDetails of the students who obtained more than 85% average(%) marks:")
print("#\tROLL NO.\tNAME\t\tSEM 1\tSEM 2\tSEM 3\tAVG(%)")
for i in range(n):
    if avg[i]>85:
        print(i+1,".","\t",rolls[i],"\t\t", names[i],"\t",\
            sem1mks[i],"\t",sem3mks[i],"\t",sem3mks[i],"\t",avg[i], sep='')
print("\nDetails of the students who obtained less than 35% average(%) marks:")
print("#\tROLL NO.\tNAME\t\tSEM 1\tSEM 2\tSEM 3\tAVG(%)")
for i in range(n):
    if avg[i]<35:
        print(i+1,".","\t",rolls[i],"\t\t", names[i],"\t",\
            sem1mks[i],"\t",sem3mks[i],"\t",sem3mks[i],"\t",avg[i], sep='')
print()