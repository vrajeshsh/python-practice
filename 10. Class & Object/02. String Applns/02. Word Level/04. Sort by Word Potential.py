import os, re
os.system('cls')

class SortWordsByPotentials():
    def __init__(self, sent):
        self.sent = sent
        self.lgt = len(sent)

    def display(self):
        print("\nThe given sentence:\n", self.sent,
                "\n\nSentence in ascending order of potential:\n", 
                    self.sortWords(),"\n", sep='')

    def getPotential(self, word):
        pot = 0
        for ch in word:
            pot+= ord(ch.upper()) - 64
        return pot

    def sortWords(self):
        words, newStr = re.split("[,;: ?.!]", self.sent), ""
        words.sort(key = self.getPotential)
        for wrd in words:
            newStr+= wrd + " "
        return newStr
    
print("To display the words of sentence in ascending order of their potentials:")
sent = input("Enter the sentence:\n")

obj = SortWordsByPotentials(sent)
obj.display()