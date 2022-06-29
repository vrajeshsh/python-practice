import os
os.system("cls")

def isendofsentence(para, pos):
    paralen = len(para)
    if pos == paralen-1:
        return True
    if para[pos] in ".!?":
        if pos < paralen-1 and para[pos+1]==' ':
            if pos < paralen-2 and para[pos+2].isupper() or para[pos+2].isdigit():
                return True
    return False
 
print("To display all sentences of a paragragh in a new line:")
para = input("Enter the paragraph:\n").strip()+"  "
paralen = len(para)

sent, count = "", 0

print("\nSentences in the paragraph:")
for i in range(paralen):
    sent+= para[i]
    if isendofsentence(para, i):
        count+=1
        print(count,". ",sent.strip(), sep='')
        sent = ""
print("\n")