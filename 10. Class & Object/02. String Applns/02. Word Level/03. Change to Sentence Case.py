import os
os.system("cls")

class SentenceCase():
    def __init__(self, sent):
        self.sent = sent
        self.lgt = len(self.sent)

    def display(self):
        print("\nThe given sentence:\n",self.sent,
            "\n\nSentence after changing to sentence case:\n", self.convert(),"\n", sep='')

    def isInUppercase(self, word):
        return word.isupper()

    def convert(self):
        word, count, newStr = "", 0, ""
        for ch in self.sent+" ":    #same algorithm used 'cheekily'...
            if ch.isalnum():
                word+=ch
            elif word!="":
                count+=1
                if word=="i":
                    word = "I"
                elif not self.isInUppercase(word):
                    word = word.title() if count==1 else word.lower()
                newStr+= word+ch
                if ch!=" ":
                    newStr+=" "
                word = ""
        if newStr.strip()[-1].isalnum():
            newStr = newStr.strip()+"."            
        return newStr

print("To convert a sentence into Sentence case:")
sent = input("Enter the sentence:\n")

obj = SentenceCase(sent)
obj.display()                