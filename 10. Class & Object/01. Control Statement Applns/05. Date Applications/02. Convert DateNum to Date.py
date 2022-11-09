import os
os.system("cls")

class DateNumToDate():

    global mDays, mName
    mDays= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mName= ["", "January", "February", "March","April", "May", "June", "July", "August",
        "September", "October", "November", "December"]

    def __init__(self):
        self.n = self.d = self.m = self.y = 0

    def accept(self):
        self.n = int(input("Enter the day number: "))
        self.y = int(input("Enter the year: "))

    def day_to_date(self):
        if self.y%400 ==0 or self.y%4==0 and self.y%100!=0:
            mDays[2] = 29
        self.d= self.n
        self.m= 1
        while self.d > mDays[self.m]:
            self.d-= mDays[self.m]
            self.m+=1
            if self.m > 12:
                self.m= 1
                self.y+= 1

    def display(self):
        print("\n",mName[self.m]," ",self.d,", ",self.y,"\n", sep='')

print("To display the date corresponding to the day number given by user: ")
obj = DateNumToDate()
obj.accept()
obj.day_to_date()
obj.display()