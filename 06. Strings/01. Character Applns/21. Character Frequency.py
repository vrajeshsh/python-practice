import os
os.system("cls")

newsent = ""

sent = input("Enter a string to count frequency of each character:\n")

print("\nCHARACTER\t\tFREQUENCY")
for ch in sent:
    if ch.upper() not in newsent.upper():
        print("<space>\t\t\t" if ch==' ' else ch+"\t\t\t\t",
            sent.upper().count(ch.upper()))
    newsent+= ch