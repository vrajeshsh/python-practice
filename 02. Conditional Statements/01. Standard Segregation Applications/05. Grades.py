'''To calculate average marks and grades obtained'''

print("To calculate the average marks and find the grades for students:")
name = input("Enter name of student:")
phy = float(input("Marks in Physics: "))
chem = float(input("Marks in Chemistry: "))
bio = float(input("Marks in Biology: "))

avg = (phy+chem+bio)/3
if avg < 40:
	grade = "Promotion not granted"
elif avg < 45:
	grade = "Pass"
elif avg < 60:
	grade = "Second Division"
elif avg < 80:
	grade = "First Division"
else:
	grade = "Distinction"

print("\nNAME: ",name,
	"\nAVERAGE (%) MARKS: ",round(avg,2),"%",
	"\nGRADE OBTAINED: ",grade)
