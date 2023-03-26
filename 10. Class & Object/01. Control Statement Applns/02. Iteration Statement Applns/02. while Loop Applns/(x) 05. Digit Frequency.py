import os, math
os.system("cls")

class DigitFrequency():
    def __init__(self, num):
        self.num = num

    def frequency(self, dig):
        temp, count = self.num, 0
        while temp>0:
            if temp%10==dig:
                count+=1
            temp//=10
        return count
    
    def frequencyInOrder(self):
        print("\nThe ordered frequency distribution table for the digits of ", self.num,": ", sep='')
        print("\nDIGIT\t\tFREQUENCY")
        for i in range(10):
            count = self.frequency(i)
            if count>0:
                print(i, "\t\t", count,sep='')
    
    # Remove all usages of string functions and work FRUGALLY using OOPS principles for the below method
    def frequencyInSequence(self):
        print("\nThe in-sequence frequency distribution table for the digits of ", self.num,": ", sep='')
        print("\nDIGIT\t\tFREQUENCY")
        temp, newNum = self.num, 0
        digCnt = int(math.log10(self.num)+1)
        while digCnt>0:
            digCnt-=1
            dig = temp//(10**digCnt)
            newNum = newNum*10+dig
            n, cnt = newNum, 0
            ''' Remove the below loop and apply OOPS concepts instead (i.e. call the frequency() method)'''
            # You might have to SHUN the very algorithm used below
            while n>0:
                if n%10==dig:
                    cnt+=1
                n//=10
            if cnt==1:
                print(dig,"\t\t", self.frequency(dig))
            temp%=(10**digCnt)

    def frequencyFreqwise(self):
        maxFreq = int(math.log10(self.num)+1)
        print("\nThe frequency-wise frequency distribution table for the digits of ", self.num,": ", sep='')
        print("\nDIGIT\t\tFREQUENCY")
        while maxFreq>0:
            for i in range(10):
                if self.frequency(i)==maxFreq:
                    print(i, "\t\t", self.frequency(i))
            maxFreq-=1

print("To display the frequency on each digit in a number: ")
num = int(input("Enter a number: "))

obj = DigitFrequency(num)
obj.frequencyInOrder()
obj.frequencyInSequence()
obj.frequencyFreqwise()

# You have MILES TO GO before you become proficient in OOPS, Vrajesh!!