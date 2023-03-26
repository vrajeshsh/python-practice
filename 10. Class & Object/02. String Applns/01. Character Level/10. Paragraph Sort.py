import os
os.system("cls")

class ParaSorter():
    def __init__(self, para):
        self.para = para
        self.vowWords = ""
    
    def isEndOfSentence(self, indx):
        paralen = len(self.para)
        if indx==paralen-1:
            return True
        if self.para[indx] in ".!?":
            if indx<paralen-1 and self.para[indx+1]==' ':
                if indx<paralen-2 and self.para[indx+2].isdigit() or self.para[indx+2].isupper():
                    return True
        return False
            
    def getVowelousWords(self, sent):
        word=""
        for ch in sent:
            if ch.isalnum():
                word+=ch
            else:
                if word[0].lower() in "aeiou" and word.lower() not in self.vowWords.lower():
                    self.vowWords+= word.title() if self.vowWords=="" else ", "+word.title()
                word=''
        
    def getSorted(self, sent):
        new_str, word, sentLen = "", sent.lower().split(" "), len(sent)
        for i in range(len(word)):
            if word[i][-1] in ".,!?":
                word[i] = word[i][:-1]
        word.sort()
        for i in range(len(word)):
            new_str+= word[i].title() if new_str=="" else " "+word[i]
        new_str= new_str.strip() + ("" if sent[sentLen-1].isalpha()  else sent[sentLen-1]) # adding the punctuation
        return new_str 

    def getParaSorted(self):
        sent, sortedPara, i = "", "", 0
        while(i < len(self.para)):
            sent+= self.para[i]
            if self.isEndOfSentence(i):
                sortedPara+= self.getSorted(sent)+ " "
                self.getVowelousWords(sent)
                sent = ""
                i+= 1
            i+= 1
        print("\nThe sorted (wordwise) paragraph:\n", sortedPara,
            "\n\nVowelous word(s) found: ", self.vowWords,"\n", sep='')
        
print("To arrange sentences in alphabetical order and separate the words that begin with a vowel:")
para = input("Enter the paragraph:\n")

obj = ParaSorter(para)
obj.getParaSorted()