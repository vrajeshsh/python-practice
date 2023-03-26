import os
os.system("cls")

class Searcher():
    def __init__(self, n):
        self.numlist = []
        self.numlen = n

    def fill_list(self):
        for i in range(self.numlen):
            print("Enter number for element #", i+1, ": ", sep='', end='')
            self.numlist.append(int(input()))

    def show_list(self):
        print("\nThe given list: ", self.numlist, "\n", sep='')
    ''' Try the below code WITHOUT SORTING. As it is it was never meant to be sorted any way! '''
    def sortOrder(self):
        return 1 if self.numlist==sorted(self.numlist) else \
            2 if self.numlist==sorted(self.numlist, reverse = True) else 0

    def linear_search(self, x):
        for i in range(self.numlen):
            if self.numlist[i]==x:
                return i
        return -1

    def binary_search(self, x):
        low, high = 0, self.numlen -1 
        while low <= high:
            mid = (low+high)//2
            if self.numlist[mid]==x:
                return mid
            elif self.numlist[mid]<x if self.sortOrder()==1 else self.numlist[mid]>x:
                low = mid+1
            else:
                high = mid -1
        return -1
    ''' The below function code is COMPLETE MESSED UP!!
    1. First check order.
    2. If 1 or 2 then call Binary else Linear just to get the index of match. Also handling the messaging dept
       here itself.
    3. Now check if the matching index==-1 then do the needful else do the needful.

    Now fix that part please. 
    '''
    def search_result(self, x):
        order = self.sortOrder()
        if order==0:
            lin = self.linear_search(x)
            print("\nThe given list is unsorted! Hence Linear Search is used!\nThe element ",x," occurs at position ", lin,".\n", sep='')
        else:
            bin = self.binary_search(x)
            print("\nThe given list is sorted in ", "Ascending" if order==1 else "Descending", " order!\nThe element ", x," occurs at position ", bin,".\n", sep='')
        if lin==-1 and bin==-1:
            print("Search element NOT present in the list!\n")
            exit()

print("To perform Binary search if the given list is sorted, else Linear search:")
n = int(input("Enter number of elements: "))
x = int(input("Enter the element to search for: "))
print()
obj = Searcher(n)
obj.fill_list()
obj.show_list()
obj.search_result(x)


