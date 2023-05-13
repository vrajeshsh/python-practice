import os
os.system('cls')

class Scholar():
    def __init__(self):
        self.adm_num = self.name = self.stream = ""
        self.subjects, self.marks = [], []

    def accept(self):
        self.adm_num = input("Enter admission number: ")
        self.name = input("Enter name: ")
        self.stream = input("Enter stream: ")
        print("\nSubject Names: ")
        for i in range(6):
            print("Enter subject #",i+1,": ", sep='', end='')
            self.subjects.append(input())
        print("\nStudent Marks: ")
        for j in range(6):
            print("Enter marks in ",self.subjects[j],": ", sep='', end='')
            self.marks.append(int(input()))

    def display(self):
        print("\n",self.adm_num,"\t\t", self.name,"\t\t", self.stream,"\t\t",sep='', end='')
        for mks in self.marks:
            print(mks,"\t", sep='', end='')
    ''' The below algorithm works on an assumption that the marks obtained by the students are
        unique. Probably if the highest or the second highest marks repeat, it might just crash.
    '''
    def get_best_scores(self):
        bestscores, max1, max2, max3, max1pos, max2pos, max3pos = [["", 0] for i in range(4)], 0, 0, 0, 0, 0, 0
        bestscores[0][0] = "English"
        bestscores[0][1] = self.marks[0]
        for i in range(1, 6):
            if self.marks[i]>max1:
                max3 = max2
                max2 = max1
                max1 = self.marks[i]
                max3pos = max2pos
                max2pos = max1pos
                max1pos = i
            elif self.marks[i]>max2:
                max3 = max2
                max2 = self.marks[i]
                max3pos = max2pos
                max2pos = i
            elif self.marks[i]>max3:
                max3 = self.marks[i]
                max3pos = i
        bestscores[1][0] = self.subjects[max1pos]
        bestscores[1][1] = self.marks[max1pos]
        bestscores[2][0] = self.subjects[max2pos]
        bestscores[2][1] = self.marks[max2pos]
        bestscores[3][0] = self.subjects[max3pos]
        bestscores[3][1] = self.marks[max3pos]
        return bestscores

class BestScores():
    def __init__(self):
        self.students = []

    def add_to_list(self):
        n = int(input("Enter the number of students: "))
        for i in range(n):
            student = Scholar()
            print("\nEnter details for Student #", i+1,": ", sep='')
            student.accept()
            self.students.append(student)

    def show_list(self):
        for student in self.students:
            student.display()
        print()

    def show_best_scores(self): 
        for student in self.students:
            total = 0
            print("\n",student.name,"'s best four scores: ", sep='')
            print("\nSubject\t\t\tMarks\n", sep='')
            scores = student.get_best_scores()
            for i in range(4):
                print(scores[i][0], "\t\t", scores[i][1])
                total+=scores[i][1]
            print("\nThe average: ",round((total/4),2), sep='')

print("To display the best four marks and subject names along with their average: ")
obj = BestScores()
obj.add_to_list()
print("\nAdmission No.\tName\t\t\tStream\t\tEnglish\tVern\tElect 1\tElect 2\tElect 3\tOptional")
obj.show_list()
obj.show_best_scores()
print()