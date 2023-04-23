import os
os.system('cls')

class Student():
    def __init__(self):
        self.regNum = ""
        self.name = ""
        self.marks = []

    def get_details(self):
        self.regNum = input("Enter Registration Number: ")
        if self.regNum=="":
            return 0
        self.name = input("Enter Name: ")
        self.marks.append(int(input("Enter marks obtained in English: ")))
        self.marks.append(int(input("Enter marks obtained in main elective 1: ")))
        self.marks.append(int(input("Enter marks obtained in main elective 2: ")))
        self.marks.append(int(input("Enter marks obtained in main elective 3: ")))
        self.marks.append(int(input("Enter marks obtained in Optional subject: ")))

    def show_details(self):
        print("\n", self.regNum, "\t", self.name, "\t\t", end= '')
        for mks in self.marks:
            print(mks, "\t", end= '')
        print(self.get_average(), "\t", self.get_point(), "\t", self.get_grade(),"\t", self.get_stream())

        '''
        print(self.regNum,"\t", self.name, "\t\t", self.students[i].marks[0], "\t", self.students.marks[1], "\t", self.students.marks[2],\
            "\t",self.students[i].marks[3],"\t", self.students[i].marks[4],"\t", self.students[i].get_average(),\
                "\t",self.students.get_points[i],"\t",self.students[i].get_grade(),"\t",self.students[i].get_stream(),\
                     sep='')
        '''
    def get_average(self):
        return sum(self.marks)/5

    def get_point(self):
        avg = self.get_average()
        return 1 if avg==100 else 10 - int(avg//10)

    def get_grade(self):
        avg = self.get_average()
        return "Distinction" if avg>=80 else "First Division" if avg>=60 else "Second Division" \
            if avg>=45 else "Pass" if avg>=40 else "Promotion not granted"

    def get_stream(self): #Use nested if statement for better handling...
        avg, opnl = self.get_average(), self.marks[4]
        if avg>=85:
            return "Maths with Comp Sc." if opnl>=90 else "Bio Sc."
        elif avg >= 75:
            return "Bio Sc." if opnl >= 80 else "Commerce w/ Math"
        elif avg >= 60:
            return "Commerce w/ math" if opnl >= 40 else "Not eligible for Std XI"
        else:
            return ""

class StudentList:

    def __init__(self):
        self.students = []

    def fill_list(self):
        print("To calculate the performance grade & stream of student and display students based on their stream:")
        n= int(input("Enter the number of students: "))
        for i in range(n):
            student= Student()
            print("\nEnter the details for Student #", (i+1),": ", sep='')
            student.get_details()
            self.students.append(student)

    def show_list(self):
        print("\n\nREG NUM\tNAME\t\t\tENG\tME 1\tME 2\tME 3\tOPLN\tAVG\tPOINTS\tGRADE\t\tSTREAM", sep='')
        for student in self.students:
            student.show_details()

        '''
        for i in range(len(self.students)):
            #print(self.students[i].regNum,"\t", self.students[i].name,sep='')
            print(self.students[i].regNum,"\t", self.students[i].name, "\t\t", self.students[i].marks[0], "\t", self.students.marks[1], "\t", self.students.marks[2],\
            "\t",self.students[i].marks[3],"\t", self.students[i].marks[4],"\t", self.students[i].get_average(),\
                "\t",self.students.get_points[i],"\t",self.students[i].get_grade(),"\t",self.students[i].get_stream(),\
                     sep='')
         '''   
    def split_list(self):
        # Showing how the student list should be split below but with two lists... rem 2 please do yourself
        comp_sc, bio_sc, comm, ineligible = StudentList(), StudentList(), StudentList(), StudentList()
        for student in self.students:
            stream = student.get_stream()
            if stream == "Maths with Comp Sc.":
                comp_sc.students.append(student)
            elif stream == "Bio Sc.":
                bio_sc.students.append(student)
            elif stream == "Commerce w/ Math":
                comm.students.append(student)
            elif stream == "Not eligible for Std XI":
                ineligible.students.append(student)
        
        print("\nMaths with Comp Sc.:")
        comp_sc.show_list()
        print("\nBio Sc.:")
        bio_sc.show_list()
        print("\nCommerce w/ Math:")
        comm.show_list()
        print("\nIneligible:")
        ineligible.show_list()

student_list = StudentList()
student_list.fill_list()

print("\nThe processed student list with points, grade and stream:")
student_list.show_list()
student_list.split_list()