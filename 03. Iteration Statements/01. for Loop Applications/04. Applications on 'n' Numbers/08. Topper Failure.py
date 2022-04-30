'''To find topper and failure in a class'''

print("To find topper and failure in a class:")
n = int(input("Enter number of students: "))

top_marks,fail_marks=0,0

print()
for i in range(1,n+1):
    print("Enter Name of student #",i,": ",sep='',end='')
    name = input()
    print(name,"'s Gender: ",sep='',end='')
    sex = input()
    print(name,"'s Registration Number: ",sep='',end='')
    reg = input()
    print(name,"'s Average Marks: ",sep='',end='')
    marks = float(input())
    if marks>top_marks:
        top_marks=marks
        top_name = name
        top_sex = sex
        top_reg = reg
    if i==1 or marks<fail_marks:
        fail_marks = marks
        fail_name = name
        fail_sex = sex
        fail_reg = reg

print("\n\t\t\tTOPPER DETAILS\t\tFAILURE DETAILS\nNAME:\t\t\t",top_name,"\t\t\t",fail_name,
    "\nGENDER:\t\t\t",top_sex,"\t\t\t",fail_sex,
    "\nREGISTRATION NUMBER:\t",top_reg,"\t\t\t",fail_reg,
    "\nAVERAGE MARKS:\t\t",top_marks,"\t\t\t",fail_marks)
