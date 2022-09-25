import os
os.system("cls")

def countconsonants(sent):
    if sent=='':
        return 0
    if sent[0].lower() not in "aeiou" and sent[0].isalpha():
        return 1+countconsonants(sent[1:])
    return countconsonants(sent[1:])

print("To count the number of occurances of consonants in a given string:")
sent = input("Enter the sentence:\n")

print("\nCount of consonants: ",countconsonants(sent),"\n",sep='')