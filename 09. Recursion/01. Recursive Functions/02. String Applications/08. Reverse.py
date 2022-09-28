import os
os.system("cls")

def reverse(str):
    str= str[-1]+str[:-1] if str[-1] in ".!?" else str
    return str.upper() if len(str)==1 else reverse(str[1:])+str[0].lower()

print("To print the reverse of a given string:")
sent = input("Enter the string:\n")
lgt = len(sent)
print("\nThe reverse of the sentence:\n",reverse(sent),"\n", sep='')
