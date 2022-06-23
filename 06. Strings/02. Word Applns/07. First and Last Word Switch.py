import os
os.system("cls")

print("To switch first and last words in a sentence:")
sent = input("Enter the sentence:\n").strip()

new_sent = sent[sent.rfind(" ")+1:]+sent[sent.find(" "):sent.rfind(" ")+1]+sent[:sent.find(" ")]

print("\nSentence after switch:\n",new_sent,"\n",sep='')
