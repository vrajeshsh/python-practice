'''To calculate grade of class based on percentage marks'''

print("To calculate grade of class based on percentage marks:")
n = int(input("Enter number of students: "))

print()
for i in range(1,n+1):
    print("Enter Percentage for student #",i,": ", sep='', end='')
    num = float(input())
    if num<40:
    	grade = 'F'
    elif num <50:
    	grade='E'
    elif num<60:
    	grade='D'
    elif num <70:
    	grade='C'
    elif num<80:
    	grade='B'
    else:
    	grade='A'

    print("Grade: ",grade)

    # Accepted