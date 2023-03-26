import os
os.system('cls')

class Collection():
    def __init__(self, n):
        self.num_list = []
        self.n = n

    def store_list(self):
        for i in range(self.n):
            print("Enter number of element #", i+1, ": ", sep='', end='')
            self.num_list.append(int(input()))
    '''There are TWO PROBLEMS with the code below:
    1. You had to return an object, but you ended up in returning a list (despite the program
       desc. saying so)
    2. You had to store ALL THE COPIES of the common elements in the list inside the object.
       E.g. Say 2 occurs 3 times in Collection A (current object) and also occurs 5 times in 
       Collection B (parameter object), then in the new object list, 8 copies of 2 should be
       there all coming 'toli banake' one after the other.
    '''   
    def common_list(self, col):
        obj, common = Collection(self.n+col.n), []
        obj.num_list = self.num_list+col.num_list
        for ele in obj.num_list:
            if obj.find_frequency(ele)>1 and ele not in common:
                common.append(ele)
        return common

    def arrange_list(self):
        return sorted(self.num_list)

    def find_frequency(self, num):
        return self.num_list.count(num)

    def show_list(self):
        print(self.num_list)

print("To display common elements in the lists:")
n1 = int(input("Enter number of elements in list 1: "))
n2 = int(input("Enter number of elements in list 2: "))

obj1, obj2 = Collection(n1), Collection(n2)
print("\nEnter elements for list 1: ")
obj1.store_list()
print("\nEnter elements for list 2: ")
obj2.store_list()

print("\nThe first list: ")
obj1.show_list()
print("\nThe second list: ")
obj2.show_list()

print("\nCommon elements of the two lists: ")
print(obj1.common_list(obj2))
print()