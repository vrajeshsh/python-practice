import os
os.system("cls")

def isEndOfSentence(para, pos):
    paralen = len(para)
    if pos==paralen-1:
        return True
    if para[pos] in ".!?":
        if pos<paralen-1 and para[pos+1]==' ':
            if pos<paralen-2 and para[pos+2].isdigit() or para[pos+2].isupper():
                return True
    return False

def getVowelRichWords(sent):
    word, vowword, vowcnt="", "", 0
    for ch in sent:
        if ch.isalnum():
            word+=ch
            if ch in "AEIOUaeiou":
                vowcnt+=1
        elif word!="":
            if vowcnt>1:
                vowword+=word if vowword=="" else ", "+word
            word,vowcnt="", 0  
    return vowword

print("To display each sentence in a paragraph and show vowel-rich words:")
para = input("Enter the paragraph:\n")
paralen = len(para)

sent, serial, vowword = "", 0, ""
print("\nSentences in the paragraph:")
for i in range(paralen):
    sent+=para[i]
    if isEndOfSentence(para, i):
        sent = sent.strip()
        serial+=1
        print(serial, ". ",sent,sep='')
        vowword= getVowelRichWords(sent) # what -if
        print( "The vowel-rich words: ","None found." if vowword=="" else vowword, "\n")
        sent = ""
