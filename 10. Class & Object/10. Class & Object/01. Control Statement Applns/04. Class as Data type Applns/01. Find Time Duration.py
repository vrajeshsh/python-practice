import os
os.system("cls")

''' WELCOME to yet ANOTHER unknown and unexplored topic of Python's Control Statement!!'''

class Time:
    def __init__(self, hh, mm):
        self.hh = hh
        self.mm = mm

    def showTime(self):
        print(self.hh,":",self.mm, sep='')

    def timeToMinutes(self):
        return self.hh*60+self.mm

    def minutesToTime(self, mins):
        self.hh= mins//60
        self.mm= mins%60
        
    def subFrom(self, time):
        diffTime= Time(0, 0)
        startMins, endMins = self.timeToMinutes(), time.timeToMinutes()
        if endMins < startMins:  # it means Overnight timing is involved
            endMins+= 24*60
        diffMins= endMins - startMins
        diffTime.minutesToTime(diffMins)
        return diffTime

print("To calculate the time for which a user is logged in:",
    "\nEnter details for the start time: ")
h1 = int(input("Enter hours: "))
m1 = int(input("Enter minutes: "))

print("Enter details for the end time: ")
h2 = int(input("Enter hours: "))
m2 = int(input("Enter minutes: "))

startTime = Time(h1, m1)
endTime = Time(h2, m2)
timeDiff = startTime.subFrom(endTime)

print("\nLog-in time:")
startTime.showTime()
print("Log-out time:")
endTime.showTime()
print("Duration: ")
timeDiff.showTime()