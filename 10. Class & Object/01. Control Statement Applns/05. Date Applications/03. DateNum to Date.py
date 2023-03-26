import os
os.system("cls")

class DayNumToDate():

    global mDays, mName
    mDays= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mName= ["", "JAN", "FEB", "MAR","APR", "MAY", "JUN", "JUL", "AUG",
        "SEP", "OCT", "NOV", "DEC"]

    def __init__(self, n, yr):
        self.yy, self.dd, self.mm = yr, n, 1
        if self.yy%400==0 or self.yy%4==0 and self.yy%100!=0:
            mDays[2] = 29
        while self.dd>mDays[self.mm]:
            self.dd-= mDays[self.mm]
            self.mm+=1
            if self.mm>12:
                self.mm = 1
                self.yy+=1

    def displayDate(self):
        print(self.dd//10,self.dd%10,"-",mName[self.mm],"-",(self.yy%100)//10,(self.yy%100)%10, sep='')

print("To display the date corresponding to the number and also the date after:")
dayNum = int(input("Enter a day number: "))
yr = int(input("Enter the year: "))
n = int(input("Enter the number of days after: "))

obj1, obj2 = DayNumToDate(dayNum, yr), DayNumToDate(dayNum+n, yr)

print("\nDATE FORMED: ", sep='', end='')
obj1.displayDate()
print("DATE AFTER ",n," DAYS: ", sep='', end='')
obj2.displayDate()
print()