from email.headerregistry import UniqueSingleAddressHeader
from operator import indexOf
import os
os.system("cls")

last_word, new_sent, first_word="", "", ""
print("To switch first and last words in a sentence:")
sent = input("Enter the sentence:\n").strip()+" "

first_word = sent[0:sent.index(" ")]
last_word = sent[-sent.index(" "):-1]
mid_words = sent[sent.index(" ")+1:-sent.index(" ")-1]
#new_sent = sent[sent.rfind(" ")+1:-1] +\sent[sent.index(" "):-sent.index(" ")-1] +\

new_sent = last_word+" "+mid_words+" "+first_word 

print("\nSentence after switch:\n",new_sent,"\n",sep='')