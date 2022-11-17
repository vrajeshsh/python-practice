import os
os.system("cls")

class Palindrome():
    def __init__(self, s):
        self.str = s

    def display(self):
        print("\n","" if self.isPalindrome() else "Non-",
         "Palindromic Sentence\n", sep='')

    def streamline(self):
        new_str = ""
        for i in range(len(self.str)):
            if self.str[i].isalpha():
                new_str+= self.str[i].lower() 
        return new_str

    def isPalindrome(self):
        newstr= self.streamline() 
        return newstr == newstr[::-1]
        
print("To check whether the given string is a Palindrome: ")
str = input("Enter the string: ")

obj = Palindrome(str)
obj.display()