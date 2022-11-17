import os
os.system("cls")

class TextDecoder():
    def __init__(self, encStr, shift):
        self.encStr = encStr
        self.shift = shift

    def decodedChar(self, char, n):
        if 65<=ord(char)<=90:
            if ord(char)+n-1<=90:
                return chr(ord(char)+n-1)
            return chr(ord(char)-27+n)
        return ""

    def getDecoded(self):
        decMsg, i ="", 0
        while i<len(self.encStr):
            decChr = self.decodedChar(self.encStr[i], self.shift)
            if self.encStr[i]==self.encStr[i+1] and decChr=='Q':
                decMsg+=" "
                i+=1
            else:
                decMsg+= decChr
            i+=1
        return decMsg
    
    def display(self):
        decMsg = self.getDecoded()
        print("\nThe encode text:\n",self.encStr,
            "\n\nThe decoded text:\n",decMsg,"\n",sep='')

print("To decode an encoded text message:")
encStr = input("Enter a encoded text:\n")
shift = int(input("Enter the shift value: "))

obj = TextDecoder(encStr, shift)
if 1<=shift<=26:
    obj.display()
else:
    print("\nINVALID SHIFT VALUE!\n")