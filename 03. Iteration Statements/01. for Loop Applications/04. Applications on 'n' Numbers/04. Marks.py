'''To calculate the classes statistics'''

print("To calculate the classes statistics:")
n = int(input("Enter number of students: "))

count1,count2,count3,count4 = 0,0,0,0

for i in range(1,n+1):
	print("Enter marks for student #",i,": ", sep='', end='')
	num = float(input())
	if num>80:
		count1+=1
	if num>60:
		count2+=1
	if num>40:
		count3+=1
	if num < 40:
		count4+=1

print("\nNumber of students who obtained more than 80: ",count1,
"\nNumber of students who obtained more than 60: ",count2,
"\nNumber of students who obtained more than 40: ",count3,
"\nNumber of students who obtained less than 40: ",count4)

# Accepted