import os
os.system("cls")

class Student():
    def __init__(self, name, rollno, mks1, mks2, mks3):
        self.name = name
        self.rollno = rollno
        self.mks1 = mks1
        self.mks2 = mks2
        self.mks3 = mks3
        self.avg = 0


    def computeGrade(self):
        self.avg = (self.mks1+self.mks2+self.mks3)/3
        if self.avg>=80:
            return 'A'
        elif self.avg>=60:
            return 'B'
        elif self.avg>=40:
            return 'C'
        else:
            return 'D'
    
    def display(self):
        grade = self.computeGrade()
        print("\n\t\tREPORT CARD\n\nName: ",self.name,"\nRoll No.: ",self.rollno,
            "\nSubject 1: ",self.mks1,"\nSubject 2: ",self.mks2,
            "\nSubject 3: ",self.mks3,"\n\nAverage: ",round(self.avg,3),
            "\nGrade: ",grade,"\n")

print("To calculate the grade of a student:")
name = input("Enter name of student: ")
rollno = input("Enter Roll No.: ")
mks1 = int(input("Ente marks in subject 1: "))
mks2 = int(input("Ente marks in subject 2: "))
mks3 = int(input("Ente marks in subject 3: "))
obj = Student(name, rollno, mks1, mks2, mks3)
obj.display()
        
