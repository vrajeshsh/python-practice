import os
os.system("cls")

class TimeInWords():
    global numWord

    numWord = ["","One", "Two","Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
        "Eighteen", "Nineteen", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty",
         "Ninty"] 

    def __init__(self, timeStr):
        self.timeStr= timeStr
        # Extraction done below
        time = self.timeStr.split(":")
        self.hr = int(time[0].strip())
        self.min = int(time[1].strip())
    ''' The below method code is COMPLETELY BIASED towards the time display. Make it generalized 
    such that some one needs to convert 93 marks to Ninety Three can also use this.
    And in CS Life also ALWAYS DO THAT!!
    Coincidentally, God also did that!! And that is why organ transplants can happen!!!'''

    def numToWords(self, num):  # Converts the integer 'num' in words e.g. 27 will be returned as TWENTY THREE
        if num<=20:
            return numWord[num]
        return numWord[num//10+18]+" "+numWord[num%10]

    def display(self): # to use numToWords() method to convert the given time to words
        time = self.numToWords(self.hr)
        if 1<=self.hr<=12 and 0<=self.min<=59:
            print("\n",self.hr//10,self.hr%10,":", self.min//10, self.min%10," - ", sep='', end='')
            if self.min==0:
                print(time," o' clock\n")
            elif self.min==15:
                print("Quarter past ",time, "\n")
            elif self.min==30:
                print("Half past ",time, "\n")
            elif self.min==45:
                print("Quarter to ",self.numToWords((self.hr%12)+1),"\n")
            elif self.min<30:
                print(self.numToWords(self.min)," minutes past ",time,"\n")
            else:
                print(self.numToWords(60-self.min)," minutes to ",self.numToWords((self.hr%12)+1),"\n")
        else:
            print("\nIncorrect input!")

print("To display time (given in numbers) in words:")
timeStr = input("Enter the time: ")

obj = TimeInWords(timeStr)
obj.display()