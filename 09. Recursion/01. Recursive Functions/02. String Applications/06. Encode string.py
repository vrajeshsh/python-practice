import os
os.system("cls")

def getcoded(char, n):
    if 65<=ord(char)<=90-n or 97<=ord(char)<=122-n or 48<=ord(char)<=59-n:
        return chr(ord(char)+n)
    elif ord(char)>59:
        return chr(ord(char)+n-26)
    else:
        return chr(ord(char)+n-10)

def encodechars(str):
    if len(str)==0:
        return str
    if str[0].isalnum():
        return getcoded(str[0],n)+encodechars(str[1:len(str)+1])
    return str[0]+encodechars(str[1:len(str)+1])

print("To encode a sentence by replacing all characters by nth letter/digit:")
sent = input("Enter the sentence:\n")
n = int(input("\nEnter the shift value: "))

print("\nThe encoded sentence:\n",encodechars(sent),"\n", sep='')
