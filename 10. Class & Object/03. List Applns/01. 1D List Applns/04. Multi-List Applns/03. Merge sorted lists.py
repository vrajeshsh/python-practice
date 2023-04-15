import os
os.system('cls')

class OrderedList():
    def __init__(self, n):
        self.ordered_list = []
        self.size = n

    def make_list(self):
        for i in range(self.size):
            print("Enter number of element #", i+1, ": ", sep='', end='')
            self.ordered_list.append(int(input()))

    def show_list(self):
        print(self.ordered_list)

    def find_order(self):
        asc, desc = 0, 0
        for i in range(self.size - 1):
            if self.ordered_list[i] <= self.ordered_list[i+1]:
                asc+=1
            if self.ordered_list[i] >= self.ordered_list[i+1]:
                desc+=1
        return 1 if asc==self.size-1 else 2 if desc==self.size-1 else 0

    def merge_ordered(self, ord_list):
        result= OrderedList(self.size + ord_list.size)
        i, j = 0, len(ord_list.ordered_list) - 1 
        while i < len(self.ordered_list) and j >= 0:
            if self.ordered_list[i] < ord_list.ordered_list[j]:
                result.ordered_list.append(self.ordered_list[i])
                i+= 1
            else:
                result.ordered_list.append(ord_list.ordered_list[j])
                j-= 1
        result.ordered_list.extend(self.ordered_list[i:])
        result.ordered_list.extend(reversed(ord_list.ordered_list[:j + 1]))
        return result

print("To merge two lists and display in ascending order:")
n1 = int(input("Enter number of elements in list 1: "))
n2 = int(input("Enter number of elements in list 2: "))

obj1, obj2 = OrderedList(n1), OrderedList(n2)
print("\nEnter elements for list 1: ")
obj1.make_list()
print("\nEnter elements for list 2: ")
obj2.make_list()

print("\nThe first list: ")
obj1.show_list()
print("\nThe second list: ")
obj2.show_list()

if obj1.find_order()!=1:
    print("\nElements of first list NOT in Ascending order!\n", sep='')
    exit()
elif obj2.find_order()!=2:
    print("\nElements of second list NOT in Descending order!\n", sep='')
    exit()
else:
    print("\nMerged list in Ascending order: ")
    obj1.merge_ordered(obj2).show_list()
    print()

    # Kindly EXPLAIN, how is this logic working despite the second list being in descending order?
    # Inverting the second list

    # Okay. Understood.... But change this as THAT WOULD BE ACCESSING IT the second time...  
    # against the problem specs...