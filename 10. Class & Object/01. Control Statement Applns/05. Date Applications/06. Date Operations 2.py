import os
os.system("cls")

class RealDate():

    global mDays, mName
    mDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mName = ["", "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    
    def __init__(self, d, m, y):
        self.dd = d
        self.yy = y
        self.mm = m
        mDays[2] = 29 if self.yy%400==0 or self.yy%4==0 and self.yy%100!=0 else 28

    def isValid(self):
        return 1000<=self.yy<=9999 and 1<=self.mm<=12 and 1<=self.dd<=mDays[self.mm]

    def showDate(self):
        print(self.dd//10,self.dd%10,"-",mName[self.mm],"-",(self.yy%100)//10,(self.yy%100)%10, sep='')

    def futureDate(self, days):
        d, m, y = self.dd, self.mm, self.yy
        for i in range(days):
            d+=1
            mDays[2] = 29 if y%400==0 or y%4==0 and y%100!=0 else 28
            if d > mDays[m]:
                d= 1
                m+= 1
                if m > 12:
                    m= 1
                    y+= 1
        return RealDate(d, m, y)

    def pastDate(self, days):
        d, m, y = self.dd, self.mm, self.yy
        for i in range(days):
            d-=1
            mDays[2] = 29 if y%400==0 or y%4==0 and y%100!=0 else 28
            if d < 1:
                m-= 1
                if m < 1:
                    m= 12
                    y-= 1
                d= mDays[m]
        return RealDate(d, m, y)
        
print("To display the future and past date from a given date:")
dd = int(input("Enter the date: "))
mm = int(input("Enter the month: "))
yy = int(input("Enter the year: "))
days = int(input("Enter the number of days for the future and past dates: "))

date = RealDate(dd, mm, yy)
print("\nDate after ",days," days from given date: ",end='', sep='')
date.futureDate(days).showDate()
print("\nDate before ",days," days from given date: ",end='', sep='')
date.pastDate(days).showDate()
print()