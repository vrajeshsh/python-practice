import os
os.system("cls")

def spacewithuscore(str):
    if len(str)==0:
        return str
    if str[0]==" ":
        return "_"+spacewithuscore(str[1:])
    return str[0]+spacewithuscore(str[1:])

print("To replace all space in a string with an underscore:")
sent = input("Enter the sentence:\n")

print("\nThe sentence after replacement:\n",spacewithuscore(sent),"\n", sep='')