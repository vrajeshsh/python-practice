import os, re
os.system("cls")

class WordFrequency():
    def accept(self):
        self.sent = input("Enter the sentence: ")
        global words
        words = re.split(r'\W+', self.sent)
        print("\nFor testing purposes:\nThe words of the sentence:\n", words)

        ''' This (as done below) people use to code in 1987 - that also in C++.
        In Java and Python, there are better ways!!
        self.words,self.allwords, word = [],[], ""
        for ch in self.sent:
            if ch.isalnum():
                word+=ch
            else:
                self.allwords.append(word.lower())
                if word.lower() not in self.words and word not in ".,!?":
                    self.words.append(word.lower())
                word = ""
        '''
    # Work of this program later whenever free... Th task remaining is very little
    # hope you would be able to complete...
    def display(self):
        print("\nThe sentence:\n", self.sent, sep='')
        self.word_frequency_wise()

    def frequency(self, word):
        return self.allwords.count(word)

    def words_frequency_wise(self):
        print("\nWORD\t\tFREQUENCY", sep='')
        sorted_list = sorted(self.words, key=self.frequency, reverse = True)
        for i in range(len(self.words)):
            print(sorted_list[i],"\t\t",self.frequency(sorted_list[i]), sep='')
        
            
print("To display words in a sentence in decreasing order of frequency:")

obj = WordFrequency()
obj.accept()
obj.display()
obj.words_frequency_wise()
print()