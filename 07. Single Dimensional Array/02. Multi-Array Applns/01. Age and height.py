import os
os.system("cls")

age, hgt, maxindx, minindx = [], [], 0, 0

print("To find the height of the oldest and age of the shortest:")
n = int(input("Enter number of students: "))
for i in range(n):
    print("\nEnter the details of Student #", i+1,": ", sep='')
    age.append(int(input("Enter age (in years): ")))
    hgt.append(int(input("Enter height (in cms): ")))
    if age[i] > age[maxindx]:
        maxindx = i
    if hgt[i] < hgt[minindx]:
        minindx = i

print("\nSTUDENT #\tAGE (YRS)\tHEIGHT (CMS)")
for i in range(n):
    print((i+1), "\t"*3, age[i], "\t"*3, hgt[i], sep='')
print("\nThe height of the oldest student: ",hgt[maxindx]," cms",
        "\nThe age of the shortest student: ", age[minindx]," years\n", sep='')
