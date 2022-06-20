import os
os.system("cls")

def convertChar(char):
    if char.isalpha():
        return "Z" if char=="A" else "z" if char=="a" else chr(ord(char)-1)
    elif char.isdigit():
        return "9" if char=="0" else str(int(char)-1)
    elif char.isspace():
        return "$"
    else:
        return char
    
new_str=""
sent = input("Enter a sentence to check convert characters in a circular manner:\n")

for i in sent:
    new_str+= convertChar(i)

print("\n",new_str,"\n")