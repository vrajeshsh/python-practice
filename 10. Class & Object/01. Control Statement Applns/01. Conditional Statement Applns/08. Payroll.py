import os
os.system("cls")

class Payroll():
    def __init__(self, empNum, name, basic):
        self.empNum = empNum
        self.name = name
        self.basic = basic
        self.allows = self.deducts = self.netPay = 0

    def calcNetSalary(self):
        global gross
        if self.basic<10000 or self.basic > 20000 :
            self.allows = .75 * self.basic
        else:
            self.allows = .72 * self.basic
        gross = self.basic+self.allows
        self.deducts= (.07*gross if gross<10000 else .08*gross) + self.calcTax(gross*12)/12
        return gross - self.deducts

    def calcTax(self, gross):
        if gross <= 100000:
            it = 0
        elif gross <= 500000:
            it = 1000 + .1 * (gross - 100000)
        elif gross <= 800000:
            it = 5000 + .2 * (gross - 500000)
        else:
            it = 10000 + .3 * (gross - 800000)
        return it

    def display(self):
        net= self.calcNetSalary()
        print("\nName: ",self.name,
            "\nEmployee number: ",self.empNum,
            "\nBasic Salary: Rs ",self.basic, 
            "\nAllowances: Rs ",round(self.allows, 2),
            "\nDeductions: Rs ",round(self.deducts, 2),
            "\nGross Pay: Rs ",round(gross, 2),
            "\nNet Pay: Rs ",round(net, 2),"\n",sep='')

print("To calculate the net salary of an employee: ")
empNum = input("Enter the employee number: ")
name = input("Enter the name: ")
basSal = float(input("Enter the basic salary: "))
obj = Payroll(empNum, name, basSal)
obj.display()
