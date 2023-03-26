import os
os.system("cls")

class DateSpan():

    global mDays, mName, isLeap
    mDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mName = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    def __init__(self, d, m, y):
        self.dd = d
        self.yy = y
        self.mm = m
        mDays[2] = 29 if self.yy%400==0 or self.yy%4==0 and self.yy%100!=0 else 28

    def isValid(self):
        return 1<=self.dd<=mDays[self.mm] and 1<=self.mm<=12 and 1000<=self.yy<=9999

    def showDate(self):
        print(self.dd//10,self.dd%10,"-",mName[self.mm],"-",(self.yy%100)//10,(self.yy%100)%10, sep='')
   
    def laterDate(self, dt):
        if dt.yy>self.yy or dt.yy==self.yy and dt.mm>self.mm or dt.yy==self.yy and \
            dt.mm==self.mm and dt.dd>self.dd:
            return DateSpan(dt.dd, dt.mm, dt.yy)
        else:
            return DateSpan(self.dd, self.mm, self.yy)

    ''' Four loops in 2022, and that too for US IT based companies? Please use just ONE LOOP for the below method.'''
    def diffDate(self, dt):
        days1, days2 = self.yy*365+self.dd, dt.yy*365+dt.dd
        for i in range(1, self.mm):
            days1+=mDays[i]
        for i in range(1, dt.mm):
            days2+=mDays[i]
        return abs(days1-days2)
        
#Keep this COMPLETED for tomorrow... if yiu fail, then tomorrow I WILL TYPE OUT MYSELF only

    def timespan(self, dt):
        daysDiff = self.diffDate(dt)
        year = daysDiff//365
        month = (daysDiff%365)//30
        days = (daysDiff%365)%30
        print(year," year(s), ",month," month(s) and ",days, " day(s).\n", sep='')

print("To display the time span between two dates:\n"
    "Enter details for first date: ",sep='')
d1 = int(input("Enter the date: "))
m1 = int(input("Enter the month: "))
y1 = int(input("Enter the year: "))
print("Enter details for the second date: ")
d2 = int(input("Enter the date: "))
m2 = int(input("Enter the month: "))
y2 = int(input("Enter the year: "))

date1, date2 = DateSpan(d1, m1, y1), DateSpan(d2, m2, y2)
print("\nFirst date: ", sep='', end='')
date1.showDate()
print("Second date: ", sep='', end='')
date2.showDate()
print("Time span between the two dates: ", sep='')
date1.timespan(date2)
print()
        