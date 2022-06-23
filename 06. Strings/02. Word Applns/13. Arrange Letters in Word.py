import os
os.system("cls")

# Not now, someday you will learn to replace the below code by a single piece of code
def sortword(word):
    new_word = ""
    for i in range(97, 123):
        for chr in word:
            if i==ord(chr.lower()):
                new_word+= chr
    return new_word

print("To display all words in a sentence alphabetically:")
sent = input("Enter the sentence:\n").strip()+" "

word, sorted_sent= "", ""

for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        sorted_sent+= sortword(word)+ch
        if ch != ' ':
            sorted_sent+= " "
        word=""

print("\nThe sentence after arranging the words alphabetically:\n",
    sorted_sent,"\n", sep='')