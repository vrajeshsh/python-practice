import os
os.system("cls")

class Calendar():
    
    global mDays, mName
    mDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mName = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", 
        "October", "November", "December"]
        
    def __init__(self, mon, y):
        self.month = mon
        self.year = y
        mDays[2]=29 if self.year%400==0 or self.year%4==0 and self.year%100!=0 else 28

    def isValid(self):
        return self.month !="" and self.month.title() in mName and 1900<=self.year<=2120

    def firstDayNum(self):
        dayNum = 1
        for i in range(1900, self.year):
            dayNum+=366 if i%400==0 or i%4==0 and i%100!=0 else 365
        for i in range(1, mName.index(self.month)):
            dayNum+= mDays[i]
        return dayNum%7

    def showCalendar(self):
        dayNum = self.firstDayNum()
        print("\n\t\t",self.month.upper(),", ",self.year,
            "\n\nSUN\tMON\tTUE\tWED\tTHU\tFRI\tSAT",sep='')
        print("\t"*dayNum,sep="", end='')
        for i in range(1, mDays[mName.index(self.month)]+1):
            print(i, sep='', end='')
            print("\n" if dayNum==6 else "\t", sep='', end='')
            dayNum+=1
            dayNum%=7

print("To display the calendar of the month and year given by the user:")
mon = input("Enter the month: ")
y = int(input("Enter the year: "))

obj = Calendar(mon, y)
if obj.isValid(): 
    obj.showCalendar()
else: 
    print("\nINVALID MONTH OR YEAR ENTERED!")
print()

    #how to place the 1st date sir?
            # 1. Get the day index.
            # 2. Give tabs ("\t") sufficient first to take the cursor AWAY to the correct place.
            # 3. Then start printing the days... after every 7 place a new line.
            # Rest you should handle.