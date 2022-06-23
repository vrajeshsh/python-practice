import os
os.system("cls")

word, new_sent="", ""
print("To remove all occurences of a given word from a sentence:")
sent = input("Enter the sentence:\n")
rem = input("\nEnter the word: ")

for ch in sent:
    if ch.isalnum(): 
        word+=ch
    elif word!="":
        if word.lower() != rem.lower():
            new_sent+= word+ch      # adding the delimeter (space/punctuation) to the new sentence
        if ch!= ' ':
            new_sent= new_sent.strip()+" " # adding a space incase the delimeter was a punctuation
        word=""

print("\nSentence after removing '",rem,"':\n",new_sent,"\n", sep='')