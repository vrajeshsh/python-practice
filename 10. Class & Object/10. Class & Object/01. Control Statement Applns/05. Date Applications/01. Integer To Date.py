import os
os.system("cls")

''' WELCOME to yet another World of Dates!!'''

class IntegerToDate():
    # Global class variables declared for later use
    global mDays, wDay, mName
    mDays= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    wDay= ["", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    mName= ["", "January", "February", "March","April", "May", "June", "July", "August",
        "September", "October", "November", "December"]

    def __init__(self, n):
        self.num = n
        self.dd = self.num//10000
        self.mm = (self.num//100) % 100
        self.yy = self.num%100
        self.yy+= 2000 if self.yy>=0 and self.yy<=29 else 1900 if self.yy>= 30 and self.yy<=99 else 0

    def isValid(self):
        mDays[2]= 29 if self.yy%400==0 or self.yy%4==0 and self.yy%100 != 0 else 28
        return True if self.yy>= 1000 and self.yy<=9999 and self.mm>=1 and self.mm<=12 and \
            self.dd>=1 and self.dd<=mDays[self.mm] else False

    def getDay(self):
        days = self.dd
        for i in range(1900,self.yy):
            days+= 366 if i%400==0 or i%4==0 and i%100!=0 else 365
        for i in range(1, self.mm):
            days+= mDays[i]
        return wDay[days%7+1]   # adding the 'shift value' here [Note 01-01-1900 was a Monday nt Sunday]
    
    def showDateLong(self):
        d = self.dd%10
        sufx = "ST" if d==1 and self.dd!=11 else "ND" if d==2 and self.dd!=12 else "RD" if d==3 and\
            self.dd!=13 else "TH"
        print("\n",self.getDay().upper(),", ",self.dd,sufx," ",mName[self.mm].upper(),", ",self.yy,"\n",sep="")

print("To display a given 6-digit integer as date and the day of the week: ")
num = int(input("Enter a 6-digit integer: "))

obj = IntegerToDate(num)
if obj.isValid():
    obj.showDateLong()
else:
    print("\nINVALID DATE!\n")