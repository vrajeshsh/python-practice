import os
os.system("cls")

class Salesperson():
    def __init__(self, name, gender, sales):
        self.name = name
        self.gender = gender
        self.sales = sales

    # You are NOT AUTHORIZED to add/subtract ANYTHING from OOP style classes!! Remember this PLEASE.  

    def calculate(self):
        if self.sales <= 100000:
            comm = 0
        elif self.sales <= 150000:
            comm = .1 * self.sales if self.gender.lower()=="m" else .12 * self.sales
        elif self.sales <= 200000:
            comm = .14 * self.sales if self.gender.lower()=="m" else .16 * self.sales
        else:
            comm = .18 * self.sales if self.gender.lower()=="m" else .2 * self.sales
        return comm
         
    def display(self):
        total = .1 * self.sales if self.sales <= 100000 else self.calculate() + 5000
        print("\nName: ",self.name,"\nCommission: Rs ",self.calculate(),
        "\nTotal Salary: Rs ", round(total, 2),"\n",sep='')

print("To calculate the commission of a salesperson:")
name = input("Enter the name: ")
gender = input("Enter the gender [M/F]: ")
sales = float(input("Enter the sale amount: Rs "))

obj = Salesperson(name, gender, sales)
obj.display()