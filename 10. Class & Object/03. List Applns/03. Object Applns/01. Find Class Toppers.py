import os
os.system("cls")

class Student():
    def __init__(self, adm_num, name, mks):
        self.adm_num = adm_num
        self.name = name
        self.marks = mks

    def display(self):
        print(self.adm_num,"\t",self.name,"\t\t", self.marks[0],"\t", self.marks[1], "\t", self.marks[2], "\t", self.marks[3], "\t", self.marks[4], "\t",self.get_total(), sep='')

    def get_total(self):
        return sum(self.marks)

    def showTopper(self, students):
        total = [student.get_total() for student in students]
        maxi = max(total)
        toppers = [student for student in students if student.get_total()==maxi]
        for topper in toppers:
            topper.display()

print("To display the toppers of a class, enter 'esc' in admission number to exit:")
students = []
while True:
    print("\nEnter details for Student #",len(students)+1,": ", sep='')
    adm_num = input("Enter Admission Number: ")
    if adm_num.lower() == 'esc':
        break
    name = input("Enter Name: ")
    mrks = [] # Take a loop for the below block
    mrks.append(int(input("Marks in English: ")))
    mrks.append(int(input("Marks in Vernacular: ")))
    mrks.append(int(input("Marks in Science: ")))
    mrks.append(int(input("Marks in Maths: ")))
    mrks.append(int(input("Marks in Computers: ")))
    student = Student(adm_num, name, mrks)
    students.append(student)

print("\nThe given list of students:")
print("#  Admn No.\t\tName\t\tEnglish\tVernacular\tScience\tMaths\tComputers\tTotal\n", sep='')
for student in students:
    student.display()

print("\nThe details of the Topper(s) of the class:")
print("#  Admn No.\t\tName\t\tEnglish\tVernacular\tScience\tMaths\tComputers\tTotal\n", sep='')
student.showTopper(students)
print()