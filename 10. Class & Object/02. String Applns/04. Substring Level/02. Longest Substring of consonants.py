import os
os.system("cls")

class ConsoChain():
    def __init__(self, s):
        self.sent = s

    def display(self):
        print("\nThe given sentence:\n", self.sent,sep='')

    def isVowel(self, ch):
        return ch.lower() in "aeiou"

    def longestConsoChain(self):
        maxLen, longSubstr, currSubstr, sentLen, consLen, pos = 0, "", "", len(self.sent), 0, ""
        for i in range(sentLen):
            ch = self.sent[i]
            if not self.isVowel(ch):
                currSubstr+=ch
                if not self.isVowel(ch):
                    consLen+=1
            else:
                if maxLen < consLen:
                    maxLen = consLen
                    longSubstr = currSubstr
                    pos = str(i-consLen) + " - " + str(i) # to fix the position
                currSubstr, consLen = "", 0

        if longSubstr=="":
            print("\nNo consonants were found in the sentence!\n")
        else:
            print("\nLongest consonant substring in the sentence: ", longSubstr,
            "\nPosition of the substring: ",pos, "\n", sep='')

print("To display the longest substring of consonants and its position:")
sent = input("Enter the sentence:\n")

obj = ConsoChain(sent)
obj.display()
obj.longestConsoChain()
