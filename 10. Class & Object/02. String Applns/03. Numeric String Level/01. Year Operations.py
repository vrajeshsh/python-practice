import os, re
os.system('cls')

class StringYear():
    def __init__(self, s):
        self.sent = s
        global words
        words = re.split("[,;: .?!]", self.sent)

    def replaceYear(self, repYr):
        newStr = ""
        for word in words:
            if word.isdigit() and len(word)==4 and 1800<=int(word)<=2030:
                word = str(repYr)
            newStr+=word if newStr=="" else " "+word
        return newStr.strip() if self.sent[-1].isalpha() else newStr.strip()+self.sent[-1]

    def updateYear(self, yrs):
        newStr = ""
        for word in words:
            if word.isdigit() and len(word)==4 and 1800<=int(word)<=2030:
                word = str(int(word)+yrs).strip()
            newStr+=word if newStr=="" else " "+word
        return newStr.strip() if self.sent[-1].isalpha() else newStr.strip()+self.sent[-1]

    def makeYearLeap(self):
        newStr =""
        for word in words:
            if word.isdigit() and len(word)==4:
                yr = int(word)
                if not (yr%400==0 or yr%4==0 and yr%100!=0):
                    if yr%4==1 or ((96<yr%100<=99) and (yr//100)%4!=3):
                        yr-=yr%4
                    else:
                        yr+=4-yr%4
                word = str(yr)
            newStr+= word if newStr=="" else " "+word
        return newStr.strip() if self.sent[-1].isalpha() else newStr.strip()+self.sent[-1]

print("To replace year, add years and find the closest leap year to the given year in sentence:")
sent = input("Enter the sentence:\n")
repYr = int(input("\nEnter the year to replace by: "))
yrs = int(input("Enter the years to add: "))

obj = StringYear(sent)

print("\nAfter replacing the years by ",repYr,":\n", obj.replaceYear(repYr),
        "\n\nAfter updating the years by ",yrs," years:\n", obj.updateYear(yrs),
            "\n\nAfter replacing the years by the closest leap year:\n", obj.makeYearLeap(),"\n", sep='')