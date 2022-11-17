import os
os.system("cls")

class CaseChanger():
    def __init__(self, s):
        self.str = s

    def display(self):
        print("\n",self.toToggleCase(),"\t(Toggle Case)",
            "\n",self.toTitleCase(),"\t(Title Case)",
            "\n",self.toLetterCase(),"\t(Letter Case)\n",sep='')

    def toToggleCase(self):
        new_str = ""
        for i in range(len(self.str)):
            new_str+= self.str[i].lower() if self.str[i].isupper() else self.str[i].upper()
        return new_str

    def toTitleCase(self):
        new_str = self.str[0].upper()
        for i in range(1, len(self.str)):
            new_str+= self.str[i].upper() if self.str[i-1]== ' ' else self.str[i].lower()
        return new_str

    def toLetterCase(self):
        new_str = ""
        for i in range(len(self.str)):
            new_str+= self.str[i].lower() if self.str[i].lower() in "aeiou" else self.str[i].upper()
        return new_str

print("To display the given sentence in Toggle, Title and Letter cases:")
str = input("Enter the string: ")

obj = CaseChanger(str)
obj.display()