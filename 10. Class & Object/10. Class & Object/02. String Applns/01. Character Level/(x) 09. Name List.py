import os
os.system("cls")

class NameList():
    # not 
    def fillNames(self):
        self.name=[]
        n = int(input("Enter number of persons: "))
        for i in range(1, n+1):
            print("Enter name #", i,": ", sep='', end='')
            self.name.append(input())

    def showNames(self):
        for name in self.name:
            print(name)

    def sortNames(self):
        self.name.sort() 

    def removeDups(self):
        res=[]  #'''  No new list will be allowed for reasons already stated above!!'''
        for i in self.name:
            if i not in res:
                res.append(i)
        return res

    def mergeWhileSort(self, listM, listF):
        listA = listM.

print("To merge the list of names of males and females, alphabetically: ")

listM, listF = NameList(), NameList()

obj = NameList()
obj.fillNames()
obj.showNames()
obj.mergeWhileSort(listM, listF)

