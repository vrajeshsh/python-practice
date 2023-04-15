import os
os.system("cls")

class StudentList:
    def __init__(self, n):
        self.name, self.avg_marks = [], []
        self.n = n

    def input(self):
        for i in range(self.n):
            print("\nEnter details for student #", i+1,":", sep='')
            self.name.append(input("Name: "))
            self.avg_marks.append(float(input("Average Marks: ")))

    def sort_records(self):
        self.name, self.avg_marks = zip(*sorted(zip(self.name, self.avg_marks)))
        return self.name

    def get_rank(self, index):
        rank = 0
        for i in range(self.n):
            if self.avg_marks[index]>35:
                if self.avg_marks[index]<self.avg_marks[i]:
                    rank+=1
            else:
                rank = -1
        return rank+1 if rank !=-1 else "N/A"

    def display(self):
        self.sort_records()
        print("\nNAME\t\tAVG MARKS(%)\tRANK",sep='')
        for i in range(self.n):
            print(self.name[i],"\t", self.avg_marks[i],"\t\t",self.get_rank(i))

print("To display Names of students in alphabetical order along with their ranks")
n = int(input("Enter the number of students: "))

obj = StudentList(n)
obj.input()
obj.display()
print()