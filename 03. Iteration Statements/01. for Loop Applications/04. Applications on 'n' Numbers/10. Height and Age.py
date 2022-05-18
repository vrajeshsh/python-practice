'''Display height of oldest and age of shortest student'''

print("Display height of oldest and age of shortest student:")
n = int(input("Enter number of students: "))
print()

max_age, max_hgt, min_age, min_hgt=0, 0,0,0
for i in range(1,n+1):
    print("\nEnter the details of Student #",i,": ", sep='')
    hi = float(input("Height (in cms): "))
    age = float(input("Age (in years): "))
    if age > max_age:
        max_age = age
        max_hgt = hi
    if i==1 or hi < min_hgt:
        min_hgt = hi
        min_age = age
        
print("\nThe height of the oldest student: ",max_hgt,
    "\nThe age of the shortest student :",min_age)
