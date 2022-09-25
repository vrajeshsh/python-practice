import os
os.system("cls")

def isPresent(str, srch): 
    len_str, len_srch = len(str), len(srch)
    if len_srch>len_str:
        return False
    if str[0:len_srch]==srch.lower():
        return True
    return isPresent(str[1:], srch)

print("To search for a substring in a string:")
str = input("Enter the string:\n")
srch = input("Enter the search string:\n")

print("\n",srch," is ","" if isPresent(str, srch) else "NOT ", "present in ",str,".\n", sep='')