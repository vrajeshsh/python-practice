import os
os.system("cls")

class Student:
    def input(self):
        self.name = input("\nEnter name: ")
        self.rollno = int(input("Enter roll no: "))
        self.age = int(input("Enter age: "))
        self.points = int(input("Enter points: "))
        
    def display(self):
        print("\nThe details of the student:")
        print("\nName: ",self.name,"\nRoll No.: ", self.rollno,
                "\nAge: ", self.age,"\nPoints: ", self.points, sep='')


class Result(Student):
    def input(self):
        super().input()
        self.sub1 = int(input("Enter marks in subject 1: "))
        self.sub2 = int(input("Enter marks in subject 2: "))
        self.sub3 = int(input("Enter marks in subject 3: "))
        self.average, self.total, self.stream = 0.0, 0, "" 
        
    def compute(self):
        self.total = self.sub1 + self.sub2 + self.sub3
        self.average = round(self.total/3, 2)

    def find_grade(self):
        match(self.average):
            case _ if self.average>= 80:
                return "A"
            case _ if self.average >= 60:
                return "B"
            case _ if self.average >= 40:
                return "C"
            case _:
                return "N/A"

    def find_stream(self):
        grade = self.find_grade()
        if self.average>=80 and self.points>=8 and grade=="A":
            self.stream =  "Science with Computers"
        elif self.average>=60 and self.points>=4 and grade=="B":
            self.stream =  "Science with Biology"
        elif self.average>=40 and self.points>=1 and grade=="C":
            self.stream =  "Commerce"
        elif self.average<40 and self.points<3 and grade=="N/A":
            self.stream =  "Admission not granted"

    def display(self):
        super().display()
        # The display format is not as per the expected one, and of very poor quality sort of 'dehati'!!
        # Improve it as per the expected one if possible.
        print("Marks obtained in three subjects:",
            "\nEnglish\tScience\tMathematics\n",
            self.sub1, "\t\t",self.sub2,"\t\t",self.sub3,
            "\nTotal Marks: ",self.total,
            "\nAverage(%): ", self.average,
            "\nGrade: ",self.find_grade(),
            "\nStream: ",self.stream, sep='')

print("To find and display the result and stream of students:")
n = int(input("Enter number of students: "))

obj = Result() 
for i in range(n):
    obj.input()
    obj.compute()
    obj.display()
