import os
os.system("cls")

def getWordAt(sent, pos): 
    count, word= 0, ""
    for ch in sent:
        if ch.isalnum():
            word+=ch
        elif ch!="":
            count+=1
            if count==pos:
                return word
            word=""
    return ""

word, count, new_str= "", 0, ""

print("To swap any two words in a sentence:")
sent = input("Enter the sentence:\n").strip()+" "
pos1 = int(input("Enter first position: "))
pos2 = int(input("Enter second position: "))

word1, word2 = getWordAt(sent, pos1), getWordAt(sent, pos2)
if word1=="" or word2=="":
    print("\nInvalid position(s) given!\n")
    exit()
for ch in sent:
    if ch.isalnum():
        word+=ch
    elif word!="":
        count+=1
        word = word2 if count==pos1 else word1 if count==pos2 else word
        new_str+= word+ch
        if ch!=" ":
            new_str+=" "
        word=""

print("\nThe new sentence after swapping the words:\n",new_str,"\n", sep='')

