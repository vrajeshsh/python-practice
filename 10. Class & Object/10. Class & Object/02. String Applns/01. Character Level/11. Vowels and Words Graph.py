import os
os.system("cls")

class VolWordGraph():
    def __init__(self, para, scale):
        self.para = para
        self.vCount, self.wCount, self.scale = [], [], scale
        vowCnt, wrdCnt, i = 0, 0, 0
        while(i < len(self.para)):
            ch= self.para[i]
            if ch in "AEIOUaeiou":
                vowCnt+= 1
            if not ch.isalnum():
                wrdCnt+= 1
            if self.isEndOfSentence(i):
                self.vCount.append(vowCnt)
                self.wCount.append(wrdCnt)
                vowCnt=wrdCnt= 0
                i+= 1
            i+= 1
    
    def isEndOfSentence(self, indx):
        paralen = len(self.para)
        if indx==paralen-1:
            return True
        if self.para[indx] in ".!?":
            if indx<paralen-1 and self.para[indx+1]==' ':
                if indx<paralen-2 and self.para[indx+2].isdigit() or self.para[indx+2].isupper():
                    return True
        return False

    def showTable(self):
        count = 0
        print("\nSentence #\tNo. of vowels\tNo. of words")
        for i in range(len(self.vCount)):
            count+=1
            print(count, "\t\t", self.vCount[i], "\t\t", self.wCount[i])
        

    def showGraph(self):
        count = 0
        print("\nSentence #\tNo. of vowels\t\t\t\tNo. of words")
        for i in range(len(self.vCount)):
            count+=1
            print(count,"\t\t", "V"*self.scale*self.vCount[i], "\t\t\t\t", "W"*self.wCount[i]*self.scale, sep='')
            i+=1

print("To count the vowels and words in a sentence and display it as a graph:")
para = input("Enter the paragraph:\n")
scale = int(input("\nEnter the scale: "))

obj = VolWordGraph(para, scale)
obj.showTable()
obj.showGraph()
print()