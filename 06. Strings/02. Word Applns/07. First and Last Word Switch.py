from email.headerregistry import UniqueSingleAddressHeader
from operator import indexOf
import os
os.system("cls")

print("To switch first and last words in a sentence:")
sent = input("Enter the sentence:\n").strip()

first_word = sent[:sent.find(" ")]
last_word = sent[sent.rfind(" ")+1:]
mid_words = sent[sent.find(" "):sent.rfind(" ")+1]

new_sent = last_word+mid_words+first_word 

print("\nSentence after switch:\n",new_sent,"\n",sep='')
