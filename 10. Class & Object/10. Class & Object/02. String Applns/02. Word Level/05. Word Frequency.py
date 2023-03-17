import os, re
os.system("cls")

class WordsFreqwise():

    def __init__(self, sent):
        self.sent = sent
        self.lgt = len(sent)
        global words
        words = re.split("[,;: ?.!]", self.sent)

    def display(self):
        print("\nThe given sentence:\n",self.sent,
            "\n\nWORD\t\tFREQUENCY",self.showWordsFreqwise(),"\n", sep='')

    def getFrequency(self, word):
        return self.sent.count(word)

    def showWordsFreqwise(self):
        freqStr = ""
        # for i in range(10, 1, -1):
        #     for wrd in words:
        #         freq = self.getFrequency(wrd)
        #         if freq==i and wrd not in freqStr:
        #             freqStr+=wrd+"\t\t"+freq+"\n"
        words.sort()
        words.sort(key=self.getFrequency, reverse = True)
        for wrd in words:
            if wrd not in freqStr:
                freqStr+="\n"+wrd+"\t\t"+str(self.getFrequency(wrd))
        return freqStr

print("To arrange words in a sentence in order of their frequencies:")
sent = input("Enter the sentence:\n")

obj = WordsFreqwise(sent)
obj.display()