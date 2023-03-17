import os
os.system("cls")

class palSubstring():
    def __init__(self, s):
        self.str = s

    def display(self):
        palInCaps = self.makePalSubsInCaps()
        print("\nThe given sentence:\n", self.str,
        "\n\nSentence after changing Palindromic substrings to upper case:\n",palInCaps,
        "\n",sep='')

    def isPalindrome(self, substr):
        return substr.lower()==substr[::1].lower()

    def makePalSubsInCaps(self):
        words, palin, newStr = self.str.split(), "", ""
        for word in words:
            for i in range(len(word)):
                for j in range(i+1, len(word)+1):
                    palin=palin + (word[i:j+1].upper() if self.isPalindrome(word[i:j+1]) else word[i:j+1])
            newStr+=palin
        return newStr

print("To display Palindromic substrings in upper case:")
sent = input("Enter the sentence: ")

obj = palSubstring(sent)
obj.display()

#not done sir