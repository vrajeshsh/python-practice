import os
os.system("cls")

class MarksRanker():
    def __init__(self, n):
        self.avg_mrks = []
        self.n = n

    def acceptMarks(self):
        for i in range(self.n):
            print("Enter average marks of student #",i+1,": ", sep='', end='')
            self.avg_mrks.append(float(input()))

    def showMarks(self):
        print("\nAverage marks (%) of all students:\n", self.avg_mrks,sep='')
        
    def arrangeMarks(self):
        return sorted(self.avg_mrks, reverse=True)

    def showMarksWithRanks(self):
        sorted_marks, rank = self.arrangeMarks(), 1
        print("\nThe marks of the students along with the allotted ranks:",
            "\nSTUDENT #\tAVG(%) MARKS\t\tRANK IN CLASS")
        for i in range(self.n):
            if sorted_marks[i]>35:
                if i > 0 and sorted_marks[i] < sorted_marks[i-1]:
                    rank+= 1
            else:
                    rank= 0
            print((i+1), 3*"\t", sorted_marks[i], 4*"\t", "N/A" if rank==0 else rank, sep='')

print("To display average marks of a class in descending order and assign them ranks:")
n = int(input("Enter number of students: "))

obj = MarksRanker(n)
obj.acceptMarks()
obj.showMarks()
obj.showMarksWithRanks()
print()