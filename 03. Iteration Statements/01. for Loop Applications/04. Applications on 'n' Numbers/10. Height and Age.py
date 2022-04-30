'''Display height of oldest and age of shortest student'''
print("Display height of oldest and age of shortest student:")
n = int(input("Enter number of students: "))
print()

min_age,min_hi=0,0
for i in range(1,n+1):
    print("Enter height for student #",i,": ",sep='',end='')
    hi = float(input())
    print("Enter age for student #",i,": ",sep='',end='')
    age = float(input())
    max_age,max_hi = 0,0
    if age>max_age:
        max_age=age
        max_hi = hi
    if i==1 or hi<min_hi:
        min_hi=hi
        min_age = age
        
print("\nMax age:",max_age,"and his height:",max_hi,
    "\nMin height:",min_hi,"and his age:",min_age)
    
