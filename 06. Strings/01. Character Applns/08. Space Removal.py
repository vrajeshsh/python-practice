import os
os.system('cls')

new_str=""
sent = input("Enter a sentence to remove extra spaces:\n").strip()

sentLen= len(sent)
for i in range(sentLen):
    if sent[i]== ' ' and sent[i+1]==' ':
        continue
    new_str+= sent[i]

print("\nSentence after removing extra spaces:\n",new_str,"\n", sep='')