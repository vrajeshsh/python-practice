import os
os.system("cls")

class PalindromicWords():
    def __init__(self, s):
        self.sent = s

    def display(self):
        palsLenwise= self.getPalsLenwise()
        
        if palsLenwise == "":
            print("\nNo Paindromes exist in the sentence!\n", sep='')
        else:
            print("\nThe Palindromic words arranged lengthwise are:\n", palsLenwise, 
                "\n", sep='')
    
    def getPalsLenwise(self):
        word, rev, palinStr = "", "", ""

        for wrdLen in range(20, 2, -1):  # loop generating all lengths possible in desc order
            for ch in self.sent:
                if ch.isalnum():
                    word+= ch
                    rev = ch+rev
                elif word!="":
                    if word.lower() == rev.lower() and len(word) == wrdLen:  # if a valid pal is found
                        if word not in palinStr:
                            palinStr+= word.title() if palinStr=="" else ", "+word.title() 
                    word= rev = ""
        return palinStr
    
print("To display all palindromic words sorted lengthwise:")
sent = input("Enter the sentence:\n")

obj = PalindromicWords(sent)
obj.display()