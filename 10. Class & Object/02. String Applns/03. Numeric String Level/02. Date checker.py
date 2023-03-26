import os
os.system("cls")

class DateChecker():
    global mDays, wDay, mName

    mDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    wDay = ["", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    mName = ["", "January", "February", "March", "April", "May", "June", "July", "August",
         "September", "October", "November", "December"]
    
    def __init__(self, date):
        self.date = date
        delims, isAlpha = "", False
        for ch in date:
            if ch.isalpha():
                isAlpha = True
            if not ch.isdigit():
                delims+=ch
        if isAlpha:
            print("\nInvalid character(s) present in the date string!\n")
            exit()
        elif len(delims)!=2 or delims[0]!=delims[1]:
            print("\nMisbalanced delimiters found in the date string!\n")
            exit() 
        else:
            dt = date.split(delims[0])
            self.dd, self.mm, self.yy = int(dt[0]), int(dt[1]), int(dt[2])
            self.yy+= 2000 if self.yy>=0 and self.yy<=29 else 1900 if self.yy>=30 and self.yy<=99 else 0

    def isValid(self):
        mDays[2] = 29 if self.yy%400==0 or self.yy%4==0 and self.yy%100!=0 else 28
        return 1000<=self.yy<=9999 and 1<=self.mm<=12 and 1<=self.dd<=mDays[self.mm]

    def getDay(self):
        days = self.dd
        for i in range(1900, self.yy):
            days+=366 if i%400==0 or i%4==0 and i%100!=0 else 365
        for i in range(1, self.mm):
            days+= mDays[i]
        return wDay[days%7+1]

    def display(self):
        d = self.dd%10
        sufx = "st" if d==1 and self.dd!=11 else "nd" if d==2 and self.dd!=12 else "rd"\
            if d==3 and self.dd!=13 else "th"
        print("\n", self.getDay(),", ",mName[self.mm]," ",self.dd,sufx,", ",self.yy, "\n", sep='')

print("To check if the given date is in valid format and display the day and date in long format:")
date = input("Enter the date: ")

obj = DateChecker(date)
if obj.isValid():
    obj.display()
else:
    print("\nInvalid date is given!\n", sep='')
'''
To check if the given date is in valid format and display the day and date in long format:
Enter the date: 23/4/2209/

Invalid character(s) present in the date string!
(Correct Output: Misbalanced delimiters found in the date string!)

Keep this FIXED.
Keep the code TESTED WELL.
Will check in the next class.
'''