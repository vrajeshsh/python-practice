import os
os.system("cls")

print("To delete all occurances of substring in a sentence:")
sent = input("Enter the sentence:\n")
substr = input("Enter the substring: ")

sentlen, sublen, new_str, i, isFound= len(sent), len(substr), "", 0, False

while i<sentlen:
    if not sent[i:i+sublen].lower()==substr.lower():
        new_str+= sent[i]
        i+=1
    else:
        isFound=True
        i+=sublen

if not isFound:
    print("\nSubstring",substr,"could not be found in the sentence!\n")
else:  
    print("\nSentence after deleting ",substr,":\n",new_str,"\n", sep='')
