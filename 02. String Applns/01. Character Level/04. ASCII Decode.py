import os
os.system("cls")

class ASCIIDecoder():
    def __init__(self, encStr):
        self.asciiStr = encStr
        self.strLen = len(encStr)

    def getDecoded(self):
        ltr, msg = "", ""
        for i in range(self.strLen - 1, -1, -1):
            ltr+= self.asciiStr[i]
            if int(ltr)==32 or 65<=int(ltr)<=90 or 97<=int(ltr)<=122:
                msg+= chr(int(ltr))
                ltr=""
        return msg
            
    def display(self):
        msg = self.getDecoded()
        print("\nThe encoded message:\n",self.asciiStr,
                "\n\nThe decoded message:\n",msg,"\n", sep='')

print("To decode an ASCII encoded message: ")
encStr = input("Enter the encoded message:\n")

obj = ASCIIDecoder(encStr)
obj.display()