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

print("To display sentences in ascending order of length:")
para = input("Enter the paragraph:\n")

count, wrdCnt, currCnt, paralen = 0, 0, 0, len(para)
print()
for i in range(1, 200):
    sent = ""
    for j in range(paralen):
        sent+=para[j]
        if isEndOfSentence(para, j):
            sent = sent.strip()
            sentlen = len(sent)
            if i == sentlen:
                count+=1
                print(count, ". ",sent,sep='')
            sent=""
print()