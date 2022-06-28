import os
os.system("cls")

print("To replace all occurances of substring in a sentence:")
sent = input("Enter the sentence:\n")
substr = input("Enter substring to search: ")
new_substr = input("Enter substring to replace with: ")

sentlen, sublen, new_str, i, isFound= len(sent), len(substr), "", 0, False

while i<sentlen:
    if not sent[i:i+sublen].lower()==substr.lower():
        new_str+= sent[i]
        i+=1
    else:
        isFound = True
        new_str+=new_substr
        i+=sublen

if not isFound:
    print("\nSubstring",substr,"could not be found in the sentence!\n")
else:    
    print("\nAfter replacing ",substr," with ",new_substr,":\n",new_str,"\n", sep='')