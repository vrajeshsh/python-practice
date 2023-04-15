import os
os.system('cls')

class DataSplitter():
    def __init__(self, n):
        self.num_list = []
        self.n = n

    def fill_list(self):
        i = 0
        while i<self.n:
            print("\nFor element #", i+1,": ", sep='')
            type = input("Enter type ['P' => Positive, 'N'=> Negative]: ")
            if type.lower()=="n" or type.lower()=='p':
                num = int(input("Enter integer: "))
                if type.lower()=='n' and num<0 or type.lower()=='p' and num>0:
                    self.num_list.append(type)
                    self.num_list.append(num)
                    i+=1 
                else:
                    print("\nType and integer mismatch! Please re-enter inputs correctly!")
            else:
                print("\nInvalid integer type! Enter P for Positive and N for Negative integers.")
    
    def show_list(self):
        print("NUMBER\t\tTYPE", sep='')
        for num in self.num_list:
            if str(num).upper() not in "PN": 
                print(num, "\t\t", "Negative" if float(num) < 0 else "Positive", sep='')

    def arrange_list(self):
        self.num_list.sort()

    def split_list(self):
        pos, neg = DataSplitter(self.n), DataSplitter(self.n)
        for i in range(0, self.n*2 -1, 2):
            if self.num_list[i].lower() =='p':
                pos.num_list.append(self.num_list[i+1])
            elif self.num_list[i].lower() =='n':
                neg.num_list.append(self.num_list[i+1])
        pos.arrange_list()
        neg.arrange_list()        
        return pos, neg

print("To display positive and negative integers of a list in separate arrays:")
n = int(input("Enter number of elements: "))

obj = DataSplitter(n)
obj.fill_list()

pos, neg = obj.split_list()

print("\nThe given list of numbers:")
obj.show_list()
print("\nThe list of negative numbers:")
neg.show_list()
print("\nThe list of positive numbers:")
pos.show_list()
print()