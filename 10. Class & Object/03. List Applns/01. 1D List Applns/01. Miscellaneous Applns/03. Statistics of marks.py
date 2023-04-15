import os
os.system('cls')

class MarksStatistics():
    def __init__(self, n):
        self.marks = []
        self.n = n

    def accept(self):
        for i in range(self.n):
            print("Enter marks obtained by student #",i+1,": ",sep='', end='')
            self.marks.append(int(input()))

    def display(self):
        print("\nMarks obtained by students: ",self.marks,"\n", sep='')
        print("The mean of marks obtained by class: ", self.mean(), sep='')
        print("The median of marks: ",self.median(), sep='')
        print("The mode of marks is ",self.mode(),".\n", sep='')

    def frequency(self, mks):
        return self.marks.count(mks)

    def mean(self):
         return round(sum(self.marks)/self.n, 2)

    def median(self):
        mks= sorted(self.marks)   # safeguarding the class member and sorting as THIS IS A REQUIREMENT here
        return (mks[self.n//2]+mks[self.n//2+1])//2 if self.n%2==0 else mks[self.n//2]
    
    def mode(self):
        maxFreq, mode = 0, 0
        for i in range(self.n):
            freq= self.frequency(self.marks[i])
            if freq > maxFreq:
                maxFreq = freq
                mode = self.marks[i] 
            elif freq == maxFreq:
                mode = max(mode, self.marks[i])  #If there are 2 or more modes in a list then the highest one is taken
        return mode

print("To display the mean, median and mode of the marks obtained by a class:")
n = int(input("Enter number of students: "))

obj = MarksStatistics(n)
obj.accept()
obj.display()
