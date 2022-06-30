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

def getLongestPalin(sent):
    word, rev, wordlen, lng_palin, maxi = "", "", 0, "", 0
    for ch in sent:
        if ch.isalnum():
            word+=ch
            rev = ch + rev
            wordlen+=1
        elif word!="":
            if word.lower()==rev.lower() and wordlen>maxi:
                lng_palin = word
                maxi = wordlen
            word, rev, wordlen = "", "", 0
    return lng_palin

print("To display the longest palindromic word in a sentence:")
para = input("Enter the paragraph:\n")
paralen = len(para)

sent, lng_palin, count = "", "", 0
print()
for i in range(paralen):
    sent+=para[i]
    if isEndOfSentence(para, i):
        sent = sent.strip()+" "
        lng_palin = getLongestPalin(sent)
        count+=1
        print(count,". ",sent, sep='')
        print("The longest Palindrome: ", "None exists!" if lng_palin=="" else \
                lng_palin, "\n", sep='')
        sent=""
