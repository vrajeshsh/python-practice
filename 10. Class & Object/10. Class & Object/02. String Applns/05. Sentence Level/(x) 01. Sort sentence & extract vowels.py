import os
os.system('cls')

class SentenceSorter():
    def __init__(self, para):
        self.para = para
        self.paraLen = len(para)

    def display(self):
        print("\nThe given sentence:\n",self.para,
        "\n\nThe sentence after arranging words in alphabetical order:\n", self.sortParagraph(),
        "\n\nVowels: ",self.vowelWords(),"\n", sep='')

    def isVowel(self, ch):
        return ch.lower() in "aeiou"

    def vowelWords(self):
        words, vowWords = self.para.split(), ""
        for word in words:
            if self.isVowel(word[0]):
                vowWords = word         # STOP Repetitions of words here. [Program specs does mention that!!]
        return vowWords

    def sortSentence(self, sent):
        words, newStr = sent.lower().split(), ""
        for i in range(len(words)):
            if words[i][-1] in ".,!?":
                words[i] = words[i][:-1]
        words.sort()
        for i in range(len(words)):
            newStr+= words[i].title() if newStr=="" else " "+words[i]
        newStr = newStr.strip() + ("" if sent[-1].isalpha() else sent[-1])
        return newStr

    # 2002 year Python coding spotted above and below DESPITE having shown a lot of proper and pure Python codes
    # Ti: Use the split() function to shorten the code using better and simoler algorithms...

    def sortParagraph(self):
        i, sent, sortedPara = 0, "", ""
        while i<self.paraLen:
            sent+= self.para[i]
            if self.para[i] in ".!?" or i==self.paraLen - 1:
                sortedPara+= " "+self.sortSentence(sent)
                sent = ""
                i+=1
            i+=1
        return sortedPara.strip()

print("To arrange sentences of a paragraph in alphabetical order and extract words that start with a vowel:")
sent = input("Enter the sentence:\n")

obj = SentenceSorter(sent)
obj.display()