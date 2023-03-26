import os
os.system('cls')

class MultiSet():
    def __init__(self, n):
        self.multi_set = []
        self.n = n

    def fill_list(self):
        for i in range(self.n):
            print("Enter number for element #", i+1, ": ", sep='', end='')
            self.multi_set.append(int(input()))

    def show_list(self):
        print(self.multi_set)

    def is_present(self, n):
        return n in self.multi_set

    ''' Change the code as per changes made in the two below methods.  '''
    
    def intersection(self, a):
        obj = MultiSet(self.n+a.n)
        obj.multi_set = self.multi_set+a.multi_set
        for ele in obj.multi_set:
            if self.is_present(ele) and a.is_present(ele) and ele not in inter:
                inter.append(ele)
        return inter

    def union(self, a, b):
        self.multi_set = a.multi_set+b.multi_set
        for num in (self.multi_set):
            if num not in union:
                union.append(num)
        return union

print("To display intersection and union of the lists: ")
n1 = int(input("Enter number of elements in list 1: "))
n2 = int(input("Enter number of elements in list 2: "))

obj1, obj2 = MultiSet(n1), MultiSet(n2)
print("\nEnter elements for list 1: ")
obj1.fill_list()
print("\nEnter elements for list 2: ")
obj2.fill_list()

print("\nThe first list: ")
obj1.show_list()
print("\nThe second list: ")
obj2.show_list()

print("\nIntersection of the two lists: ")
print(obj1.intersection(obj2))
print("\nUnion of the two lists: ")
print(obj1.union(obj1, obj2))
print()