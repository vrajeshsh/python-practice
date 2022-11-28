import os, re
os.system("cls")

class WordSwapper():
    def __init__(self, s, p1, p2):
        self.sent = s
        self.pos1= p1
        self.pos2= p2

    def display(self):
        print("\nThe original sentence:\n", self.sent,
            "\n\nSentence after swapping the words:\n",
                self.getWordsSwapped(),"\n",sep='')

    def getWordAt(self, pos):
        global words
        words = re.split("[,;: ?.!]", self.sent)
        ''' Iterative version
        for i in range(len(words)):
            if not words[i][-1].isalpha():
                words[i] = words[i][:-1]
        '''
        return words[pos - 1]

    def getWordsSwapped(self):
        newstr, word1, word2 =  "", self.getWordAt(self.pos1), self.getWordAt(self.pos2)
        for i in range(len(words)):
            words[i]= word2 if i==self.pos1-1 else word1 if i==self.pos2-1 else words[i]
            newstr+=words[i] if newstr=="" else " "+words[i]
        return newstr+ self.sent[-1] if not self.sent[-1].isalpha() else newstr

print("To display sentence after swapping two words:")
sent = input("Enter the sentence:\n")
pos1 = int(input("Enter word position 1 for swapping: "))
pos2 = int(input("Enter word position 2 for swapping: "))

obj = WordSwapper(sent, pos1, pos2)
obj.display()