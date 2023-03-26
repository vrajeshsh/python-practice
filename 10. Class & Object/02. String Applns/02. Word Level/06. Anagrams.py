import os, re
os.system("cls")

class FindAnagrams():
    def __init__(self, s):
        self.sent = s

    def display(self):
        anagrams = self.findAnagrams()
        print("\nThe given sentence:\n",self.sent, sep='')
        if anagrams=="":
            print("\nNo anagrams found in the sentence!\n", sep='')
        else:
            print("\nAnagrams found in the sentence are:", anagrams, "\n",sep='')
     
    def areAnagrams(self, str1, str2):
        word1, word2 = str1.replace(" ", "").lower(), str2.replace(" ", "").lower()
        return sorted(word1)==sorted(word2) and word1!=word2
    
    def findAnagrams(self):
        words, anagrams, i = re.split("[,;: ?.!]", self.sent), "", 0
        for i in range(len(words) - 1):
            for j in range(i, len(words)):
                if self.areAnagrams(words[i], words[j]):
                    anagrams+="\n"+words[i].title()+", "+words[j].title()
                elif self.areAnagrams(words[i], words[j-1]+words[j]):
                    anagrams+="\n"+words[i].title()+", "+words[j-1].title()+" "+words[j].title()
        return anagrams

print("To display all anagrams present in a sentence:")
sent = input("Enter the sentence:\n")

obj = FindAnagrams(sent)
#print(obj.areAnagrams("Swear Oft", "software"))
obj.display()        