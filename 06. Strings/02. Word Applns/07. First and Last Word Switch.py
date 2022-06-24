import os
os.system("cls")

print("To switch first and last words in a sentence:")
sent = input("Enter the sentence:\n").strip()


end = "" if sent[-1].isalnum() else sent[-1]
last = sent[sent.rfind(" ")+1:] if sent[-1].isalnum() else sent[sent.rfind(" ")+1:-1]
new_sent = last +sent[sent.find(" "):sent.rfind(" ")+1]+sent[:sent.find(" ")]+end

print("\nSentence after switch:\n",new_sent,"\n",sep='')
