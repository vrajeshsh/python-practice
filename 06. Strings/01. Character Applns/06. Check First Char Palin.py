import os
os.system("cls")

ini, rev_ini, sentLen = "", "", 0

sent = input("Enter a sentence to display first letters:\n")
sentLen = len(sent)
for i in range(sentLen):
    ch= sent[i].upper()
    if i==0 or sent[i-1]==' ':
        ini+= ch+"."
        rev_ini= ch+"."+rev_ini

print("\nInitials: ",ini,
    "\nThis string is ","NOT " if ini != rev_ini else "",
        "a Palindrome!\n", sep='')

# Tricks and Gimmicks are supposed to be used by Magicians!!
# Use them when by depth you have become ONE