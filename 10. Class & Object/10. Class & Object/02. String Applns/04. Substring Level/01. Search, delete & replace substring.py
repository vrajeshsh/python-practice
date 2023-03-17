import os
os.system("cls")

class Substring():
    def __init__(self, s):
        self.sent = s
        self.sentLen = len(s)

    def display(self):
        print("\nThe given sentence:\n", self.sent,"\n")
                 
    def findMatches(self, substr):
        pos, substrLen = "", len(substr)
        for i in range(self.sentLen-substrLen+1):
            if self.sent[i:i+substrLen].lower()==substr.lower():
                pos+=str(i+1) if pos=="" else ", "+str(i+1)
        if pos == "":
            print("\nThe substring '",self.substring,"' NOT found in the given sentence!\n", sep='')
        else:
            print("\nThe substring '",substr,"' occurs at positions: ", pos)    

    def deleteSubstring(self, substr):
        i, newStr, substrLen = 0, "", len(substr)
        while i<self.sentLen:
            if not self.sent[i:i+substrLen].lower()==substr.lower():
                newStr+=self.sent[i]
                i+=1
            else:
                i+=substrLen
        if newStr == self.sent:
            print("\nThe substring '",self.substring,"' NOT found in the given sentence!\n", sep='')
        else:
            print("\nThe new sentence after removing all occurrences of '", substr,"':\n", newStr, sep='')

    def replaceSubstring(self, substr, repstr):
        i, newStr, substrLen = 0, "", len(substr)
        while i<self.sentLen:
            if not self.sent[i:i+substrLen].lower()==substr.lower():
                newStr+=self.sent[i]
                i+=1
            else:
                newStr+=repstr
                i+=substrLen
        if newStr == self.sent:
            print("\nThe substring '",self.substring,"' NOT found in the given sentence!\n", sep='')
        else:
            print("\nThe new sentence after replacing all occurrences of '", substr,"' by '",repstr,"':\n", newStr,"\n", sep='')

sent = input("Enter a sentence:\n")
substr = input("Enter substring to search: ")
repstr = input("Enter substring to replace with: ")

obj = Substring(sent)
obj.display()
obj.findMatches(substr)
obj.deleteSubstring(substr)
obj.replaceSubstring(substr, repstr)
# Just add 1 to the indices that are getting generated for matches. 
