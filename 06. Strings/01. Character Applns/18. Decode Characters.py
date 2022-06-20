import os
os.system("cls")

def replaceChar(char):
    if ord(char)==90:
        return "a"
    elif ord(char)==122:
        return "A"
    elif 65<=ord(char)<=89:
        return chr(ord(char)+1).lower()
    elif 97<=ord(char)<=121:
        return chr(ord(char)+1).upper()
    else:
        return char

new_str=""
sent = input("Enter a sentence to check replace characters in a circular manner:\n")

for i in sent:
    new_str+=replaceChar(i)

print("\n",new_str,"\n")