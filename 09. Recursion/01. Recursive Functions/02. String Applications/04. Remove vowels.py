import os
os.system("cls")

def removevowels(sent):
    if len(sent)==0:
        return sent
    if sent[0].lower() in "aeiou":
        return removevowels(sent[1:len(sent)+1])
    return sent[0]+removevowels(sent[1:len(sent)+1])

print("To remove all vowels from a given string:")
sent = input("Enter the sentence:\n")

print("\nSentence after removing all vowels:\n",removevowels(sent),"\n",sep='')