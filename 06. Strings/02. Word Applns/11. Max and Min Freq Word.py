import os
os.system("cls")

word, most, least, count, new_word ="", "", "", 0, ""

print("To display the most and least occuring words in a sentence:")
sent = input("Enter the sentence:\n").strip()+" "

maxi, mini = 0, 100

for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        freq = sent.lower().count(word.lower()+ch)
        if freq>maxi:
            maxi = freq
            most = word
        if freq<mini:
            mini = freq
            least = word
        word=""

print("\nMost occuring word:",most,"\nLeast occuring word:", least,"\n")
