'''To find topper and trailure in a class'''

print("To find topper and trailure in a class:")
n = int(input("Enter number of students: "))

top_marks, trail_marks=0,0

print()
for i in range(1,n+1):
    print("Enter details of Student #",i,": ",sep='')
    name = input("Name: ")
    sex = input("Gender [(M)ale/(F)emale]: ")
    reg = input("Registration no.: ")
    marks = float(input("Average Marks: "))
    if marks>top_marks:
        top_marks=marks
        top_name = name
        top_sex = sex
        top_reg = reg
    if i==1 or marks<trail_marks:
        trail_marks = marks
        trail_name = name
        trail_sex = sex
        trail_reg = reg

print("\n\t\t\tTOPPER DETAILS\t\tTRAILOR DETAILS",
    "\nNAME:\t\t\t",top_name,"\t\t\t",trail_name,
    "\nGENDER:\t\t\t",top_sex,"\t\t\t",trail_sex,
    "\nREGISTRATION NUMBER:\t",top_reg,"\t\t\t",trail_reg,
    "\nAVERAGE MARKS:\t\t",top_marks,"\t\t\t",trail_marks)

# Accepted after layout and English Grammer changes