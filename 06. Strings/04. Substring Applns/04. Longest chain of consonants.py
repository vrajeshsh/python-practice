import os
os.system("cls")

print("To find the longest chain consonants in a sentence:")
sent = input("Enter the sentence:\n")

sentlen, start, end, maxlen, consolen = len(sent), 0, 0, 0, 0 
conso_str, lngest_con = "", ""

for i in range(sentlen):
    if sent[i] not in "AEIOUaeiou":
        conso_str+=sent[i]
        if sent[i].isalpha():
            consolen+=1 
    else: 
        if maxlen < consolen:
            maxlen = consolen
            lngest_con = conso_str
            start = i-1-consolen
            end = i-1
        conso_str, consolen = "", 0

if lngest_con=="":
    print("\nNo consonants were found in the sentence!\n")
else:    
    print("\nLongest consonant chain in the sentence: ", lngest_con,
        "\nPosition of the consonant chain: ", start," - ",end,"\n", sep='')