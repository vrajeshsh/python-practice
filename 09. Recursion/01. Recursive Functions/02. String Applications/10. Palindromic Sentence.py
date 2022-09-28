import os
os.system("cls")

def isPalindrome(str, p1, p2):
    if p1==p2:
        return True
    if not str[p1].isalpha():
        return isPalindrome(str, p1+1, p2)
    if not str[p2].isalpha():
        return isPalindrome(str, p1, p2-1) 
    if str[p1].lower()!=str[p2].lower():
        return False
    else:
        return isPalindrome(str, p1+1, p2-1)
    

print("To check if the given sentence is Palindromic or not:")
sent = input("Enter the sentence:\n")
lgt = len(sent)
print("\n","" if isPalindrome(sent, 0, lgt-1) else "Non-","Palindromic sentence.\n", sep='')

''' Fix the code after considering the faulty I/O given below:
To check if the given sentence is Palindromic or not:
Enter the sentence:
     Was   it    a      Ca t,,, or a car,,, i saw???

Palindromic sentence.
'''