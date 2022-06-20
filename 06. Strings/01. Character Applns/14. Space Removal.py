from multiprocessing.context import SpawnProcess
import os
os.system('cls')

sent = input("Enter a sentence to remove uneven spacing:\n").strip()

new_str=""
sentLen, new_str = len(sent), ""
for i in range(sentLen):
    if sent[i].isalnum() or (sent[i-1] == ' ' and sent[i+1].isalnum()):
        new_str+=sent[i]

print("\nSentence after removing extra spaces:\n",new_str, "\n",  sep='')
