import os
os.system("cls")

count=0
sent = input("Enter a sentence for counting number of words:\n")
for i in range(len(sent)):
    if (sent[i-1].isspace() and sent[i].isalnum()) or\
        (i==0 and sent[0].isalnum()):
        count+=1

print("\nThere are",count,"words in the sentence.\n")