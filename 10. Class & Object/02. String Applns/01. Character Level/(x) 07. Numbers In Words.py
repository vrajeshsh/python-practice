import os, math
os.system("cls")

class AmountInWords():

    global word

    word = ["","One", "Two","Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty", "Thirty", 
        "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"] 

    def __init__(self, amt):
        self.amount= amt
        self.str= ""

        #this is not done sir Fine will check this next class...
        
    def numToWords(self, num):  # converts the integer 'num' to words
        if num<=20:
            return word[num]
        return word[num//10+18]+" "+word[num%10]

    def convert(self):  # converts the amount to words by calling other methods
        print("\n", self.amount, " in words: ", sep='', end='')
        if 1<=self.amount<=10000:
            if self.amount<100:
                print(self.numToWords(self.amount),"\n", sep='')
            elif self.amount<1000:
                print(self.numToWords(self.amount//100), " Hundred and ",
                (self.numToWords((self.amount//10)%10+18)+self.numToWords(self.amount%10) \
                if self.amount%100>=20 else self.numToWords(self.amount%100)),"\n", sep='')
            else:
                print(self.numToWords(self.amount//1000)," Thousand ",
                (self.numToWords((self.amount//100)%10)+ " Hundred " if (self.amount//100)%10>0 else ""),
                "and ", (self.numToWords((self.amount//10)%10+18)+self.numToWords(self.amount%10) 
                if self.amount%100>=20 else self.numToWords(self.amount%100)),"\n", sep='')
        else:
            print("\nOut of range!\n")

print("To display numbers (<10000) in words:")
amt = int(input("Enter the amount: "))

obj = AmountInWords(amt)
obj.convert()