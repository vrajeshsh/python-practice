import os
os.system("cls")

def isPalindromic(word):
    if len(word)==1:
        return True
    if word[0].lower()==word[-1].lower():
        return isPalindromic(word[1:-1])
    return False

print("To check whether or not a given word is Palindromic:")
word = input("Enter the word: ")

print("\n",word," is","" if isPalindromic(word) else " NOT", " a Palindromic word.\n", sep='')

