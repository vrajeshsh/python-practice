import os
os.system("cls")

print("To shift upper case, lower case and special characters in a sentence:")
sent = input("Enter a sentence:\n")

str, new_sent, lgt, start = list(sent), "", len(sent), 0

for i in range(3):
    for j in range(lgt):
        if i==0 and str[j].isupper() or i==1 and str[j].islower() or\
        i==2 and str[j].isdigit():
            str.insert(start, str.pop(j))
            start+=1
new_sent= new_sent.join(str)

print("\nThe characters of the string after shifting are:\n",new_sent,
    "\n",sep='')