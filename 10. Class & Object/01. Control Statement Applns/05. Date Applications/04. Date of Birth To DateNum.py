import os
os.system("cls")

class DateToDayNum():

    global mDays
    mDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def input(self):
        self.dd = int(input("Enter the date: "))
        self.mm = int(input("Enter the month: "))
        self.yy = int(input("Enter the year: "))

    def isValid(self):
        return 1000<=self.yy<=9999 and 1<=self.mm<=12 and 1<=self.dd<=mDays[self.mm]

    def dateToDateNum(self):
        mDays[2] = 29 if self.yy%400==0 or self.yy%4==0 and self.yy%100!=0 else 28
        days = self.dd
        for i in range(1, self.mm):
            days+= mDays[i]
        return days
    
    def showOutput(self):
        dayNum = self.dateToDateNum()
        if self.isValid():
            print("\nVALID DATE\nDAY NUMBER: ",dayNum,"\n", sep='')
        else:
            print("\nINVALID DATE\n")

print("To display the day number corresponding to the users date of birth:")
obj = DateToDayNum()
obj.input()
obj.showOutput()