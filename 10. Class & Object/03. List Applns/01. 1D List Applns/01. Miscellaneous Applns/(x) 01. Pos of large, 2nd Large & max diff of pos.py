import os
os.system("cls")

class ListOperations():
    def __init__(self, n):
        self.num = []
        self.num_len = n

    def fill_list(self):
        for i in range(self.num_len):
            print("Enter number for element #",i+1,": ",sep='', end='')
            self.num.append(int(input()))

    def show_list(self):
        print("\nThe given list: ",self.num,"\n", sep='')

    def index_highest(self):
        print("The largest number ",max(self.num)," occurs at position(s): ",
             self.num.index(max(self.num))+1,sep='')
    # Redo the below code (for the next class on Friday) without sorting the array
    def second_highest(self):
        print("The second largest number in the list is: ", ,sep='')

    '''Shorten the code below using Pythin std coding. '''
    def index_maxdiff(self):
        maxDiff, pos = 0, ""
        for i in range(self.num_len - 1):
            if abs(self.num[i] - self.num[i+1]) >= maxDiff:
                maxDiff = abs(self.num[i] - self.num[i+1])
                pos = (str(i+1)+" & "+str(i+2)) if pos=="" else  ", "+(str(i+1)+" & "+str(i+2))
        print("The maximum difference of ", maxDiff," occurs at positions: ", pos, "\n", sep='')

print("To display the position of largest number, the second largest numbers along \
 with index such that difference in i and i+1 elements is maximum:")
n = int(input("Enter number of elements: "))

obj = ListOperations(n)
obj.fill_list()
obj.show_list()
obj.index_highest()
obj.second_highest()
obj.index_maxdiff()
