import os
os.system("cls")

print("To search for substring in a sentence:")
sent = input("Enter the sentence:\n")
substr = input("Enter the substring: ")

sentlen, sublen, pos = len(sent), len(substr), ""

for i in range(sentlen-sublen+1):
    if sent[i:i+sublen].lower() == substr.lower():
        pos+= str(i+1) if pos=="" else ", "+str(i+1)

if pos=="":
    print("\nSubstring",substr,"could not be found in the sentence!\n")
else:
    print("\n",substr," exists at position(s): ",pos,"\n", sep='')

# You work as if you are already in US 2090 with Robots all around working with high calibre machines
# with extreme capacity!!

# Substring is one word