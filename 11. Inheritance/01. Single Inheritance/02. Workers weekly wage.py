import os
os.system('cls')

class Worker:
    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num

    def display(self):
        print("Name: ",self.name,
            "\nID number: ", self.id_num, sep='')

class Wages (Worker):
    def __init__(self, name, id_num, hrs, rate):
        super().__init__(name, id_num)
        self.hrs = hrs
        self.rate = rate
        self.calculate()

    def calculate(self):
        if self.hrs<=35:
            self.wages= self.hrs * self.rate
        elif self.hrs<=60: 
            self.wages= self.rate * 35 + 1.5 * self.rate * (self.hrs - 35)
        elif self.hrs <= 70:
            self.wages= self.rate * 35 + 1.5 * self.rate * 25 + 2 * self.rate * (self.hrs - 60)
        else:
            self.wages= self.rate * 35 + 1.5 * self.rate * 25 + 2 * self.rate * 10

    def display(self):
        super().display()
        print("Hours: ", self.hrs, 
            "\nRate: ", self.rate, 
            "\nWages: Rs ", self.wages, sep='')
        if self.hrs > 70:
            print("Worker worked for more than 70 hours! ",
             "Payment given till 70 hours as per company rule.", sep='')

print("To display the details of a daily worker and calculate his/her wages: ")
name = input("Enter the name: ")
id_num = int(input("Enter the ID number: "))
hrs = int(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly rate: Rs "))

wage = Wages(name, id_num, hrs, rate)
print("\nThe details of the worker:")
wage.display()
print()