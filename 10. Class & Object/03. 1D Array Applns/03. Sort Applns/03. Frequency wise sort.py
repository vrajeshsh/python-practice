import os
os.system('cls')

class SortFrequencyWise():
    def __init__(self, n):
        self.avgMks = []
        self.n = n

    def acceptMarks(self):
        for i in range(self.n):
            print("Enter average marks of student #",i+1,": ", sep='', end='')
            self.avgMks.append(float(input()))

    def displayMarks(self):
        print("\nAverage marks (%) of all students:\n", self.avgMks,sep='')

    def frequency(self, avgMks):
        return self.avgMks.count(avgMks)

    ''' Note:
    1. You are NOT ALLOWED to take any new array
    2. You are NOT ALLOWED to sort the array
    '''
    ''' Swap if the freq1 < fre2. But also check when the two freqs are equal, then check 
    for avg[j] < avg[j+1]. '''  
    
    def sortFreqwise(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.frequency(self.avgMks[i])<self.frequency(self.avgMks[j]) or \
                    (self.frequency(self.avgMks[i])==self.frequency(self.avgMks[j]) \
                        and self.avgMks[i]>self.avgMks[j]) :
                    self.avgMks[i], self.avgMks[j]= self.avgMks[j], self.avgMks[i]
                
        print("\nAfter arranging the numbers frequency-wise:\n", self.avgMks,"\n",sep='')            

print("To arrange the average marks of a class in order of frequency: ")
n = int(input("Enter the number of students: "))

obj = SortFrequencyWise(n)
obj.acceptMarks()
obj.displayMarks()
obj.sortFreqwise()