import os
os.system('cls')

class VowelWordCounter():
    def __init__(self, para, scale):
        self.para = para
        self.paraLen = len(para)
        self.scale = scale
        self.vowCnt, self.wrdCnt = [], []
        vCnt, wCnt, i = 0, 0, 0
        while i<self.paraLen:
            ch = self.para[i]
            if self.isVowel(ch):
                vCnt+=1
            if not ch.isalnum():
                wCnt+=1
            if ch in ".!?":
                self.vowCnt.append(vCnt)
                self.wrdCnt.append(wCnt)
                vCnt = wCnt = 0
                i+=1
            i+=1


    def display(self):
        print("\nThe given sentence:\n", self.para,sep="")

    def isVowel(self, ch):
        return ch.lower() in "aeiou"

    def showCounterTable(self):
        sentCnt = 0
        print("\nSentence #\tNo. of Vowels\tNo. of Words")
        for i in range(len(self.vowCnt)):
            sentCnt+=1
            print(sentCnt, "\t\t", self.vowCnt[i], "\t\t", self.wrdCnt[i])
        

    def showCounterGraph(self):
        sentCnt = 0
        print("\nSentence #\tNo. of Vowels\t\tNo. of Words")
        for i in range(len(self.vowCnt)):
            sentCnt+=1
            print(sentCnt, "\t\t", "V"*self.scale*self.vowCnt[i], "\t\t\t\t", "V"*self.scale*self.wrdCnt[i])


print("To count the vowels and words in a sentencve and display it as a graph:")
para = input("Enter the sentence:\n")
scale = int(input("\nEnter the scale: "))

obj = VowelWordCounter(para, scale)
obj.display()
obj.showCounterTable()
obj.showCounterGraph()
print()

# sir just one question, what about the scale parameter?? Is it okay to use?
# Yeah, initially although I had mentioned and my program used it... but while designing the class I FORGOT TO ADD IT IN THE __init__() function!!!
# But yu HANDLED IT well.

#not done 

# Well the entire PLANNING for this program needs to be changed!!!
''' Think 'this way':
What if you could get hold of the main things that are required for both the two requirements:
(i) Count of the vowels
(ii) Count of the words
From some source...

Then how nicely the two functions could be busy only in making the table and the Bar-graph
without caring for the sentence extraction or running loops for finding the same counts
repeatedly in the two functons.

True my hint is almost like the old story- 'We (the mice) will be very happy if we can bell the cat!!'
But then how hard it is to Bell the Cat we all know!!

Nonetheless, if you try hard, very simply you can understand the TRICK and handle the requirements.
'''