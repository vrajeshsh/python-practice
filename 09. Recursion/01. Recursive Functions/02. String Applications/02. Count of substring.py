import os
os.system("cls")

def countoccurs(str, srch):
    len_str, len_srch = len(str), len(srch)
    if len_str==0:
        return 0
    if str[0:len_srch].lower() == srch.lower():
        return 1+countoccurs(str[1:], srch)
    return countoccurs(str[1:], srch)    

print("To search for a substring in a string:")
str = input("Enter the string:\n")
srch = input("\nEnter the search string:\n")

count = countoccurs(str, srch)
if count>0:
    print("\n'",srch,"' occurs ",count," time(s).\n", sep='')
else:
    print("\n'",srch,"' NOT found!\n", sep='')