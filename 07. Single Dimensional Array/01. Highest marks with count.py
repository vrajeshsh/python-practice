import os
os.system("cls")

marks, max_marks, max_count = [], 0, 0

print("To find the highest marks and count of students obtaining it:")
n = int(input("Enter number of students: "))

print()
for i in range(n):
    print("Enter marks of student #", i+1,": ", sep='', end='')
    marks.append(int(input()))

for mks in marks:
    if mks > max_marks:
        max_marks = mks
        max_count= 1
    elif mks == max_marks:
        max_count+= 1

print("\nThe marks as obtained by the students:\n", marks,
    "\n\nThe highest marks obtained: ", max_marks,
        "\nIt's frequency: ", max_count,"\n", sep='')
