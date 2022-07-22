import os
os.system("cls")

print("To find the height of the oldest and age of the shortest:")
n = int(input("Enter number of students: "))
print()

age, hgt, max_age, min_hgt = [], [], 0, 200
for i in range(n):
    print("Enter age of student #", i+1,": ", end='', sep='')
    age.append(int(input()))
    print("Enter height of student #", i+1,": ", end='', sep='')
    hgt.append(int(input()))
    if age[i]>max_age:
        oldestHgt = hgt[i]
        max_age = age[i]
    if hgt[i]<min_hgt:
        shortestAge = age[i]
        min_hgt = hgt[i]
        
print("\nThe height of the oldest student: ",oldestHgt," cms",
        "\nThe age of the shortest student: ", shortestAge," years\n", sep='')

'''
Think for a while!

For killing two mosquitoes, you're firing Bofors Guns Vrajesh?
Why two extraneous functions for such a trivial problem solution?

Understand why most US Faculty members ban functions. Most functions like max() etc. are LOOP INVOKING.
And loops are the root cause for slow and inefficient codes.
That's why!!
'''