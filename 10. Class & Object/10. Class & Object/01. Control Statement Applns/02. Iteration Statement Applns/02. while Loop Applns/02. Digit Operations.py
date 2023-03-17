import os
os.system("cls")

class DigitOperations():
    def __init__(self, num, dig):
        self.num = num
        self.dig = dig

    def missingDigits(self):
        miss = ""
        for i in range(10):
            temp = self.num
            while temp>0:
                if i==temp%10:
                    break
                temp//=10
            if temp==0:
                miss+= str(i) if miss=="" else ", "+str(i)
        
        if miss=="":
            print("\nNo missing digits in the number!\n")
        else:
            print("The missing numbers in ", self.num," are: ", miss, "\n")

        
    '''
    For a change work WITHOUT any STRING variable in the below method.
    '''
    def posAndFreqOf(self, d):
        temp, cnt, pos, freq = self.num, 0, "", 0
        lgt = len(str(temp))
        while temp>0:
            if temp%10==d:
                pos= str(lgt-cnt) if pos=="" else str(lgt-cnt)+", "+pos 
                freq+=1
            cnt+=1
            temp//=10
        print("\nPosition(s) of ",d,": ",pos," and its frequency: ",freq, sep='')

    def primeDigits(self):
        temp, prime = self.num, ""
        while temp>0:
            dig=temp%10
            if dig==2 or dig==3 or dig==5 or dig==7:
                prime=str(dig) if prime=="" else str(dig)+", "+prime
            temp//=10
        return prime

    def display(self):
        self.missingDigits()
        self.posAndFreqOf(self.dig)
        print("\nPrime digits in same sequence:\n",self.primeDigits(),"\n", sep='')

print("To display the missing digits in a number and frequency of a given digit in the number:")
num = int(input("Enter a number: "))
dig = int(input("Enter the digit: "))
obj = DigitOperations(num, dig)
obj.display()

#sir the shortening of code is not done yet