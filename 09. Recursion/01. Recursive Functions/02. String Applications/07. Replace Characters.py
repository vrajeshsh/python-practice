import os
os.system("cls")

def getaltered(char):
    if char.islower():
        vow = ['a','e','i','o','u']
        if char in vow:
            return vow[(vow.index(char)+1)%5]
        elif char=="b":
            return "z"
        else:
            return chr(ord(char)-1) if chr(ord(char)-1) not in vow else chr(ord(char)-2)
    elif char.isupper():
        vow = ['A','E','I','O','U']
        if char in vow:
            return vow[(vow.index(char)+1)%5]
        elif char=="B":
            return "Z"
        else:
            return chr(ord(char)-1) if chr(ord(char)-1) not in vow else chr(ord(char)-2)
    else:
        return str(9-int(char))

def replacechars(str):
    if len(str)==0:
        return str
    if str[0].isalnum():
        return getaltered(str[0])+replacechars(str[1:len(str)+1])
    return str[0]+replacechars(str[1:len(str)+1])

print("To replace every vowel by the next, consonant bey the prev and digit by its complement:")
sent = input("Enter the sentence:\n")

print("\nThe altered sentence:\n",replacechars(sent),"\n", sep='')
