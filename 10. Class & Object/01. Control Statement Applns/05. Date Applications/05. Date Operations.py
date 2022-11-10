import os
os.system("cls")

class ModelDate():

    global mDays, mName
    mDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mName = ["", "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP",
    "OCT", "NOV", "DEC"]

    ''' Never add/remove any class member -- that is DISALLOWED!!'''
    def __init__(self, d, m, y): 
        self.dd = d
        self.mm = m
        self.yy = y
        mDays[2] = 29 if self.yy%400==0 or self.yy%4==0 and self.yy%100!=0 else 28

    def isValid(self):
        return 1000<=self.yy<=9999 and 1<=self.mm<=12 and 1<=self.dd<=mDays[self.mm]

    def display(self):
        print(self.dd//10,self.dd%10,"-",mName[self.mm],"-",(self.yy%100)//10,(self.yy%100)%10, sep='')

    def dateToDateNumber(self):
        days = self.dd
        for i in range(1, self.mm):
            days+= mDays[i]
        return days

    def dateNumberToDate(self, num):
        self.dd, self.mm = num, 1
        while self.dd >= mDays[self.mm]:
            self.dd-= mDays[self.mm]
            self.mm+=1
            if self.mm>12:
                self.mm = 1
                self.yy+=1
    
    def futureDate(self, days):
        futureDate= ModelDate(0, 0, self.yy)
        futureDate.dateNumberToDate(days+ self.dateToDateNumber())
        return futureDate

    def dateDifference(self, dt):
        return abs(self.dateToDateNumber() - dt.dateToDateNumber())

print("To perform standard Date Operations with two dates belonging to the same year:",
    "\nEnter details for the first date:")
d1 = int(input("Enter the day: "))
m1 = int(input("Enter the month: "))
y1 = int(input("Enter the year: "))
print("Enter details for the second date:")
d2 = int(input("Enter the day: "))
m2 = int(input("Enter the month: "))
y2 = int(input("Enter the year: "))
if y1 != y2:
    print("\nThe two dates must be in the same year as per program requirement!\n")
    exit()
days = int(input("Enter the number of days to be added for the future date: "))

date1, date2 = ModelDate(d1, m1, y1), ModelDate(d2, m2, y2)

if date1.isValid() and date2.isValid():
    print("\nThe first date: ", sep='', end='')
    date1.display()
    print("The second date: ", sep='', end='')
    date2.display()
    print("Date after ",days," days from date1: ",sep='', end='')
    date1.futureDate(days).display()
    print("Date after ",days," days from date2: ",sep='', end='')
    date2.futureDate(days).display()
    print("Date difference: ",date1.dateDifference(date2),"\n", sep='')
else:
    print("INVALID DATE(S)!")